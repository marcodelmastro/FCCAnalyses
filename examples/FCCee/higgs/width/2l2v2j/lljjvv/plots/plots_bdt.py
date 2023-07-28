import ROOT

# global parameters
intLumi        =  5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = "ZH #rightarrow ZZZ #rightarrow #mu^{+}#mu^{-}/e^{+}e^{-} + jj #nu#nu"
delphesVersion = "3.4.2"
energy         =  240.0
collider       = "FCC-ee"
inputDir       = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/woutfilter_score_6classes_lljjvv/"
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['stack','nostack']
outdir         = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/plots/woutfilter_score_6classes_lljjvv/"

variables = ['HZZ','HWW','Hbb','Htautau','ZZ','WW','HZZ_centered','myScore_new','myScore_new_zoom']
#'Hcc','Hss', 'Hgg', 'Hmumu','HZa','Haa']

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['6classes']   = ["sel0","sel1","sel2","sel3","sel4","sel5"]
#,"sel2","sel3","sel4","sel5"]

#selections['WWplots'] = ["sel10","sel11"]

extralabel = {}
extralabel['sel0'] = "BDT 6 classes"
extralabel['sel1'] = "ZZ"
extralabel['sel2'] = "ZZ & WW"
extralabel['sel3'] = "ZZ & WW & HWW"
extralabel['sel4'] = "ZZ & WW & HWW & Htautau"
extralabel['sel5'] = "ZZ & WW & HWW & Htautau & Hbb"



colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['nunuH,HZZ'] = ROOT.kBlue
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
                 'backgrounds':{'nunuH,HZZ':['wzp6_ee_nunuH_HZZ_ecm240'],

                                   'WW':['p8_ee_WW_ecm240'],
                                   'ZZ':['p8_ee_ZZ_ecm240'], 

                                   'Htautau':['wzp6_ee_mumuH_Htautau_ecm240', 'wzp6_ee_eeH_Htautau_ecm240'],
                                   
                                   'HWW':['wzp6_ee_mumuH_HWW_ecm240', 'wzp6_ee_eeH_HWW_ecm240'],
                                   
                                   'Hbb':['wzp6_ee_mumuH_Hbb_ecm240', 'wzp6_ee_nunuH_Hbb_ecm240', 'wzp6_ee_eeH_Hbb_ecm240'],
                                   'Hgg':['wzp6_ee_mumuH_Hgg_ecm240', 'wzp6_ee_eeH_Hgg_ecm240'],
                                   
                                   'H->other decays':['wzp6_ee_mumuH_Hcc_ecm240', 'wzp6_ee_eeH_Hcc_ecm240', 'wzp6_ee_mumuH_Hmumu_ecm240', 'wzp6_ee_eeH_Hmumu_ecm240', 'wzp6_ee_mumuH_HZa_ecm240', 'wzp6_ee_nunuH_HZa_ecm240', 'wzp6_ee_eeH_HZa_ecm240', 'wzp6_ee_mumuH_Hss_ecm240', 'wzp6_ee_eeH_Hss_ecm240', 'wzp6_ee_mumuH_Haa_ecm240', 'wzp6_ee_eeH_Haa_ecm240']}
                 }
                        

              


legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['nunuH,HZZ'] = '#nu#nuH, HZZ'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['Htautau'] = 'H#rightarrow#tau#tau'
legend['HWW'] = 'H#rightarrowWW'
legend['Hbb'] = 'H#rightarrowbb'
legend['Hgg'] = 'H#rightarrowgg'
legend['H->other decays'] = 'H#rightarrowother'
#legend['Mee'] = 'Mee'
#legend['VV'] = 'VV boson'
