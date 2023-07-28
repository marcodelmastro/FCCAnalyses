#Input directory where the files produced at the pre-selection level are
inputDir  = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/stage2/"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/"

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},
              # 'wzp6_ee_mumuH_HWW_ecm240':{},
              # 'wzp6_ee_mumuH_HZa_ecm240':{},
              # 'wzp6_ee_mumuH_Haa_ecm240':{},
              # 'wzp6_ee_mumuH_Hbb_ecm240':{},
              # 'wzp6_ee_mumuH_Hcc_ecm240':{},
              # 'wzp6_ee_mumuH_Hgg_ecm240':{},
              # 'wzp6_ee_mumuH_Hmumu_ecm240':{},
              # 'wzp6_ee_mumuH_Hss_ecm240':{},
              # 'wzp6_ee_mumuH_Htautau_ecm240':{},
              # #'wzp6_ee_mumu_ecm240':{},
              # 'wzp6_ee_nunuH_HZZ_ecm240':{},
              # 'wzp6_ee_nunuH_HWW_ecm240':{},
              # 'wzp6_ee_nunuH_HZa_ecm240':{},
              ## 'wzp6_ee_nunuH_Haa_ecm240':{},
              # 'wzp6_ee_nunuH_Hbb_ecm240':{},
              # 'wzp6_ee_nunuH_Hcc_ecm240':{},
              # 'wzp6_ee_nunuH_Hgg_ecm240':{},
              # 'wzp6_ee_nunuH_Hmumu_ecm240':{},
              # 'wzp6_ee_nunuH_Hss_ecm240':{},
              # 'wzp6_ee_nunuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HZZ_ecm240':{},
              # 'wzp6_ee_eeH_HWW_ecm240':{},
              # 'wzp6_ee_eeH_HZa_ecm240':{},
              # 'wzp6_ee_eeH_Haa_ecm240':{},
              # 'wzp6_ee_eeH_Hbb_ecm240':{},
              # 'wzp6_ee_eeH_Hcc_ecm240':{},
              # 'wzp6_ee_eeH_Hgg_ecm240':{},
              # 'wzp6_ee_eeH_Hmumu_ecm240':{},
              # 'wzp6_ee_eeH_Hss_ecm240':{},
              # 'wzp6_ee_eeH_Htautau_ecm240':{},
              ## 'wzp6_ee_ee_Mee_30_150_ecm240':{},
              # 'p8_ee_ZZ_ecm240':{},#Run the full statistics in one output file named <outputDir>/p8_ee_ZZ_ecm240.root
              # 'p8_ee_WW_ecm240':{} #Run 50% of the statistics in two files named <outputDir>/p8_ee_WW_ecm240/chunk<N>.root
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

