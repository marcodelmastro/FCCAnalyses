#!/usr/bin/env python

import ROOT

inputdir = 'outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/'
outdir = 'outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/plots/'

signals = ['wzp6_ee_mumuH_HZZ_ecm240',
           'wzp6_ee_eeH_HZZ_ecm240']
backgrounds = ['wzp6_ee_mumuH_HWW_ecm240',
               'wzp6_ee_mumuH_HZa_ecm240',
               'wzp6_ee_mumuH_Haa_ecm240',
               'wzp6_ee_mumuH_Hbb_ecm240',
               'wzp6_ee_mumuH_Hcc_ecm240',
               'wzp6_ee_mumuH_Hgg_ecm240',
               'wzp6_ee_mumuH_Hmumu_ecm240',
               'wzp6_ee_mumuH_Hss_ecm240',
               'wzp6_ee_mumuH_Htautau_ecm240',
#               'wzp6_ee_nunuH_HZZ_ecm240',
               'wzp6_ee_nunuH_HWW_ecm240',
               'wzp6_ee_nunuH_HZa_ecm240',
               'wzp6_ee_nunuH_Hbb_ecm240',
               'wzp6_ee_nunuH_Hcc_ecm240',
               'wzp6_ee_nunuH_Hgg_ecm240',
               'wzp6_ee_nunuH_Hmumu_ecm240',
               'wzp6_ee_nunuH_Hss_ecm240',
               'wzp6_ee_nunuH_Htautau_ecm240',
               #'wzp6_ee_mumu_ecm240',
               'wzp6_ee_eeH_HWW_ecm240',
               'wzp6_ee_eeH_HZa_ecm240',
               'wzp6_ee_eeH_Haa_ecm240',
               'wzp6_ee_eeH_Hbb_ecm240',
               'wzp6_ee_eeH_Hcc_ecm240',
               'wzp6_ee_eeH_Hgg_ecm240',
               'wzp6_ee_eeH_Hmumu_ecm240',
               'wzp6_ee_eeH_Hss_ecm240',
               'wzp6_ee_eeH_Htautau_ecm240',
               #'wzp6_ee_ee_Mee_30_150_ecm240',
               'p8_ee_ZZ_ecm240',
               'p8_ee_WW_ecm240']

var = ['mz'] #par exemple, mais osef
sels = ['sel0', 
        'sel1', 
        'sel2', 
        'sel3', 
        'sel4', 
        'sel5', 
        'sel6',
        'sel7',
        'sel8',
        'sel9',
        'sel10',
        'sel11'
       # 'sel12',
       # 'sel13',
       # 'sel14'
        ]


formats = ['png', 'pdf']

def main():
    n = len(sels)
    h = ROOT.TH1F("soverb", "S/B for Region 1", n+1, 0, n+1)
    for i in range(0,n): 
        sums = 0 
        sumb = 0 
        for s in signals:
                fs = ROOT.TFile.Open(f"{inputdir}{s}_sel{i}_histo.root")
                for vs in var:
                    hs = fs.Get(vs) 
                sums = sums + hs.Integral()
                #print(sums*5*10**(6))
                
        for b in backgrounds: 
                fb = ROOT.TFile.Open(f"{inputdir}{b}_sel{i}_histo.root")
                for vb in var: 
                    hb = fb.Get(vb) 
                sumb = sumb + hb.Integral()
                
      
        final = sums/sumb 
        h.SetBinContent(i+1, final) 

    c = ROOT.TCanvas()
    h.SetXTitle("Index of the selection") 
    c.SetLogy()
    h.Draw("hist")
    for ext in formats:
        c.SaveAs(f"{outdir}soverb.{ext}")
    
    

    print(final)    
       

if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)
    main()
