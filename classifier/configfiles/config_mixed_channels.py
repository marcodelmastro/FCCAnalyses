import os
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import uproot as up
import glob

# ______________________________________________________________________________________________________
def count_events(file, tree_name):
    #fileup = up.open(file)
    #tree = fileup[tree_name]
    
    # TODO: remove hardcoding num entries
    return 100000

# ______________________________________________________________________________________________________
def get_file_event_counts(file_list, tree_name):
    with ThreadPoolExecutor() as executor:
        event_counts = list(executor.map(count_events, file_list, [tree_name]*len(file_list)))
    return dict(zip(file_list, event_counts))

# ______________________________________________________________________________________________________
def get_optimized_file_list(file_event_counts, max_events):
    total_events = 0
    optimized_file_list = []

    for file, event_count in file_event_counts.items():
        total_events += event_count
        optimized_file_list.append(file)

        # Print current state of variables for debugging
        #print(f'File added: {file}')
        #print(f'Event count for file: {event_count}')
        #print(f'Total events so far: {total_events}')
        if total_events + event_count > max_events:
            break

    # Print final results
    print(f'Final file list: {optimized_file_list}')
    print(f'Total number of events: {total_events}')

    return optimized_file_list



def concatenate_files(file, tree_name, variables):

    fileup = up.open(file)
    tree = fileup[tree_name]
    data = tree.arrays(variables, library="pd")
        
    if set(data.columns) != set(variables):
        print(f"Unexpected columns in DataFrame: {set(data.columns) - set(variables)}")

    return data

def concatenate_files_wrapper(args):
    return concatenate_files(*args)

# ___________________________________________________________________________________________________
class Process:
    def __init__(self, name, files, category, weight, max_events):
        self.name = name     
        # Get optimized file list
        self.files = files
        self.category = category
        self.weight = weight
        self.max_events = int(max_events)

    def df(self, variables=[]):

        # Create a list of tuples each containing (file, tree_name, variables)
        # generate dict with filename: nevents
        file_event_counts = get_file_event_counts(glob.glob(self.files), "events")
        
        self.files = get_optimized_file_list(file_event_counts, max_events)
        
        tasks = [(file, "events", variables) for file in self.files]

        #df = concatenate_files(self.files, "events", variables, self.max_events)
        
        # Use as many cores as available
        with ProcessPoolExecutor() as executor:
            results = list(executor.map(concatenate_files_wrapper, tasks))
            
        # results is a list of DataFrames
        df = pd.concat(results, ignore_index=True)       
        df["target"] = self.category

        nev = len(df.index)
        if self.max_events > nev:
            print(
                "WARNING: requested {}, but found only {} events in {}, using only {}".format(
                    self.max_events, nev, self.name, nev
                )
            )

        if self.max_events < nev:
            return df.iloc[: self.max_events]
        else:
            return df


# _____________________________________________________________________________________________________
# data




final_states = {
    "HZZ":0,
    "HWW": 1,
    "Hbb": 2,
    "Htautau": 3,
    "ZZ":4,
    "WW":5,
    #"Hgg":6,
    #"Hcc":6,
    #"Hss":7,
    #"Hmumu":8,
    #"Hgg":9,
    #"Haa":10,
    #"HZa":11,
}






vars = ["N_selected_leptons",
        "Zcand_m",
        "Zcand_recoil_m",
        "secondZ_m",
        "secondZ_p",
        "jet1_e",
        "jet2_e",
        "jet1_theta", 
        "jet2_theta", 
        "emiss",
        "etmiss",
        "pzmiss",
        "dmerge_2_34",
        "dmerge_2_23",
        "dmerge_2_12", 
        "visible_mass_predef", 
        "N_LooseLeptons_2",
        "N_LooseLeptons_1",
        "minNconst",
        "maxNconst",
        "meanNconst",
        "minNconst_3",
        "maxNconst_3",
        "meanNconst_3",
        "mon_missing_theta",
        "angle_miss_jet1",
        "angle_miss_jet2",
        "min_angle_miss_jet", 
        "angle_jet1_jet2",
        "angle_dilepton_miss",
        "angle_dijet_miss",
        "angle_dijet_dilepton",
        "recoil_dijet_m",
        "dilepton_miss_m",
        "dijet_miss_m",

]

max_events = 3.3e6
ncpus = 128
v = "6classes_vvlljj"

## for training
#path = "/eos/experiment/fcc/ee/analyses/case-studies/higgs/flat_trees/zh_vvjj_var_training_v3/"

## for evaluation
#path = "/eos/experiment/fcc/ee/analyses/case-studies/higgs/flat_trees/zh_vvjj_var_v3/"

#for evaluation:
path = "outputs/fccee/higgs/mH-recoil/neutrinos/vvlljj/stage2/bdt/woutfilter/"

#for training:
#path = "outputs/fccee/higgs/mH-recoil/neutrinos/vvlljj/stage2/bdt/mergedtrees/"

#cas vvlljj

#processes = []
#for proc, index in final_states.items():
#    if proc not in ["HZZ","WW", "ZZ"]:
#        processes.append(Process(proc, "{}/wzp6_ee_{}_ecm240.root".format(path, proc), index, 1.0, max_events))
#    elif proc == "HZZ":
#        processes.append(Process(proc, "{}/wzp6_ee_nunuH_HZZ_ecm240.root".format(path), index, 1.0, max_events))
#    else:
#        processes.append(Process(proc, "{}/p8_ee_{}_ecm240.root".format(path, proc), index, 1.0, max_events))



processes = []
for proc, index in final_states.items():
    if proc not in ["WW", "ZZ"]:
        processes.append(Process(proc, "{}/wzp6_ee_{}_ecm240.root".format(path, proc), index, 1.0, max_events))
    else:
        processes.append(Process(proc, "{}/p8_ee_{}_ecm240.root".format(path, proc), index, 1.0, max_events))

