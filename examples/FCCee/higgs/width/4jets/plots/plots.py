import ROOT

# global parameters
intLumi        = 5.0e+06 #in pb-1
intLumiLabel   = "L = 5 ab^{-1}"
ana_tex        = 'ZH #rightarrow ZZZ #rightarrow #mu^{+}#mu^{-}/e^{+}e^{-} + jj jj'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
inputDir       = 'outputs/fccee/higgs/mH-recoil/hzz/final/4jets/Zleptonique/'
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['stack','nostack']
outdir         = 'outputs/fccee/higgs/mH-recoil/hzz/plots/4jets/allevents/'

variables = ['mz','mz_zoom', 'theta', 'phi', 'cos' ,'eta', 'y','leptonic_recoil_m','leptonic_recoil_m_zoom','leptonic_recoil_m_zoom2','leptonic_recoil_m_zoom6', 'selected_muons_e', 'selected_electrons_e', 'selected_leptons_e', 'selected_muons_p', 'selected_electrons_p' , 'selected_leptons_p', 'selected_muons_px', 'selected_electrons_px' , 'selected_leptons_px', 'selected_muons_py', 'selected_electrons_py' , 'selected_leptons_py', 'selected_muons_pz', 'selected_electrons_pz' , 'selected_leptons_pz', 'selected_muons_pt', 'selected_electrons_pt' , 'selected_leptons_pt', 'N_selected_leptons', 'N_zed_leptonic', 'jet1_p', 'jet2_p', 'jet3_p', 'jet4_p', 'jet1_pt', 'jet2_pt', 'jet3_pt', 'jet4_pt', 'jet1_e', 'jet2_e', 'jet3_e', 'jet4_e', 'jet1_2_m', 'jet2_2_m', 'dmerge_4_12','dmerge_4_12_shift', 'dmerge_4_23', 'dmerge_4_34', 'dmerge_4_34_zoom', 'dmerge_4_45', 'firstZ_m', 'firstZ_p', 'firstZ_pt', 'secondZ_m', 'secondZ_p', 'secondZ_pt','higgs_4_m', 'higgs_4_p','higgs_4_m_zoom', 'higgs_2_m', 'dmerge_2_12', 'dmerge_2_23', 'dmerge_2_34', 'dmerge_2_45']

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['H4jets']   = ["sel0","sel1","sel2","sel3", "sel4", "sel5", "sel6", "sel7","sel8"]
#, "sel11", "sel12"]

extralabel = {}
extralabel['sel0'] = "No cut"
extralabel['sel1'] = "Nb sel lept"
extralabel['sel2'] = "Nb sel lept + mll"
extralabel['sel3'] = "Nb sel lept + mll + recoil"
extralabel['sel4'] = "Nb sel lept + mll + recoil + etmiss"
extralabel['sel5'] = "Nb sel lept + mll + recoil + etmiss + pzmiss"
extralabel['sel6'] = "Nb sel lept + mll + recoil + etmiss + pzmiss + mzz"
extralabel['sel7'] = "Final selection"
extralabel['sel8'] = "Final selection, last cut on d23"
extralabel['sel9'] = "Nb sel lept + mll + recoil + etmiss + pzmiss + mzz + dm34 + dm23 + Nb const 4th jet"
#extralabel['sel13'] = "mll + recoil + etmiss + dmerge34 + mZZ + dmerge23 +pzmiss + nb of sel lept + MassZonshell + MassZoffshell + MomZonshell + MomZoffshell + Momjets"
#extralabel['sel14'] = "mll + recoil + etmiss + dmerge34 + mZZ + dmerge23 +pzmiss + nb of sel lept + MassZonshell + MassZoffshell + MomZonshell + MomZoffshell + Momjets + dmerge45"


#extralabel['sel7'] = "81 < mll < 101 GeV &|cos|<0.9 & 120 < m_recoil < 140 GeV & 100<mjj<150 & Emiss < 30GeV & |y|<1 & d34 >10"
#extralabel['sel8'] = "81 < mll < 101 GeV &|cos|<0.9 & 120 < m_recoil < 140 GeV & 100<mjj<150 & Emiss < 30GeV & |y|<1 & d34 >10 & Ej1 < 80 & 20<Ej2<60"
#extralabel['sel9'] = "81 < mll < 101 GeV &|cos|<0.9 & 120 < m_recoil < 140 GeV & 100<mjj<150 & Emiss < 30GeV & |y|<1 & d34 >10 & Ej1 < 80 & 20<Ej2<60 & 10<Ej3<40 "
#extralabel['sel10'] = "81 < mll < 101 GeV &|cos|<0.9 & 120 < m_recoil < 140 GeV & 100<mjj<150 & Emiss < 30GeV & |y|<1 & d34 >10 & Ej1 < 80 & 20<Ej2<60 & 10<Ej3<40 & flavourscoreZ1=2"
#extralabel['sel11'] = "sel finale"




colors = {}
colors['Signal,HZZ'] = ROOT.kRed
colors['WW'] = ROOT.kOrange+6
colors['ZZ'] = ROOT.kOrange-2
colors['HWW'] = ROOT.kGreen
colors['Hbb'] = ROOT.kPink-9
colors['Hcc'] = ROOT.kCyan+2
colors['Hgg'] = ROOT.kBlue
colors['H->other decays'] = ROOT.kViolet

#colors['VV'] = ROOT.kGreen+3

