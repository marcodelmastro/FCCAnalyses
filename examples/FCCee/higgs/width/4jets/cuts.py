#Input directory where the files produced at the pre-selection level are
inputDir  = "/scratch/combes/stage2/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "/scratch/combes/final/cutshisto/"

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
               'wzp6_ee_mumu_ecm240':{},
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
               'wzp6_ee_ee_Mee_30_150_ecm240':{},
               'p8_ee_ZZ_ecm240':{},#Run the full statistics in one output file named <outputDir>/p8_ee_ZZ_ecm240.root
               'p8_ee_WW_ecm240':{} #Run 50% of the statistics in two files named <outputDir>/p8_ee_WW_ecm240/chunk<N>.root
    #'p8_ee_ZH_ecm240':{'fraction':0.2, 'output':'p8_ee_ZH_ecm240_out'} #Run 20% of the statistics in one file named <outputDir>/p8_ee_ZH_ecm240_out.root (example on how to change the output name)
               }


#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
#procDictAdd={"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

#Number of CPUs to use
nCPUS = 8

#produces ROOT TTrees, default is False
doTree = False
doScale = True
#cutList = {f"sel0":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40",
#           "sel1":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+5",
#           "sel2":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+10",
#           "sel3":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+15",
#           "sel4":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+20",
#           "sel5":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+25",
#           "sel6":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+30",
#           "sel7":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+35",
#           "sel8":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+40",
#           "sel9":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+45",
#           "sel10":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 40+50"
#              }

cutList = {f"sel0": " Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0",
              "sel1":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+5",
              "sel2":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+10",
              "sel3":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+15",
              "sel4":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+20",
              "sel5":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+25",
              "sel6":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+30",
              "sel7":" Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+35",
              "sel8":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+40",
              "sel9":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+45",
              "sel10":"Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && N_selected_leptons == 2 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23 > 0+50"
              }


#cutList = {"sel9":"Zcand_m > 73",
#           "sel10":"Zcand_m > 73 + 1",
#           "sel11":"Zcand_m > 73 + 2",
#           "sel12":"Zcand_m > 73 + 3",
#           "sel13":"Zcand_m > 73 + 4",
#           "sel14":"Zcand_m > 73 + 5",
#           "sel15":"Zcand_m > 73 + 6",
#           "sel16":"Zcand_m > 73 + 7",
#           "sel17":"Zcand_m > 73 + 8",
#           "sel18":"Zcand_m > 73 + 9",
#           "sel19":"Zcand_m > 73 + 10"}
#
#cutList = {"sel0":"Zcand_m < 97",
#           "sel1":"Zcand_m < 98",
#           "sel2":"Zcand_m < 99",
#           "sel3":"Zcand_m < 100",
#           "sel4":"Zcand_m < 101",
#           "sel5":"Zcand_m < 102",
#           "sel6":"Zcand_m < 103",
#           "sel7":"Zcand_m < 104",
#           "sel8":"Zcand_m < 105",
#           "sel9":"Zcand_m < 106",
#           "sel10":"Zcand_m < 107"
#       }
#
#cutList = {"sel0":"etmiss < 10",
#           "sel1":"etmiss < 11",
#           "sel2":"etmiss < 12",
#           "sel3":"etmiss < 13",
#           "sel4":"etmiss < 14",
#           "sel5":"etmiss < 35",
#           "sel6":"etmiss < 16",
#           "sel7":"etmiss < 17",
#           "sel8":"etmiss < 18",
#           "sel9":"etmiss < 19",
#           "sel10":"etmiss < 20"
#       }
#
#cutList = {"sel0":"Zcand_recoil_m < 137",
#           "sel1":"Zcand_recoil_m < 138",
#           "sel2":"Zcand_recoil_m < 139",
#           "sel3":"Zcand_recoil_m < 140",
#           "sel4":"Zcand_recoil_m < 141",
#           "sel5":"Zcand_recoil_m < 142",
#           "sel6":"Zcand_recoil_m < 143",
#           "sel7":"Zcand_recoil_m < 144",
#           "sel8":"Zcand_recoil_m < 145",
#           "sel9":"Zcand_recoil_m < 146",
#           "sel10":"Zcand_recoil_m < 147"
#       }
#
#cutList = {"sel0":"Zcand_recoil_m > 119",
#           "sel1":"Zcand_recoil_m > 120",
#           "sel2":"Zcand_recoil_m > 121",
#           "sel3":"Zcand_recoil_m > 122",
#           "sel4":"Zcand_recoil_m > 123",
#           "sel5":"Zcand_recoil_m > 124",
#           "sel6":"Zcand_recoil_m > 135",
#           "sel7":"Zcand_recoil_m > 126",
#           "sel8":"Zcand_recoil_m > 127",
#           "sel9":"Zcand_recoil_m > 128",
#           "sel10":"Zcand_recoil_m > 129"
#       }

histoList = {

"dmerge_4_34":{"name":"dmerge_4_34","title":"dmerge_4_34","bin":125,"xmin":0,"xmax":700},

"dmerge_4_23":{"name":"dmerge_4_23","title":"dmerge_4_23","bin":125,"xmin":0,"xmax":700},



 "mz":{"name":"Zcand_m","title":"m_{Z} [GeV]","bin":125,"xmin":0,"xmax":350},


}

