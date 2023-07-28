

#Input directory where the files produced at the pre-selection level are
inputDir  = "outputs/fccee/higgs/mH-recoil/hzz/stage2/4jets/Zleptonic/woutfilter/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs/fccee/higgs/mH-recoil/hzz/final/4jets/Zleptonique/woutfilter/"

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
              # 'wzp6_ee_mumu_ecm240':{},
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
               #'wzp6_ee_ee_Mee_30_150_ecm240':{},
               'p8_ee_ZZ_ecm240':{},#Run the full statistics in one output file named <outputDir>/p8_ee_ZZ_ecm240.root
               'p8_ee_WW_ecm240':{} #Run 50% of the statistics in two files named <outputDir>/p8_ee_WW_ecm240/chunk<N>.root
    #'p8_ee_ZH_ecm240':{'fraction':0.2, 'output':'p8_ee_ZH_ecm240_out'} #Run 20% of the statistics in one file named <outputDir>/p8_ee_ZH_ecm240_out.root (example on how to change the output name)
               }

#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
#procDictAdd={"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

#Number of CPUs to use
nCPUS = 32

#produces ROOT TTrees, default is False
doTree = False
doScale = True
###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
#cutList = {"sel0":"Zcand_q == 0",
#            "sel1":"Zcand_q == -1 || Zcand_q == 1",
#            "sel2":"Zcand_m > 80 && Zcand_m < 100",
#            "sel3":"MyFilter==true && (Zcand_m < 80 || Zcand_m > 100)"
#            }