plots = {}
plots['H4jets'] = {'signal': {'Signal,HZZ':['wzp6_ee_mumuH_HZZ_ecm240', 'wzp6_ee_eeH_HZZ_ecm240']},
                   'backgrounds' :{'HWW':['wzp6_ee_mumuH_HWW_ecm240', 'wzp6_ee_eeH_HWW_ecm240'],
                                   'Hbb':['wzp6_ee_mumuH_Hbb_ecm240', 'wzp6_ee_eeH_Hbb_ecm240'],
                                   'Hcc':['wzp6_ee_mumuH_Hcc_ecm240', 'wzp6_ee_eeH_Hcc_ecm240'],
                                   'Hgg':['wzp6_ee_mumuH_Hgg_ecm240', 'wzp6_ee_eeH_Hgg_ecm240'],
                                   

                                   'H->other decays':['wzp6_ee_mumuH_HZa_ecm240', 'wzp6_ee_eeH_HZa_ecm240', 'wzp6_ee_mumuH_Hss_ecm240', 'wzp6_ee_eeH_Hss_ecm240', 'wzp6_ee_mumuH_Haa_ecm240', 'wzp6_ee_eeH_Haa_ecm240', 'wzp6_ee_mumuH_Htautau_ecm240','wzp6_ee_eeH_Htautau_ecm240', 'wzp6_ee_mumuH_Hmumu_ecm240', 'wzp6_ee_eeH_Hmumu_ecm240'],
#                                   #'mumuH-Hss':['wzp6_ee_mumuH_Hss_ecm240'],
#                                   #'eeH-Hss':['wzp6_ee_eeH_Hss_ecm240'],
#                                   #'mumuH-Htautau':['wzp6_ee_mumuH_Htautau_ecm240'],
#                                   #'eeH-Htautau':['wzp6_ee_eeH_Htautau_ecm240'],
                                    'WW':['p8_ee_WW_ecm240'],
                                    'ZZ':['p8_ee_ZZ_ecm240']}}
#                                   #'mumu':['wzp6_ee_mumu_ecm240'],
#                                   #'Mee':['wzp6_ee_ee_Mee_30_150_ecm240']}}
#


#plots['H4jetsbckg'] = {'signal':{'mumuH-HZZ':['wzp6_ee_mumuH_HZZ_ecm240'],
#                         'eeH-HZZ':['wzp6_ee_eeH_HZZ_ecm240']},
#                         
#                   'backgrounds':{'mumuH-HWW':['wzp6_ee_mumuH_HWW_ecm240'],
#                                  'eeH-HWW':['wzp6_ee_eeH_HWW_ecm240'],
#                                  'mumuH-Haa':['wzp6_ee_mumuH_Haa_ecm240'],
 ##                                 'eeH-Haa':['wzp6_ee_eeH_Haa_ecm240'],
  #                                'mumuH-HZa':['wzp6_ee_mumuH_HZa_ecm240'],
  ##                                'eeH-HZa':['wzp6_ee_eeH_HZa_ecm240'],
   ##                               'mumuH-Hbb':['wzp6_ee_mumuH_Hbb_ecm240'],
    ##                              'eeH-Hbb':['wzp6_ee_eeH_Hbb_ecm240'],
    #                              'mumuH-Hcc':['wzp6_ee_mumuH_Hcc_ecm240'],
     ##                             'eeH-Hcc':['wzp6_ee_eeH_Hcc_ecm240'],
      ##                            'mumuH-Hgg':['wzp6_ee_mumuH_Hgg_ecm240'],
       ##                           'eeH-Hgg':['wzp6_ee_eeH_Hgg_ecm240'],
        ##                          'mumuH-Hmumu':['wzp6_ee_mumuH_Hmumu_ecm240'],
         ##                         'eeH-Hmumu':['wzp6_ee_eeH_Hmumu_ecm240'],
          ##                        'mumuH-Hss':['wzp6_ee_mumuH_Hss_ecm240'],
           ##                       'eeH-Hss':['wzp6_ee_eeH_Hss_ecm240'],
            ##                      'mumuH-Htautau':['wzp6_ee_mumuH_Htautau_ecm240'],
             ##                     'eeH-Htautau':['wzp6_ee_eeH_Htautau_ecm240'],
              #                    'WW':['p8_ee_WW_ecm240'],
               #                   'ZZ':['p8_ee_ZZ_ecm240'],
               #                   'mumu':['wzp6_ee_mumu_ecm240'],
                #                  'Mee':['wzp6_ee_ee_Mee_30_150_ecm240']}}
                 #'WW':['p8_ee_WW_ecm240'],
                             # 'ZZ':['p8_ee_ZZ_ecm240'],
                             # 'mumu':['wzp6_ee_mumu_ecm240']}
              

#plots['HZZ']= {'signal':{'mumuH-HZZ':['wzp6_ee_mumuH_HZZ_ecm240']},
#              'backgrounds':{}
#              }


#plots['ZH_2'] = {'signal':{'ZH':['MySample_p8_ee_ZH_ecm240']},
#                 'backgrounds':{'VV':['p8_ee_WW_ecm240','p8_ee_ZZ_ecm240']}
#             }



legend = {}
legend['Signal,HZZ'] = 'Signal'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['HWW'] = 'H#rightarrowWW'
legend['Hbb'] = 'H#rightarrowbb'
legend['Hcc'] = 'H#rightarrowcc'
legend['Hgg'] = 'H#rightarrowgg'

legend['H->other decays'] = 'H#rightarrowother'
