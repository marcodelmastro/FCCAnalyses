#Input directory where the files produced at the pre-selection level are
inputDir  = "/sps/atlas/combes/FCCAnalyses/outputs/fccee/higgs/mH-recoil/hzz/stage2/4jets/Zleptonic/bdt_score_test1_4jets/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "/sps/atlas/combes/FCCAnalyses/outputs/fccee/higgs/mH-recoil/hzz/final/4jets/Zleptonique/bdt_score_test1_4jets/"

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
           "sel1":"myScore > 9",
           "sel2":"myScore > 9.5",
           "sel3":"myScore > 10",
}

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    
    "HZZ":{"name":"HZZ", "title":"HZZ score", "bin": 20,  "xmin":-10, "xmax":10},
    "HZZ_centered":{"name":"HZZ", "title":"HZZ score", "bin": 20,  "xmin":-1, "xmax":3},
    "HWW":{"name":"HWW", "title":"HWW score", "bin": 20,  "xmin":-10, "xmax":10},
    "Hbb":{"name":"Hbb", "title":"Hbb score", "bin": 20,  "xmin":-10, "xmax":10},
    "ZZ":{"name":"ZZ", "title":"ZZ score", "bin": 20,  "xmin":-10, "xmax":10},
    "WW":{"name":"WW", "title":"WW score", "bin": 20,  "xmin":-10, "xmax":10},
    "myScore_new":{"name":"myScore", "title":"Optimal variable", "bin":100, "xmin":-7, "xmax":11},
    "myScore_new_zoom":{"name":"myScore", "title":"Optimal variable", "bin":100, "xmin":-6, "xmax":11},

    "mz":{"name":"Zcand_m","title":"Dilepton mass [GeV]","bin":125,"xmin":70,"xmax":120},
    "N_selected_leptons":{"name":"N_selected_leptons", "title":"Number of selected leptons", "bin":100, "xmin":0, "xmax":10}, 
    "leptonic_recoil_m":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":100,"xmin":110,"xmax":150},


    


    "firstZ_m":{"name":"firstZ_m", "title":"Dijet mass of the jets chosen for the on-shell Z [GeV]", "bin":100, "xmin":50, "xmax":125},
    "firstZ_p":{"name":"firstZ_p", "title":"Dijet mom of the jets chosen for the on-shell Z [GeV]", "bin":100, "xmin":70, "xmax":110},
    "secondZ_m":{"name":"secondZ_m", "title":"mass of the Z2 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":90},
    "secondZ_p":{"name":"secondZ_p", "title":"mom of the Z2 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":200},
    "higgs_4_m":{"name":"higgs_4_m","title":"Higgs mass from the 2Z, Durham 4 [GeV]","bin":125,"xmin":0,"xmax":250},
    "higgs_4_p":{"name":"higgs_4_p","title":"Higgs mom from the 2Z, Durham 4 [GeV]","bin":125,"xmin":0,"xmax":250},
    "higgs_2_m":{"name":"higgs_2_m","title":"Higgs mass from the 2Z, Durham 2 [GeV]","bin":125,"xmin":0,"xmax":250},
    "emiss":{"name":"emiss", "title":"missing energy [GeV]", "bin":100, "xmin":0, "xmax":30},
    "pzmiss":{"name":"pzmiss", "title":"missing momentum [GeV]", "bin":100, "xmin":0, "xmax":30},
    "etmiss":{"name":"etmiss", "title":"transverse missing energy [GeV]", "bin":100, "xmin":0, "xmax":30},
    "mintheta":{"name":"mintheta","title":"Min Delta theta between the 4 Durham kt jets","bin":100,"xmin":-7,"xmax":7},


    "firstZ_m_antikt_ter":{"name":"firstZ_m_antikt_ter", "title":"mass of the Z1 (all jets apart from 3/4, Durham antikt R=0.8", "bin":100, "xmin":0, "xmax":200},
    "secondZ_m_antikt_ter":{"name":"secondZ_m_antikt_ter", "title":"mass of the Z2 (j3+j4, Durham antikt R=0.8)", "bin":100, "xmin":0, "xmax":200},
    "firstZ_m_antikt_1_2_ter":{"name":"firstZ_m_antikt_1_2_ter", "title":"mass of the Z1 (jet1+jet2 Durham antikt R=0.8", "bin":100, "xmin":0, "xmax":200},
    "firstZ_m_antikt_reco_ter":{"name":"firstZ_m_antikt_reco_ter", "title":"mass of the Z1 (reco Durham antikt R=0.8", "bin":100, "xmin":0, "xmax":200},


    "firstZ_m_antikt_bis":{"name":"firstZ_m_antikt_bis", "title":"mass of the Z1 (all jets apart from 3/4, Durham antikt R=0.6", "bin":100, "xmin":0, "xmax":200},
    "secondZ_m_antikt_bis":{"name":"secondZ_m_antikt_bis", "title":"mass of the Z2 (j3+j4, Durham antikt R=0.6)", "bin":100, "xmin":0, "xmax":200},
    "firstZ_m_antikt_1_2_bis":{"name":"firstZ_m_antikt_1_2_bis", "title":"mass of the Z1 (jet1+jet2 Durham antikt R=0.6", "bin":100, "xmin":0, "xmax":200},
    "firstZ_m_antikt_reco_bis":{"name":"firstZ_m_antikt_reco_bis", "title":"mass of the Z1 (reco Durham antikt R=0.6", "bin":100, "xmin":0, "xmax":200},


    "N_jets_antikt4_bis":{"name":"N_jets_antikt4_bis", "title":"Number of jets (Durham anti-kt 0.6)", "bin":60, "xmin":0, "xmax":60},
    "N_jets_antikt4_Ab5_bis":{"name":"N_jets_antikt4_Ab5_bis", "title":"Number of jets above 5GeV (Durham anti-kt 0.6)", "bin":20, "xmin":0, "xmax":20},
    "N_jets_antikt4_ter":{"name":"N_jets_antikt4_ter", "title":"Number of jets (Durham anti-kt 0.8)", "bin":60, "xmin":0, "xmax":60},
    "N_jets_antikt4_Ab5_ter":{"name":"N_jets_antikt4_Ab5_ter", "title":"Number of jets above 5GeV (Durham anti-kt 0.8)", "bin":20, "xmin":0, "xmax":20},

    "dmerge_2_34":{"name":"dmerge_2_34","title":"d34","bin":125,"xmin":0,"xmax":400},
    "dmerge_2_23":{"name":"dmerge_2_23","title":"d23","bin":125,"xmin":0,"xmax":3000},
    "dmerge_2_45":{"name":"dmerge_2_45","title":"d45","bin":125,"xmin":0,"xmax":200},

    "jet1_e":{"name":"jet1_e","title":"energy of the first (highest p) jet from Durham4 [GeV]","bin":100,"xmin":0,"xmax":200},
    "jet2_e":{"name":"jet2_e", "title":"energy of the second jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet3_e":{"name":"jet3_e", "title":"energy of the third jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet4_e":{"name":"jet4_e", "title":"energy of the fourth jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},

    "jet1_theta":{"name":"jet1_theta", "title":"#theta of the 1st jet from Durham kt N=4 [GeV]", "bin":100, "xmin":0, "xmax":4},
    "jet2_theta":{"name":"jet2_theta", "title":"#theta of the 2nd jet from Durham kt N=4 [GeV]", "bin":100, "xmin":0, "xmax":4},
    "jet3_theta":{"name":"jet3_theta", "title":"#theta of the 3rd jet from Durham kt N=4 [GeV]", "bin":100, "xmin":0, "xmax":4},
    "jet4_theta":{"name":"jet4_theta", "title":"#theta of the 4th jet from Durham kt N=4 [GeV]", "bin":100, "xmin":0, "xmax":4},


    "N_LooseLeptons_2":{"name":"N_LooseLeptons_2", "title":"Number of leptons with p>2GeV", "bin":20, "xmin":0, "xmax":20},
    "N_LooseLeptons_1":{"name":"N_LooseLeptons_1", "title":"Number of leptons with p>1GeV", "bin":20, "xmin":0, "xmax":20},

    "angle_2_jet1_jet2":{"name":"angle_2_jet1_jet2", "title":"angle_2_jet1_jet2", "bin":100, "xmin":-4, "xmax":4},
    "angle_jet1_jet2":{"name":"angle_jet1_jet2", "title":"angle_jet1_jet2", "bin":100, "xmin":-4, "xmax":4},
    "angle_jet1_jet3":{"name":"angle_jet1_jet3", "title":"angle_jet1_jet3", "bin":100, "xmin":-4, "xmax":4},
    "angle_jet1_jet4":{"name":"angle_jet1_jet4", "title":"angle_jet1_jet4", "bin":100, "xmin":-4, "xmax":4},
    "angle_jet2_jet3":{"name":"angle_jet2_jet3", "title":"angle_jet2_jet3", "bin":100, "xmin":-4, "xmax":4},
    "angle_jet2_jet4":{"name":"angle_jet2_jet4", "title":"angle_jet2_jet4", "bin":100, "xmin":-4, "xmax":4},
    "angle_jet3_jet4":{"name":"angle_jet3_jet4", "title":"angle_jet3_jet4", "bin":100, "xmin":-4, "xmax":4},
    "angle_Z1_Z2":{"name":"angle_Z1_Z2", "title":"angle_Z1_Z2", "bin":100, "xmin":-4, "xmax":4},

    
    
    #"Hcc":{"name":"Hcc", "title":"Hcc score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Hss":{"name":"Hss", "title":"Hss score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Hgg":{"name":"Hgg", "title":"Hgg score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Hmumu":{"name":"Hmumu", "title":"Hmumu score", "bin": 20,  "xmin":-10, "xmax":10},
    #"Haa":{"name":"Haa", "title":"Haa score", "bin": 20,  "xmin":-10, "xmax":10},
    #"HZa":{"name":"HZa", "title":"HZa score", "bin": 20,  "xmin":-10, "xmax":10},
    



}