cutList = {"sel0":"Zcand_cos < 2", #aucun cut
           "sel1":"N_selected_leptons == 2",
           "sel2":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101",
           "sel3":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140",
           "sel4":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 ",
           "sel5":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15",

	   "sel6":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && higgs_4_m > 110 && higgs_4_m < 138",

          "sel7":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15 && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60",

	   "sel8":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15  && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23>250"

          # "sel9":"N_selected_leptons == 2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && etmiss < 13 && pzmiss < 15  && higgs_4_m > 110 && higgs_4_m < 138 && dmerge_4_34 > 60 && dmerge_4_23>250 && jetconstituents_antikt4_4 > 2",



          # "sel7":"Zcand_m > 81 && Zcand_m < 101 && abs(Zcand_cos) < 0.9  && Zcand_recoil_m > 120 && Zcand_recoil_m < 140 && higgs_4_m > 100 && higgs_4_m < 150 && emiss < 30 && abs(Zcand_y)<1 && dmerge_4_34 > 10 ",
           #"sel8":"Zcand_m > 81 && Zcand_m < 101 && abs(Zcand_cos) < 0.9  && Zcand_recoil_m > 120 && Zcand_recoil_m < 140 && higgs_4_m > 100 && higgs_4_m < 150 && emiss < 30 && abs(Zcand_y)<1 && dmerge_4_34 > 10 && jet1_e < 80 && jet2_e < 60 && jet2_e > 20 ", 
           #"sel9":"Zcand_m > 81 && Zcand_m < 101 && abs(Zcand_cos) < 0.9  && Zcand_recoil_m > 120 && Zcand_recoil_m < 140 && higgs_4_m > 100 && higgs_4_m < 150 && emiss < 30 && abs(Zcand_y)<1 && dmerge_4_34 > 10 && jet1_e < 80 && jet2_e < 60 && jet2_e > 20 && jet3_e < 40 && jet3_e > 10",
           #"sel10":"Zcand_m > 81 && Zcand_m < 101 && abs(Zcand_cos) < 0.9  && Zcand_recoil_m > 120 && Zcand_recoil_m < 140 && higgs_4_m > 100 && higgs_4_m < 150 && emiss < 30 && abs(Zcand_y)<1 && dmerge_4_34 > 10 && jet1_e < 80 && jet2_e < 60 && jet2_e > 20 && jet3_e < 40 && jet3_e > 10 && flavourZ1 > 1",
           #"sel11": "Zcand_m > 81 && Zcand_m < 101 && abs(Zcand_cos) < 0.9  && Zcand_recoil_m > 120 && Zcand_recoil_m < 140 && higgs_4_m > 100 && higgs_4_m < 150 && emiss < 30 && abs(Zcand_y)<1 && dmerge_4_34 > 10 && jet1_e < 80 && jet2_e < 60 && jet2_e > 20 && jet3_e < 40 && jet3_e > 10 && flavourZ1 > 1 && firstZ_m > 81 && firstZ_m < 101"
           
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    "mz":{"name":"Zcand_m","title":"Dilepton mass [GeV]","bin":125,"xmin":0,"xmax":200},
    "mz_zoom":{"name":"Zcand_m","title":"Dilepton mass [GeV]","bin":40,"xmin":79,"xmax":103},
    "theta":{"name":"Zcand_theta","title":"theta","bin":100,"xmin":-7,"xmax":7},
    "phi":{"name":"Zcand_phi","title":"phi","bin":100,"xmin":-7,"xmax":7},
    "cos":{"name":"Zcand_cos","title":"costheta","bin":100,"xmin":-1,"xmax":1},
    "eta":{"name":"Zcand_eta","title":"eta","bin":100,"xmin":-10,"xmax":10},
    "y":{"name":"Zcand_y","title":"rapidity y","bin":100,"xmin":-5,"xmax":5},
    

    "leptonic_recoil_m":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":100,"xmin":0,"xmax":200},
    "leptonic_recoil_m_zoom":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":200,"xmin":80,"xmax":160},
    "leptonic_recoil_m_zoom1":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":100,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom2":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":200,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom3":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":400,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom4":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":800,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom5":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":2000,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom6":{"name":"Zcand_recoil_m","title":"Z leptonic recoil [GeV]","bin":100,"xmin":122,"xmax":125},

    "selected_muons_e":{"name":"selected_muons_e","title":"Energie of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_e":{"name":"selected_electrons_e","title":"Energie of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_e":{"name":"selected_leptons_e","title":"Energie of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":0, "xmax":200},


    "selected_muons_p":{"name":"selected_muons_p","title":"Mom of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_p":{"name":"selected_electrons_p","title":"Mom of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_p":{"name":"selected_leptons_p","title":"Mom of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":0, "xmax":200},


    "selected_muons_px":{"name":"selected_muons_px","title":"Momx of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_px":{"name":"selected_electrons_px","title":"Momx of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_px":{"name":"selected_leptons_px","title":"Momx of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},


"selected_muons_py":{"name":"selected_muons_py","title":"Momy of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_py":{"name":"selected_electrons_py","title":"Momy of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_py":{"name":"selected_leptons_py","title":"Momy of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},


    "selected_muons_pz":{"name":"selected_muons_pz","title":"Momz of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pz":{"name":"selected_electrons_pz","title":"Momz of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},
    "selected_leptons_pz":{"name":"selected_leptons_pz","title":"Momz of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_pt":{"name":"selected_muons_pt","title":"Transv Mom of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pt":{"name":"selected_electrons_pt","title":"Transv Mom of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_pt":{"name":"selected_leptons_pt","title":"Transv Mom of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":0, "xmax":200},

    "N_selected_leptons":{"name":"N_selected_leptons", "title":"Number of selected leptons", "bin":100, "xmin":0, "xmax":10}, 
    "N_zed_leptonic":{"name":"N_zed_leptonic", "title":"Number of reconstructed leptonic Z", "bin":100, "xmin":0, "xmax":10},


    "jet1_p":{"name":"jet1_p","title":"momentum of the first (highest p) jet from Durham4 [GeV]","bin":100,"xmin":0,"xmax":200},
    "jet2_p":{"name":"jet2_p", "title":"momentum of the second jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet3_p":{"name":"jet3_p", "title":"momentum of the third jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet4_p":{"name":"jet4_p", "title":"momentum of the fourth jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},

    "jet1_pt":{"name":"jet1_pt", "title":"transv momentum of the first (highest p) jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet2_pt":{"name":"jet2_pt", "title":"transv momentum of the second jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet3_pt":{"name":"jet3_pt", "title":"transv momentum of the third jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet4_pt":{"name":"jet4_pt", "title":"transv momentum of the fourth jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},

    "jet1_e":{"name":"jet1_e", "title":"energy of the first (highest p) jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet2_e":{"name":"jet2_e", "title":"energy of the second jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet3_e":{"name":"jet3_e", "title":"energy of the third jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet4_e":{"name":"jet4_e", "title":"energy of the fourth jet from Durham4 [GeV]", "bin":100, "xmin":0, "xmax":200},

    "dmerge_4_12":{"name":"dmerge_4_12","title":"dmerge_4_12","bin":125,"xmin":800,"xmax":1800},
    "dmerge_4_12_shift":{"name":"dmerge_4_12","title":"dmerge_4_12_shift","bin":125,"xmin":2000,"xmax":8000},
    "dmerge_4_23":{"name":"dmerge_4_23","title":"d23","bin":125,"xmin":0,"xmax":4000},
    "dmerge_4_23_zoom1":{"name":"dmerge_4_23","title":"dmerge_4_23 zoom gauche","bin":125,"xmin":200,"xmax":400},
    "dmerge_4_23_zoom2":{"name":"dmerge_4_23","title":"dmerge_4_23 zoom droite","bin":125,"xmin":550,"xmax":900},
    "dmerge_4_34":{"name":"dmerge_4_34","title":"dmerge_4_34","bin":125,"xmin":0,"xmax":1000},
    "dmerge_4_34_zoom":{"name":"dmerge_4_34","title":"dmerge_4_34_zoom","bin":125,"xmin":0,"xmax":150},
    "dmerge_4_45":{"name":"dmerge_4_45","title":"dmerge_4_45","bin":125,"xmin":0,"xmax":700},
    
    

    "firstZ_m":{"name":"firstZ_m", "title":"Dijet mass of the jets chosen for the on-shell Z [GeV]", "bin":100, "xmin":50, "xmax":125},
    "firstZ_p":{"name":"firstZ_p", "title":"momentum of the Z1 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":200},
    "firstZ_pt":{"name":"firstZ_pt", "title":"transv mom of the Z1 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":200},

     "secondZ_m":{"name":"secondZ_m", "title":"mass of the Z2 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":200},
    "secondZ_p":{"name":"secondZ_p", "title":"momentum of the Z2 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":200},
    "secondZ_pt":{"name":"secondZ_pt", "title":"transv mom of the Z2 after resobuilder for durham4", "bin":100, "xmin":0, "xmax":200},


    
    "higgs_4_m":{"name":"higgs_4_m","title":"Higgs mass from the 2Z, Durham 4 [GeV]","bin":125,"xmin":0,"xmax":250},
    #"higgs_4_p":{"name":"higgs_4_p","title":"Higgs momentum from the 2Z, Durham 4 [GeV]","bin":125,"xmin":0,"xmax":150},
    "higgs_4_m_zoom":{"name":"higgs_4_m","title":"Higgs mass from the 2Z, Durham 4 [GeV]","bin":105,"xmin":90,"xmax":150},
    #"diffmasshiggs":{"name":"diffmasshiggs","title":"Zcand_recoil_m - higgs_4_m [GeV]","bin":125,"xmin":0,"xmax":30},

    "higgs_2_m":{"name":"higgs_2_m","title":"Higgs mass from the 2Z, Durham 2 [GeV]","bin":125,"xmin":0,"xmax":250},

    "dmerge_2_12":{"name":"dmerge_2_12","title":"dmerge_2_12","bin":125,"xmin":0,"xmax":700},
    "dmerge_2_23":{"name":"dmerge_2_23","title":"dmerge_2_23","bin":125,"xmin":0,"xmax":700},
    "dmerge_2_34":{"name":"dmerge_2_34","title":"dmerge_2_34","bin":125,"xmin":0,"xmax":700},
    "dmerge_2_45":{"name":"dmerge_2_45","title":"dmerge_2_45","bin":125,"xmin":0,"xmax":700},


    "jet1_2_m":{"name":"jet1_2_m", "title":"mass of the Z1 (closest to mZ) from Durham2 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet2_2_m":{"name":"jet2_2_m", "title":"mass of the Z2 from Durham2 [GeV]", "bin":100, "xmin":0, "xmax":200},

    #"diffZ14":{"name":"diffZ14", "title":"difference for Z1 between the true inv mass and the one computed thx to Duhram 4/Reso Builder [GeV]","bin":100,"xmin":0, "xmax":50},
    #"diffZ24":{"name":"diffZ24", "title":"difference for Z2 between the true inv mass and the one computed thx to Duhram 4/Reso Builder [GeV]","bin":100,"xmin":0, "xmax":50},
    #"diffZ12":{"name":"diffZ12", "title":"difference for Z1  between the true inv mass and the one computed thx to Duhram 2 [GeV]","bin":100,"xmin":0, "xmax":100},
    #"diffZ22":{"name":"diffZ22", "title":"difference for Z2  between the true inv mass and the one computed thx to Duhram 2 [GeV]","bin":100,"xmin":0, "xmax":50},


    "emiss":{"name":"emiss", "title":"missing energy [GeV]", "bin":100, "xmin":0, "xmax":100},
    "pzmiss":{"name":"pzmiss", "title":"missing momentum [GeV]", "bin":100, "xmin":0, "xmax":100},
    "pzmiss_zoom":{"name":"pzmiss", "title":"missing momentum [GeV]", "bin":100, "xmin":0, "xmax":60},
    "etmiss":{"name":"etmiss", "title":"transverse missing energy [GeV]", "bin":100, "xmin":0, "xmax":100},
    "etmiss_zoom":{"name":"etmiss", "title":"transverse missing energy [GeV]", "bin":100, "xmin":0, "xmax":60},

    "Dtheta_ZZ1":{"name":"Dtheta_ZZ1","title":"Delta theta between Z and Z1","bin":100,"xmin":-7,"xmax":7},
    "Dtheta_ZZ2":{"name":"Dtheta_ZZ2","title":"Delta theta between Z and Z2","bin":100,"xmin":-7,"xmax":7},
    "Dtheta_Z1Z2":{"name":"Dtheta_Z1Z2","title":"Delta theta between Z1 and Z2","bin":100,"xmin":-7,"xmax":7},

    "firstZ_part1_flavour":{"name":"firstZ_part1_flavour","title":"Flavour of the 1st particle of the Z1 pair","bin":100,"xmin":0,"xmax":22},
    "firstZ_part2_flavour":{"name":"firstZ_part2_flavour","title":"Flavour of the 2nd particle of the Z1 pair","bin":100,"xmin":0,"xmax":22},
    "secondZ_part1_flavour":{"name":"secondZ_part1_flavour","title":"Flavour of the 1st particle of the Z2 pair","bin":100,"xmin":0,"xmax":22},
    "secondZ_part2_flavour":{"name":"secondZ_part2_flavour","title":"Flavour of the 2nd particle of the Z2 pair","bin":100,"xmin":0,"xmax":22},

    "firstZ_part1_flavour_gm":{"name":"firstZ_part1_flavour_gm","title":"Flavour gm of the 1st particle of the Z1 pair","bin":100,"xmin":0,"xmax":22},
    "firstZ_part2_flavour_gm":{"name":"firstZ_part2_flavour_gm","title":"Flavour gm of the 2nd particle of the Z1 pair","bin":100,"xmin":0,"xmax":22},
    "secondZ_part1_flavour_gm":{"name":"secondZ_part1_flavour_gm","title":"Flavour gm of the 1st particle of the Z2 pair","bin":100,"xmin":0,"xmax":22},
    "secondZ_part2_flavour_gm":{"name":"secondZ_part2_flavour_gm","title":"Flavour gm of the 2nd particle of the Z2 pair","bin":100,"xmin":0,"xmax":22},


    

    #"flavourscoreZ1":{"name":"flavourscoreZ1", "title":"Flavour score of the Z1 pair", "bin":100, "xmin":0, "xmax":3},
    #"flavourscoreZ2":{"name":"flavourscoreZ2", "title":"Flavour score of the Z2 pair", "bin":100, "xmin":0, "xmax":3},
    
    #"flavourscoreZ1_gm":{"name":"flavourscoreZ1_gm", "title":"Flavour gm score of the Z1 pair", "bin":100, "xmin":0, "xmax":3},
    #"flavourscoreZ2_gm":{"name":"flavourscoreZ2_gm", "title":"Flavour gm score of the Z2 pair", "bin":100, "xmin":0, "xmax":3},


    #"mz_recoil_2D":{"cols":["Zcand_m", "Zcand_recoil_m"],"title":"m_{Z} - leptonic recoil [GeV]", "bins": [(40,80,100), (100,120,140)]},
#    "flavourpartZ1":{"cols":["firstZ_part1_flavour", "firstZ_part2_flavour"],"title":"flavour of the first and second particules of the Z1 pair", "bins": [(100,0,22), (100,0,22)]},
#    "flavourpartZ2":{"cols":["secondZ_part1_flavour", "secondZ_part2_flavour"],"title":"flavour of the first and second particules of the Z2 pair", "bins": [(100,0,22), (100,0,22)]}, 
#    "flavourZ1Z2":{"cols":["flavourscoreZ1", "flavourscoreZ2"],"title":"flavour score for the Z1 and Z2 pairs", "bins": [(100,0,3), (100,0,3)]}, 
#
#
#    "flavourpartZ1_gm":{"cols":["firstZ_part1_flavour_gm", "firstZ_part2_flavour_gm"],"title":"flavour of the first and second particules of the Z1 pair", "bins": [(100,0,22), (100,0,22)]},
#    "flavourpartZ2_gm":{"cols":["secondZ_part1_flavour_gm", "secondZ_part2_flavour_gm"],"title":"flavour of the first and second particules of the Z2 pair", "bins": [(100,0,22), (100,0,22)]}, 
#    "flavourZ1Z2_gm":{"cols":["flavourscoreZ1_gm", "flavourscoreZ2_gm"],"title":"flavour score for the Z1 and Z2 pairs", "bins": [(100,0,3), (100,0,3)]}, 
#
#    "deltaetaZZ":{"name":"deltaetaZZ", "title":" |etaZ1 - etaZ2|", "bin":100, "xmin":0, "xmax":10},
#    "deltaetaZ1":{"name":"deltaetaZ1", "title":" |etajet1 - etajet2| du Z on shell", "bin":100, "xmin":0, "xmax":10},
#    "deltaetaZ2":{"name":"deltaetaZ2", "title":" |etajet1 - etajet2| du Z off shell", "bin":100, "xmin":0, "xmax":10},
#
#    "jetconstituents_4_1":{"name":"jetconstituents_4_1", "title":"Number of constituents of the first jet", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_4_2":{"name":"jetconstituents_4_2", "title":"Number of constituents of the second jet", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_4_3":{"name":"jetconstituents_4_3", "title":"Number of constituents of the third jet", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_4_4":{"name":"jetconstituents_4_4", "title":"Number of constituents of the fourth jet", "bin":100, "xmin":0, "xmax":100},
#
#
#    "N_jets_antikt4":{"name":"N_jets_antikt4", "title":"Number of jets (Durham anti-kt 0.4)", "bin":60, "xmin":0, "xmax":60},
#    "N_jets_antikt4_Ab5":{"name":"N_jets_antikt4_Ab5", "title":"Number of jets above 5GeV (Durham anti-kt 0.4)", "bin":20, "xmin":0, "xmax":20},
#    "N_jets_antikt4_Ab10":{"name":"N_jets_antikt4_Ab10", "title":"Number of jets above 10Gev (Durham anti-kt 0.4)", "bin":20, "xmin":0, "xmax":20},
#
#    "jet1_antikt4_energy":{"name":"jet1_antikt4_energy", "title":"Energy of the first jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":150},
#    "jet2_antikt4_energy":{"name":"jet2_antikt4_energy", "title":"Energy of the second jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":150},
#    "jet3_antikt4_energy":{"name":"jet3_antikt4_energy", "title":"Energy of the third jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":100},
#    "jet4_antikt4_energy":{"name":"jet4_antikt4_energy", "title":"Energy of the fourth jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":100},
#    "jet5_antikt4_energy":{"name":"jet5_antikt4_energy", "title":"Energy of the fourth jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":70},
#    "jet6_antikt4_energy":{"name":"jet6_antikt4_energy", "title":"Energy of the fourth jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":70},
#
#    
#    "jetconstituents_antikt4_1":{"name":"jetconstituents_antikt4_1", "title":"Number of constituents of the first jet (Durham-antikt 0.4)", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_antikt4_2":{"name":"jetconstituents_antikt4_2", "title":"Number of constituents of the second jet (Durham-antikt 0.4)", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_antikt4_3":{"name":"jetconstituents_antikt4_3", "title":"Number of constituents of the third jet (Durham-antikt 0.4)", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_antikt4_4":{"name":"jetconstituents_antikt4_4", "title":"Number of constituents of the fourth jet (Durham-antikt 0.4)", "bin":100, "xmin":0, "xmax":100},
#
#    "dmerge_antikt4_12":{"name":"dmerge_antikt4_12","title":"dmerge_4_12 antikt 0.4","bin":125,"xmin":0,"xmax":2000},
#    "dmerge_antikt4_23":{"name":"dmerge_antikt4_23","title":"dmerge_4_23 antikt 0.4","bin":125,"xmin":0,"xmax":1500},
#    "dmerge_antikt4_34":{"name":"dmerge_antikt4_34","title":"dmerge_4_34 antikt 0.4","bin":125,"xmin":0,"xmax":1000},
#    "dmerge_antikt4_45":{"name":"dmerge_antikt4_45","title":"dmerge_4_45 antikt 0.4","bin":125,"xmin":0,"xmax":1000},
#
#    "firstZ_m_antikt":{"name":"firstZ_m_antikt", "title":"mass of the Z1 (all jets apart from 3/4, Durham antikt R=0.4", "bin":100, "xmin":0, "xmax":200},
#    "secondZ_m_antikt":{"name":"secondZ_m_antikt", "title":"mass of the Z2 (j3+j4, Durham antikt R=0.4)", "bin":100, "xmin":0, "xmax":200},
#    "firstZ_m_antikt_1_2":{"name":"firstZ_m_antikt_1_2", "title":"mass of the Z1 (jet1+jet2 Durham antikt R=0.4", "bin":100, "xmin":0, "xmax":200},
#    "firstZ_m_antikt_reco":{"name":"firstZ_m_antikt_reco", "title":"mass of the Z1 (reco Durham antikt R=0.4", "bin":100, "xmin":0, "xmax":200},
#
#
#
#    "N_jets_antikt4_bis":{"name":"N_jets_antikt4_bis", "title":"Number of jets (Durham anti-kt 0.6)", "bin":60, "xmin":0, "xmax":60},
#    "N_jets_antikt4_Ab5_bis":{"name":"N_jets_antikt4_Ab5_bis", "title":"Number of jets above 5GeV (Durham anti-kt 0.6)", "bin":20, "xmin":0, "xmax":20},
#    "N_jets_antikt4_Ab10_bis":{"name":"N_jets_antikt4_Ab10_bis", "title":"Number of jets above 10Gev (Durham anti-kt 0.6)", "bin":20, "xmin":0, "xmax":20},
#
#    "jet1_antikt4_energy_bis":{"name":"jet1_antikt4_energy_bis", "title":"Energy of the first jet (Durham anti-kt 0.6)", "bin":100, "xmin":0, "xmax":150},
#    "jet2_antikt4_energy_bis":{"name":"jet2_antikt4_energy_bis", "title":"Energy of the second jet (Durham anti-kt 0.6)", "bin":100, "xmin":0, "xmax":150},
#    "jet3_antikt4_energy_bis":{"name":"jet3_antikt4_energy_bis", "title":"Energy of the third jet (Durham anti-kt 0.6)", "bin":100, "xmin":0, "xmax":100},
#    "jet4_antikt4_energy_bis":{"name":"jet4_antikt4_energy_bis", "title":"Energy of the fourth jet (Durham anti-kt 0.6)", "bin":100, "xmin":0, "xmax":100},
#    "jet5_antikt4_energy_bis":{"name":"jet5_antikt4_energy_bis", "title":"Energy of the fourth jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":70},
#    "jet6_antikt4_energy_bis":{"name":"jet6_antikt4_energy_bis", "title":"Energy of the fourth jet (Durham anti-kt 0.4)", "bin":100, "xmin":0, "xmax":70},
#
#
#    
#    "jetconstituents_antikt4_1_bis":{"name":"jetconstituents_antikt4_1_bis", "title":"Number of constituents of the first jet (Durham-antikt 0.6)", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_antikt4_2_bis":{"name":"jetconstituents_antikt4_2_bis", "title":"Number of constituents of the second jet(Durham-antikt 0.6)", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_antikt4_3_bis":{"name":"jetconstituents_antikt4_3_bis", "title":"Number of constituents of the third jet (Durham-antikt 0.6)", "bin":100, "xmin":0, "xmax":100},
#    "jetconstituents_antikt4_4_bis":{"name":"jetconstituents_antikt4_4_bis", "title":"Number of constituents of the fourth jet (Durham-antikt 0.6)", "bin":100, "xmin":0, "xmax":100},
#
#    "dmerge_antikt4_12_bis":{"name":"dmerge_antikt4_12_bis","title":"dmerge_4_12 antikt 0.6","bin":125,"xmin":0,"xmax":2000},
#    "dmerge_antikt4_23_bis":{"name":"dmerge_antikt4_23_bis","title":"dmerge_4_23 antikt 0.6","bin":125,"xmin":0,"xmax":1500},
#    "dmerge_antikt4_34_bis":{"name":"dmerge_antikt4_34_bis","title":"dmerge_4_34 antikt 0.6","bin":125,"xmin":0,"xmax":1000},
#    "dmerge_antikt4_45_bis":{"name":"dmerge_antikt4_45_bis","title":"dmerge_4_45 antikt 0.6","bin":125,"xmin":0,"xmax":1000}, 
#
#    "firstZ_m_antikt_bis":{"name":"firstZ_m_antikt_bis", "title":"mass of the Z1 (all jets apart from 3/4, Durham antikt R=0.6", "bin":100, "xmin":0, "xmax":200},
#    "secondZ_m_antikt_bis":{"name":"secondZ_m_antikt_bis", "title":"mass of the Z2 (j3+j4, Durham antikt R=0.6)", "bin":100, "xmin":0, "xmax":200},
#    "firstZ_m_antikt_1_2_bis":{"name":"firstZ_m_antikt_1_2_bis", "title":"mass of the Z1 (jet1+jet2 Durham antikt R=0.6", "bin":100, "xmin":0, "xmax":200},
#    "firstZ_m_antikt_reco_bis":{"name":"firstZ_m_antikt_reco_bis", "title":"mass of the Z1 (reco Durham antikt R=0.6", "bin":100, "xmin":0, "xmax":200},
#
#
#
#    "N_jets_antikt4_ter":{"name":"N_jets_antikt4_ter", "title":"Number of jets (Durham anti-kt 0.8)", "bin":60, "xmin":0, "xmax":60},
#    "N_jets_antikt4_Ab5_ter":{"name":"N_jets_antikt4_Ab5_ter", "title":"Number of jets above 5GeV (Durham anti-kt 0.8)", "bin":20, "xmin":0, "xmax":20},
#    "N_jets_antikt4_Ab10_ter":{"name":"N_jets_antikt4_Ab10_ter", "title":"Number of jets above 10Gev (Durham anti-kt 0.8)", "bin":20, "xmin":0, "xmax":20},
#
#    "firstZ_m_antikt_ter":{"name":"firstZ_m_antikt_ter", "title":"mass of the Z1 (all jets apart from 3/4, Durham antikt R=0.8", "bin":100, "xmin":0, "xmax":200},
#    "secondZ_m_antikt_ter":{"name":"secondZ_m_antikt_ter", "title":"mass of the Z2 (j3+j4, Durham antikt R=0.8)", "bin":100, "xmin":0, "xmax":200},
#    "firstZ_m_antikt_1_2_ter":{"name":"firstZ_m_antikt_1_2_ter", "title":"mass of the Z1 (jet1+jet2 Durham antikt R=0.8", "bin":100, "xmin":0, "xmax":200},
#    "firstZ_m_antikt_reco_ter":{"name":"firstZ_m_antikt_reco_ter", "title":"mass of the Z1 (reco Durham antikt R=0.8", "bin":100, "xmin":0, "xmax":200},
#
#    
#
#    "Dtheta_Z1":{"name":"Dtheta_Z1","title":"Delta theta between jet1&2 of the on shell Z","bin":100,"xmin":-7,"xmax":7},
#    "Dtheta_Z2":{"name":"Dtheta_Z2","title":"Delta theta jet1&2 of the off shell Z","bin":100,"xmin":-7,"xmax":7},
#    "Dphi_Z1":{"name":"Dphi_Z1","title":"Delta phi between jet1&2 of the on shell Z","bin":100,"xmin":-7,"xmax":7},
#    "Dphi_Z2":{"name":"Dphi_Z2","title":"Delta phi jet1&2 of the off shell Z","bin":100,"xmin":-7,"xmax":7},
#
#    "mintheta":{"name":"mintheta","title":"Min Delta theta between the 4 Durham kt jets","bin":100,"xmin":-7,"xmax":7},
#    "secondmintheta":{"name":"secondmintheta","title":"Second Min Delta theta between the 4 Durham kt jets","bin":100,"xmin":-7,"xmax":7},
#
#
#
#

}

