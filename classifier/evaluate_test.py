import sys
#sys.path.insert(0, "/afs/cern.ch/user/s/selvaggi/.local/lib/python3.10/site-packages")

import pandas as pd
import xgboost as xgb
import numpy as np
import pickle
import uproot as up
import os
import glob
import ROOT

import concurrent.futures
import argparse
import importlib
import json




jsonfile=os.path.join(os.getenv('FCCDICTSDIR'), 'FCCee_procDict_winter2023_IDEA.json')
metadata = json.load(open(jsonfile))
print(metadata)
Nevents = metadata['wzp6_ee_eeH_HZZ_ecm240']['sumOfWeights']
xs = metadata['wzp6_ee_eeH_HZZ_ecm240']['crossSection']
print("Example 1:", Nevents, xs)

def mergeProcesses(md, p_merged, *args):
    md[p_merged] = {'crossSection':0, 'sumOfWeights':0, 'numberOfEvents':0}
    for a in args:
        for kw in ['crossSection', 'sumOfWeights', 'numberOfEvents']:
            md[p_merged][kw] += md[a][kw]

# petite fonction pour se faciliter la vie et sommer les ee et mumu

mergeProcesses(metadata, 'llHZZ', 'wzp6_ee_eeH_HZZ_ecm240', 'wzp6_ee_mumuH_HZZ_ecm240')
print("Values for llHZZ:")
print("Sum of weigths:", metadata['llHZZ']['sumOfWeights'])
print("cross-section:", metadata['llHZZ']['crossSection'])

#HWW
mergeProcesses(metadata, 'llHWW', 'wzp6_ee_eeH_HWW_ecm240', 'wzp6_ee_mumuH_HWW_ecm240')
#Hbb
mergeProcesses(metadata, 'llHbb', 'wzp6_ee_eeH_Hbb_ecm240', 'wzp6_ee_mumuH_Hbb_ecm240')
#Htautau
#mergeProcesses(metadata, 'llHtautau', 'wzp6_ee_eeH_Htautau_ecm240', 'wzp6_ee_mumuH_Htautau_ecm240')
#Hgg
mergeProcesses(metadata, 'llHgg', 'wzp6_ee_eeH_Hgg_ecm240', 'wzp6_ee_mumuH_Hgg_ecm240')
mergeProcesses(metadata, 'llHcc', 'wzp6_ee_eeH_Hcc_ecm240', 'wzp6_ee_mumuH_Hcc_ecm240')

# Parse command line arguments
parser = argparse.ArgumentParser(description="Load config file.")
parser.add_argument("config_file", help="Configuration file to load.")
args = parser.parse_args()


# Import config file
# Import config file
config_file_path = args.config_file
config_dir, config_file_name = os.path.split(config_file_path)
config_module_name = config_file_name.rstrip(".py")

# Add the config directory to sys.path to ensure the config module can be found
sys.path.append(config_dir)
config = importlib.import_module(config_module_name)

final_states = config.final_states
path = config.path
vars = config.vars
processes = config.processes
v = config.v
ncpus = config.ncpus

print(xgb.__version__)
print(up.__version__)


# Define the function to evaluate the model on a single root file
def evaluate_file(model, file_in):
    proc_dir = os.path.dirname(file_in)
    score_dir = "{}_{}".format(proc_dir, score_tag)
    
    os.system("mkdir -p {}".format(score_dir))
    #print(file_in)
    
    fileup = up.open(file_in)
    print("file in is opened")
    tree = fileup["events"]
    print("tree")
    data = tree.arrays(vars, library="pd")

    
    #dfs = up.iterate("{}:events".format(file_in), library="pd") 
    #data = pd.concat(dfs, ignore_index=True)

    # Get the variables for classification
    scores = model.predict_proba(data[vars])
    

    # Add the predicted class to the data
    maxval = 1e99
    minval = -1e99
    for i, name in enumerate(final_states.keys()):
        
        data[name] = np.log10(scores[:, i] / (1 - scores[:, i]))
        # data[name] = scores[:, i]
        
    data["myScore"] = np.log10(scores[:,0] / ((metadata['llHWW']['crossSection']/metadata['llHWW']['numberOfEvents'])*scores[:,1] + (metadata['llHbb']['crossSection']/metadata['llHbb']['numberOfEvents'])*scores[:,2] + (metadata['llHgg']['crossSection']/metadata['llHgg']['numberOfEvents'])*scores[:,5] + (metadata['p8_ee_ZZ_ecm240']['crossSection']/metadata['p8_ee_ZZ_ecm240']['numberOfEvents'])*scores[:,3] + (metadata['p8_ee_WW_ecm240']['crossSection']/metadata['p8_ee_WW_ecm240']['numberOfEvents'])*scores[:,4])+ (metadata['llHcc']['crossSection']/metadata['llHcc']['numberOfEvents'])*scores[:,6])
# + (metadata['llHgg']['crossSection']/metadata['llHgg']['numberOfEvents'])*scores[:,6]))
    print("data=", data["myScore"])

    file_out = "{}/{}".format(score_dir, os.path.basename(file_in))
      
    ufile_out = up.recreate(file_out)
    
    ufile_out["events"] = data

    rfile_in = ROOT.TFile(file_in)
    tparam = rfile_in.eventsProcessed

    print("writing file {} ... ".format(file_out))

    rfile_out = ROOT.TFile(file_out, "update")
    tparam.Write()
    rfile_out.Close()

   

# Define the function to evaluate the model on a single root file
def evaluate_process(model, proc_dir, score_tag):

    files = glob.glob("{}/*.root".format(proc_dir))

    # Define the output ROOT file and tree
    score_dir = "{}_{}".format(proc_dir, score_tag)
    os.system("mkdir -p {}".format(score_dir))

    print("mkdir -p {}".format(score_dir))
    
    for file_in in files:

        dfs = up.iterate("{}:events".format(file_in), library="pd")

        data = pd.concat(dfs, ignore_index=True)

        # Get the variables for classification
        scores = model.predict_proba(data[vars])

        # Add the predicted class to the data
        maxval = 1e99
        minval = -1e99
        
        
        for i, name in enumerate(final_states.keys()):

            scores_i = scores[:, i]
            # Apply the conditions
            data[name] = np.where(scores_i <= 0, -15,
             np.where(scores_i >= 1, 15,
             np.log10(scores_i / (1 - scores_i))))
	
        

        file_out = "{}/{}".format(score_dir, os.path.basename(file_in))
        ufile_out = up.recreate(file_out)
        ufile_out["events"] = data

        rfile_in = ROOT.TFile(file_in)
        tparam = rfile_in.eventsProcessed

        print(score_dir)
        print("writing file {} ... ".format(file_out))

        rfile_out = ROOT.TFile(file_out, "update")
        tparam.Write()
        rfile_out.Close()
    



# Load the trained model from file
with open("model_{}.pkl".format(v), "rb") as f:
    model = pickle.load(f)
    print('model loaded')


score_tag = "score_{}".format(v)

files = []
for proc in processes:
    
    proc_dir = os.path.dirname(proc.files)    
    proc_files = glob.glob("{}/*.root".format(proc_dir))
    print(proc_dir)
    for f in proc_files:
        files.append(f)
        

for i, file_in in enumerate(files):
    print(file_in)
    evaluate_file(model, file_in)


#with concurrent.futures.ThreadPoolExecutor() as executor:
    # Use a lambda to include model in function arguments
#    executor.map(lambda file_in: evaluate_file(model, file_in), files)
