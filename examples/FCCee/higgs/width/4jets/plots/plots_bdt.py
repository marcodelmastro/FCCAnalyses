import ROOT

# global parameters
intLumi        =  5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = "ZH #rightarrow ZZZ #rightarrow #mu^{+}#mu^{-}/e^{+}e^{-} + jj jj"
delphesVersion = "3.4.2"
energy         =  240.0
collider       = "FCC-ee"
inputDir       = "/sps/atlas/combes/FCCAnalyses/outputs/fccee/higgs/mH-recoil/hzz/final/4jets/Zleptonique/bdt_score_test1_4jets/"
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['stack','nostack']
outdir         = "/sps/atlas/combes/FCCAnalyses/outputs/fccee/higgs/mH-recoil/hzz/plots/4jets/bdt_score_test1_4jets/"

variables = ['HZZ','HWW','Hbb','ZZ','WW','HZZ_centered','myScore_new','myScore_new_zoom','mz', 'N_selected_leptons', 'leptonic_recoil_m', 'jet1_e','jet2_e','jet3_e','jet4_e', 'firstZ_m','firstZ_p', 'secondZ_m', 'secondZ_p', 'higgs_4_m','higgs_4_p','higgs_2_m', 'pzmiss','emiss','etmiss', 'mintheta','firstZ_m_antikt_ter','secondZ_m_antikt_ter','firstZ_m_antikt_1_2_ter','firstZ_m_antikt_reco_ter', 'firstZ_m_antikt_bis','secondZ_m_antikt_bis','firstZ_m_antikt_1_2_bis','firstZ_m_antikt_reco_bis','N_jets_antikt4_bis', 'N_jets_antikt4_Ab5_bis', 'N_jets_antikt4_ter', 'N_jets_antikt4_Ab5_ter', 'dmerge_2_34', 'dmerge_2_45','dmerge_2_23', 'jet1_theta', 'jet2_theta', 'jet3_theta', 'jet4_theta', 'N_LooseLeptons_2', 'N_LooseLeptons_1', 'angle_2_jet1_jet2', 'angle_jet1_jet2', 'angle_jet1_jet3', 'angle_jet1_jet4', 'angle_jet2_jet3', 'angle_jet2_jet4', 'angle_jet3_jet4', 'angle_Z1_Z2'  ]
#'Hcc','Hss', 'Hgg', 'Hmumu','HZa','Haa']

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['6classes']   = ["sel0","sel1","sel2","sel3"]
#,"sel2","sel3","sel4","sel5"]

#selections['WWplots'] = ["sel10","sel11"]

extralabel = {}
extralabel['sel0'] = "BDT 4jets"
extralabel['sel1'] = "myScore > 9"
extralabel['sel2'] = "myScore > 9.5"
extralabel['sel3'] = "myScore > 10"
extralabel['sel4'] = "ZZ & WW & HWW & Htautau"
extralabel['sel5'] = "ZZ & WW & HWW & Htautau & Hbb"



colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['llH,HZZ'] = ROOT.kBlue
colors['WW'] = ROOT.kOrange+6
colors['ZZ'] = ROOT.kOrange-2
colors['Htautau'] = ROOT.kCyan+2
colors['HWW'] = ROOT.kGreen
colors['Hbb'] = ROOT.kPink-9
colors['Hgg'] = ROOT.kOrange+3
colors['H->other decays'] = ROOT.kViolet

#colors['VV'] = ROOT.kGreen+3

plots = {}


#plots['WWplots'] = {'signal':{'WW':['p8_ee_WW_ecm240']},
#               'backgrounds':{}}
                            
                                   
                                   
plots['6classes'] = {'signal':{'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240','wzp6_ee_eeH_HZZ_ecm240']},
                 'backgrounds':{'WW':['p8_ee_WW_ecm240'],
                                'ZZ':['p8_ee_ZZ_ecm240'], 

                                'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 'wzp6_ee_eeH_Htautau_ecm240'],
                                   
                                'HWW':['wzp6_ee_mumuH_HWW_ecm240', 'wzp6_ee_eeH_HWW_ecm240'],
                                   
                                'Hbb':['wzp6_ee_mumuH_Hbb_ecm240', 'wzp6_ee_eeH_Hbb_ecm240'],
                                   'Hgg':['wzp6_ee_mumuH_Hgg_ecm240', 'wzp6_ee_eeH_Hgg_ecm240'],
                                   
                                   'H->other decays':['wzp6_ee_mumuH_Hcc_ecm240', 'wzp6_ee_eeH_Hcc_ecm240', 'wzp6_ee_mumuH_Hmumu_ecm240', 'wzp6_ee_eeH_Hmumu_ecm240', 'wzp6_ee_mumuH_HZa_ecm240', 'wzp6_ee_eeH_HZa_ecm240', 'wzp6_ee_mumuH_Hss_ecm240', 'wzp6_ee_eeH_Hss_ecm240', 'wzp6_ee_mumuH_Haa_ecm240', 'wzp6_ee_eeH_Haa_ecm240']}
                 }
                        

              


legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['llH,HZZ'] = 'l^{+}l^{-}H, HZZ'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['Htautau'] = 'H#rightarrow#tau#tau'
legend['HWW'] = 'H#rightarrowWW'
legend['Hbb'] = 'H#rightarrowbb'
legend['Hgg'] = 'H#rightarrowgg'
legend['H->other decays'] = 'H#rightarrowother'
#legend['Mee'] = 'Mee'
#legend['VV'] = 'VV boson'
