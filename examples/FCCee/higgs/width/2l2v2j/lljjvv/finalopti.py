#Input directory where the files produced at the pre-selection level are

inputDir = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/stage2/"

outputDir = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/cutshisto/"


processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},
               'wzp6_ee_eeH_HZZ_ecm240':{},
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_nunuH_HZZ_ecm240':{},
               'wzp6_ee_nunuH_HWW_ecm240':{},
               'wzp6_ee_nunuH_HZa_ecm240':{},
               'wzp6_ee_nunuH_Hbb_ecm240':{},
               'wzp6_ee_nunuH_Hcc_ecm240':{},
               'wzp6_ee_nunuH_Hgg_ecm240':{},
               'wzp6_ee_nunuH_Hmumu_ecm240':{},
               'wzp6_ee_nunuH_Hss_ecm240':{},
               'wzp6_ee_nunuH_Htautau_ecm240':{},
               #'wzp6_ee_mumu_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
               #'wzp6_ee_ee_Mee_30_150_ecm240':{},
               'p8_ee_ZZ_ecm240':{},
               'p8_ee_WW_ecm240':{}
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



cutList = {f"sel0":"Zcand_cos < 2",
           "sel1":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128",
           "sel2":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+1",
           "sel3":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+2",
           "sel4":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+3",
           "sel5":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+4",
           "sel6":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+5",
           "sel7":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+6",
           "sel8":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+7",
           "sel9":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+8",
           "sel10":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+9",
           "sel11":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124  && meanNconst > 8 && secondZ_m < 95 && secondZ_m > 67 && abs(cos(missing_theta)) < 0.96 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && dmerge_2_23 < 100 && Zcand_recoil_m < 128+10"
       }

histoList = {

"dmerge_2_34":{"name":"dmerge_2_34","title":"dmerge_4_34","bin":125,"xmin":0,"xmax":700},

"dmerge_2_23":{"name":"dmerge_2_23","title":"dmerge_4_23","bin":125,"xmin":0,"xmax":700},

"secondZ_m":{"name":"secondZ_m", "title":"Dijet mass (Durham kt N=2)", "bin":100, "xmin":0, "xmax":200},


"leptonic_recoil_m":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass of the lepton pair [GeV]","bin":100,"xmin":0,"xmax":200},



}
