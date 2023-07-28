#Input directory where the files produced at the pre-selection level are
inputDir  = "outputs/fccee/higgs/mH-recoil/neutrinos/vvlljj/stage2/bdt/woutfilter_score_6classes_vvlljj/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs/fccee/higgs/mH-recoil/neutrinos/vvlljj/final/woutfilter_score_6classes_vvlljj/"

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               #'wzp6_ee_mumu_ecm240':{},
               'wzp6_ee_nunuH_HZZ_ecm240':{},
               #'wzp6_ee_nunuH_HWW_ecm240':{},
               'wzp6_ee_nunuH_HZa_ecm240':{},
              ## 'wzp6_ee_nunuH_Haa_ecm240':{},
               'wzp6_ee_nunuH_Hbb_ecm240':{},
              # 'wzp6_ee_nunuH_Hcc_ecm240':{},
              # 'wzp6_ee_nunuH_Hgg_ecm240':{},
               'wzp6_ee_nunuH_Hmumu_ecm240':{},
              # 'wzp6_ee_nunuH_Hss_ecm240':{},
              # 'wzp6_ee_nunuH_Htautau_ecm240':{},

               'wzp6_ee_eeH_HZZ_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
              # 'wzp6_ee_ee_Mee_30_150_ecm240':{},
               'p8_ee_ZZ_ecm240':{},#Run the full statistics in one output file named <outputDir>/p8_ee_ZZ_ecm240.root
               'p8_ee_WW_ecm240':{} #Run 50% of the statistics in two files named <outputDir>/p8_ee_WW_ecm240/chunk<N>.root
    #'p8_ee_ZH_ecm240':{'fraction':0.2, 'output':'p8_ee_ZH_ecm240_out'} #Run 20% of the statistics in one file named <outputDir>/p8_ee_ZH_ecm240_out.root (example on how to change the output name)
               }

#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
#procDictAdd={"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

#Number of CPUs to use
nCPUS = 64

#produces ROOT TTrees, default is False
doTree = False
doScale = False
###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
#cutList = {"sel0":"Zcand_q == 0",
#            "sel1":"Zcand_q == -1 || Zcand_q == 1",
#            "sel2":"Zcand_m > 80 && Zcand_m < 100",
#            "sel3":"MyFilter==true && (Zcand_m < 80 || Zcand_m > 100)"
#            }

cutList = {"sel0":"HZZ < 20",
           "sel1":"ZZ < 1",
           "sel2":"ZZ < 1 && WW < 0",
           "sel3":"ZZ < 1 && WW < 0 && HWW < 2",
           "sel4":"ZZ < 1 && WW < 0 && HWW < 2 && Htautau < 0",

           "sel5":"ZZ < 1 && WW < 0 && HWW < 2 && Htautau < 0 && Hbb < 2"
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    
    "HZZ":{"name":"HZZ", "title":"HZZ score", "bin": 20,  "xmin":-10, "xmax":10},
    "HZZ_centered":{"name":"HZZ", "title":"HZZ score", "bin": 20,  "xmin":-1, "xmax":3},
    "HWW":{"name":"HWW", "title":"HWW score", "bin": 20,  "xmin":-10, "xmax":10},
    "Hbb":{"name":"Hbb", "title":"Hbb score", "bin": 20,  "xmin":-10, "xmax":10},
    "Htautau":{"name":"Htautau", "title":"Htautau score", "bin": 20,  "xmin":-10, "xmax":10},
    "ZZ":{"name":"ZZ", "title":"ZZ score", "bin": 20,  "xmin":-10, "xmax":10},
    "WW":{"name":"WW", "title":"WW score", "bin": 20,  "xmin":-10, "xmax":10},
    "myScore_new":{"name":"myScore", "title":"Optimal variable", "bin":100, "xmin":-4, "xmax":15},
    "myScore_new_zoom":{"name":"myScore", "title":"Optimal variable", "bin":100, "xmin":-1, "xmax":13},

    
    #"Hcc":{"name":"Hcc", "title":"Hcc score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Hss":{"name":"Hss", "title":"Hss score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Hgg":{"name":"Hgg", "title":"Hgg score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Hmumu":{"name":"Hmumu", "title":"Hmumu score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Haa":{"name":"Haa", "title":"Haa score", "bin": 20,  "xmin":-10, "xmax":10},
    #"HZa":{"name":"HZa", "title":"HZa score", "bin": 20,  "xmin":-10, "xmax":10},
    



}