cutList = {"sel0":"Zcand_cos < 2", #aucun cut, 
           "sel1":"N_selected_leptons ==2",
           "sel2":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101",
           "sel3":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138",
           "sel4":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8",
           "sel5":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60",
           "sel6":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93",
           "sel7":"N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4",
           "sel8": "N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2",
           "sel9": "N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5",
           "sel10": "N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000",
           
           "sel11": "N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000 &&  dmerge_2_23 < 60 ",
           "sel12": "N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000 && dmerge_2_23 > 60 ",


           "sel13": "N_selected_leptons ==2 && Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 138 && meanNconst > 8 && secondZ_m < 100 && secondZ_m > 60 && abs(cos(missing_theta)) < 0.93 && min_angle_miss_jet > 0.4 && N_LooseLeptons_2 == 2 && emiss < 45 && emiss > 5 && dmerge_2_12 > 2000 && dmerge_2_23 > 60 && meanNconst_3 > 10 "

           
           #"sel9": "Zcand_m > 81 && Zcand_m < 101 && Zcand_recoil_m > 124 && Zcand_recoil_m < 140 && emiss > 5 && secondZ_m < 40 && secondZ_m > 65 && dmerge_2_12 > 10 && dmerge_2_23 < 100 && secondZ_p < 40"

           
           }

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    "mz":{"name":"Zcand_m","title":"Dilepton mass [GeV]","bin":125,"xmin":0,"xmax":200},
    "mz_zoom":{"name":"Zcand_m","title":"Dilepton mass (zoom) [GeV]","bin":40,"xmin":79,"xmax":103},
    "theta":{"name":"Zcand_theta","title":"#theta of the lepton pair ","bin":100,"xmin":-7,"xmax":7},
    "phi":{"name":"Zcand_phi","title":"#phi of the lepton pair","bin":100,"xmin":-7,"xmax":7},
    "cos":{"name":"Zcand_cos","title":"cos(#theta) of the lepton pair","bin":100,"xmin":-1,"xmax":1},
    "eta":{"name":"Zcand_eta","title":"Pseudo-rapidity #eta of the lepton pair","bin":100,"xmin":-10,"xmax":10},
    "y":{"name":"Zcand_y","title":"Rapidity y of the lepton pair","bin":100,"xmin":-5,"xmax":5},
    

    "leptonic_recoil_m":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass of the lepton pair [GeV]","bin":100,"xmin":0,"xmax":200},
    "leptonic_recoil_m_zoom":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":200,"xmin":80,"xmax":160},
    "leptonic_recoil_m_zoom1":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":100,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom2":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":200,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom3":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":400,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom4":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":800,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom5":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":2000,"xmin":120,"xmax":140},
    "leptonic_recoil_m_zoom6":{"name":"Zcand_recoil_m","title":"Leptonic recoil mass [GeV]","bin":100,"xmin":122,"xmax":125},

    "selected_muons_e":{"name":"selected_muons_e","title":"Energy of selected muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_e":{"name":"selected_electrons_e","title":"Energy of selected electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_e":{"name":"selected_leptons_e","title":"Energy of selected leptons [GeV]", "bin":100, "xmin":0, "xmax":200},


    "selected_muons_p":{"name":"selected_muons_p","title":"Momentum of selected muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_p":{"name":"selected_electrons_p","title":"Momentum of selected electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_p":{"name":"selected_leptons_p","title":"Momentum of selected leptons [GeV]", "bin":100, "xmin":0, "xmax":200},


    "selected_muons_px":{"name":"selected_muons_px","title":"px of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_px":{"name":"selected_electrons_px","title":"px of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_px":{"name":"selected_leptons_px","title":"px of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},


    "selected_muons_py":{"name":"selected_muons_py","title":"py of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_py":{"name":"selected_electrons_py","title":"py of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_py":{"name":"selected_leptons_py","title":"py of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},


    "selected_muons_pz":{"name":"selected_muons_pz","title":"pz of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pz":{"name":"selected_electrons_pz","title":"pz of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},
    "selected_leptons_pz":{"name":"selected_leptons_pz","title":"pz of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":-100, "xmax":100},

    "selected_muons_pt":{"name":"selected_muons_pt","title":"pt of selected (wrt momentum) muons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_electrons_pt":{"name":"selected_electrons_pt","title":"pt of selected (wrt momentum) electrons [GeV]", "bin":100, "xmin":0, "xmax":200},
    "selected_leptons_pt":{"name":"selected_leptons_pt","title":"pt of both selected (wrt momentum) muons and electrons [GeV]", "bin":100, "xmin":0, "xmax":200},

    "N_selected_leptons":{"name":"N_selected_leptons", "title":"Number of selected leptons", "bin":10, "xmin":0, "xmax":10}, 

    "N_zed_leptonic":{"name":"N_zed_leptonic", "title":"Number of reconstructed leptonic Z", "bin":10, "xmin":0, "xmax":10},

    "N_LooseLeptons":{"name":"N_LooseLeptons", "title":"Number of leptons with p>10GeV", "bin":20, "xmin":0, "xmax":20},
    "N_LooseLeptons_2":{"name":"N_LooseLeptons_2", "title":"Number of leptons with p>2GeV", "bin":20, "xmin":0, "xmax":20},
    "LooseLeptons_pt":{"name":"LooseLeptons_pt","title":"Transverse momentum of leptons with p>10GeV [GeV]", "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_p":{"name":"LooseLeptons_p","title":"Momentum of leptons with p>10GeV [GeV]", "bin":100, "xmin":0, "xmax":200},
    "LooseLeptons_theta":{"name":"LooseLeptons_theta","title":"#theta of leptons with p>10GeV [GeV]", "bin":100, "xmin":0, "xmax":4},
    "LooseLeptons_phi":{"name":"LooseLeptons_phi","title":"#phi of leptons with p>10GeV [GeV]", "bin":100, "xmin":-7, "xmax":7},




    "jet1_p":{"name":"jet1_p","title":"Momentum of the 1st jet from Durham kt N=2 [GeV]","bin":100,"xmin":0,"xmax":200},
    "jet2_p":{"name":"jet2_p", "title":"Momentum of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":200},    

    "jet1_px":{"name":"jet1_px","title":"px of the 1st jet from Durham kt N=2 [GeV]","bin":100,"xmin":-100,"xmax":100},
    "jet2_px":{"name":"jet2_px", "title":"px of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":-100, "xmax":100},
    
    "jet1_py":{"name":"jet1_py","title":"py of the 1st jet from Durham kt N=2 [GeV]","bin":100,"xmin":-100,"xmax":100},
    "jet2_py":{"name":"jet2_py", "title":"py of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":-100, "xmax":100},

    "jet1_pz":{"name":"jet1_pz","title":"pz of the 1st jet from Durham kt N=2 [GeV]","bin":100,"xmin":-100,"xmax":100},
    "jet2_pz":{"name":"jet2_pz", "title":"pz of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":-100, "xmax":100},

    "jet1_pt":{"name":"jet1_pt", "title":"pt of the 1st jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet2_pt":{"name":"jet2_pt", "title":"pt of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":200},
         
    "jet1_e":{"name":"jet1_e", "title":"Energy of the 1st jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":200},
    "jet2_e":{"name":"jet2_e", "title":"Energy of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":200},

    "jet1_theta":{"name":"jet1_theta", "title":"#theta of the 1st jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":4},
    "jet2_theta":{"name":"jet2_theta", "title":"#theta of the 2nd jet from Durham kt N=2 [GeV]", "bin":100, "xmin":0, "xmax":4},

    "jet1_Nconst":{"name":"jet1_Nconst", "title":"Number of constituents of the 1st jet from Durham kt N=2", "bin":70, "xmin":0, "xmax":70},
    "jet2_Nconst":{"name":"jet2_Nconst", "title":"Number of constituents of the 2nd jet from Durham kt N=2", "bin":70, "xmin":0, "xmax":70},

    "minNconst":{"name":"minNconst", "title":"Minimum number of constituents from Durham kt N=2", "bin":70, "xmin":0, "xmax":70},
    "maxNconst":{"name":"maxNconst", "title":"Maximum number of constituents from Durham kt N=2", "bin":70, "xmin":0, "xmax":70},
    "meanNconst":{"name":"meanNconst", "title":"Mean number of constituents from Durham kt N=2", "bin":70, "xmin":0, "xmax":70},
    

    "minNconst_3":{"name":"minNconst_3", "title":"Minimum number of constituents from Durham kt N=3", "bin":40, "xmin":0, "xmax":40},
    "maxNconst_3":{"name":"maxNconst_3", "title":"Maximum number of constituents from Durham kt N=3", "bin":40, "xmin":0, "xmax":40},
    "meanNconst_3":{"name":"meanNconst_3", "title":"Mean number of constituents from Durham kt N=3", "bin":40, "xmin":0, "xmax":40},

    
    
    "diffthetajets":{"name":"diffthetajets", "title":"Angular diff (theta) between the first and second jets", "bin" :100, "xmin":0, "xmax":4},

    "visible_mass_predef":{"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":0, "xmax":300},
    "visible_mass_predef_zoom":{"name":"visible_mass_predef", "title":"Visible Mass [GeV]", "bin":100, "xmin":200, "xmax":240},

    "secondZ_m":{"name":"secondZ_m", "title":"Dijet mass (Durham kt N=2)", "bin":100, "xmin":0, "xmax":200},
    "secondZ_m_zoom1":{"name":"secondZ_m", "title":"Dijet mass (Durham kt N=2)", "bin":100, "xmin":80, "xmax":120},
    "secondZ_m_zoom2":{"name":"secondZ_m", "title":"Dijet mass (Durham kt N=2)", "bin":100, "xmin":30, "xmax":70},
    "secondZ_m_centered":{"name":"secondZ_m", "title":"Dijet mass (Durham kt N=2)", "bin":100, "xmin":60, "xmax":100},
    "secondZ_m_centered_2":{"name":"secondZ_m", "title":"Dijet mass (Durham kt N=2)", "bin":20, "xmin":60, "xmax":100},

    "secondZ_p":{"name":"secondZ_p", "title":"Dijet momentum (Durham kt N=2)", "bin":100, "xmin":0, "xmax":200},
    "secondZ_px":{"name":"secondZ_px", "title":"Dijet px (Durham kt N=2)", "bin":100, "xmin":-100, "xmax":100},
    "secondZ_py":{"name":"secondZ_py", "title":"Dijet py (Durham kt N=2)", "bin":100, "xmin":-100, "xmax":100},
    "secondZ_pz":{"name":"secondZ_pz", "title":"Dijet pz (Durham kt N=2)", "bin":100, "xmin":-100, "xmax":100},
    "secondZ_pt":{"name":"secondZ_pt", "title":"Dijet transverse momentum (Durham kt N=2)", "bin":100, "xmin":0, "xmax":200},

    

    "dmerge_2_12":{"name":"dmerge_2_12","title":"dmerge_12","bin":125,"xmin":0,"xmax":12000},
    "dmerge_2_23":{"name":"dmerge_2_23","title":"dmerge_23","bin":125,"xmin":0,"xmax":1000},
    "dmerge_2_34":{"name":"dmerge_2_34","title":"dmerge_34","bin":125,"xmin":0,"xmax":700},
    "dmerge_2_45":{"name":"dmerge_2_45","title":"dmerge_45","bin":125,"xmin":0,"xmax":700},




    "emiss":{"name":"emiss", "title":"Missing energy [GeV]", "bin":100, "xmin":0, "xmax":100},
    "pxmiss":{"name":"pxmiss", "title":"Missing px [GeV]", "bin":100, "xmin":-80, "xmax":80},
    "pymiss":{"name":"pymiss", "title":"Missing py [GeV]", "bin":100, "xmin":-80, "xmax":80},
    "pzmiss":{"name":"pzmiss", "title":"Missing pz [GeV]", "bin":100, "xmin":-80, "xmax":80},
    "pzmiss_zoom":{"name":"pzmiss", "title":"Missing pz [GeV]", "bin":100, "xmin":0, "xmax":60},
    "etmiss":{"name":"etmiss", "title":"Missing transverse energy [GeV]", "bin":100, "xmin":0, "xmax":100},
    "etmiss_zoom":{"name":"etmiss", "title":"Missing transverse energy [GeV]", "bin":100, "xmin":0, "xmax":60},


    

    "missing_theta":{"name":"missing_theta", "title":"#theta extracted from the missing tlv", "bin":100, "xmin":0, "xmax":4},
    "angle_miss_jet1":{"name":"angle_miss_jet1", "title":"angular difference between missing tlv and jet1", "bin":100, "xmin":0, "xmax":4},
    "angle_miss_jet2":{"name":"angle_miss_jet2", "title":"angular difference between missing tlv and jet2", "bin":100, "xmin":0, "xmax":4},
    "min_angle_miss_jet":{"name":"min_angle_miss_jet","title":"Minimal angular difference between missing tlv and jets", "bin":100, "xmin":0, "xmax":4},
    "max_angle_miss_jet":{"name":"max_angle_miss_jet", "title":"Maximal angular difference between missing tlv and jets", "bin":100, "xmin":0, "xmax":4},

    
    
    



}

