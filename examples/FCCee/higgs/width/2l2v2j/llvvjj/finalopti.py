#Input directory where the files produced at the pre-selection level are

inputDir = "outputs/fccee/higgs/mH-recoil/neutrinos/llvvjj/stage2/"

outputDir = "outputs/fccee/higgs/mH-recoil/neutrinos/llvvjj/final/cutshisto/"


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



cutList = {f"sel0":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50",
           "sel1":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50 + 10",
           "sel2":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50 + 20",
           "sel3":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 <50 + 30",
           "sel4":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50+40",
           "sel5":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50+50",
           "sel6":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 <50+60",
           "sel7":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 <50+70",
           "sel8":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50+80",
           "sel9":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50+90",
           "sel10":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 120 && Zcand_recoil_m < 160 && emiss > 20 && emiss <65 && secondZ_m < 38 && secondZ_m > 10 && dmerge_2_12 > 10  && secondZ_p < 40 && meanNconst > 7 && etmiss > 10 && dmerge_2_23 < 50+100"
       }

histoList = {

"dmerge_2_34":{"name":"dmerge_2_34","title":"dmerge_4_34","bin":125,"xmin":0,"xmax":700},

"dmerge_2_23":{"name":"dmerge_2_23","title":"dmerge_4_23","bin":125,"xmin":0,"xmax":700},





}
