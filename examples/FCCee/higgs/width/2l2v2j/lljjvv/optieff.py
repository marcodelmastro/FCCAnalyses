#!/usr/bin/env python

import ROOT

inputdir = 'outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/cutshisto/'
outdir = 'outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/plots/opti/'

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
               'wzp6_ee_nunuH_HZZ_ecm240',
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

var = ['leptonic_recoil_m'] #par exemple, mais osef
sels = ['sel0', 'sel1', 'sel2', 'sel3', 'sel4', 'sel5', 'sel6','sel7','sel8','sel9','sel10','sel11']


cuts = []
cut = 128
cuts.append(f"{cut}") 
for j in range (1,12):
    cut = cut + 1
    cuts.append(f"{cut}")

print(cuts)    


formats = ['png', 'pdf']

def main():
    sumssel0 = 0
    sumbsel0 = 0 
    n = len(sels)
    h = ROOT.TH1F("signaleff", "Signal and Background Efficiencies", n, 0, n)
    h2 = ROOT.TH1F("backgroundeff", "Signal and Background Efficiencies", n, 0, n)
    xax = h2.GetXaxis()
    for i in range(0,n): 
        sums = 0 
        sumb = 0 
        for s in signals:
                fs = ROOT.TFile.Open(f"{inputdir}{s}_sel{i}_histo.root")
                for vs in var:
                    hs = fs.Get(vs) 
                sums = sums + hs.Integral()
        if i == 0:
            sumssel0 = sums
        else :
            news = sums/sumssel0
            print(news)
            #print(sumssel0)
            #print(sums)
            h.SetBinContent(i,news)
                
        for b in backgrounds: 
                fb = ROOT.TFile.Open(f"{inputdir}{b}_sel{i}_histo.root")
                for vb in var: 
                    hb = fb.Get(vb) 
                sumb = sumb + hb.Integral()
        if i == 0:
            sumbsel0 = sumb
        else : 
            newb = sumb/sumbsel0
            print(newb)
            h2.SetBinContent(i,newb)
            xax.SetBinLabel(i,cuts[i-1])
                
      
        

    c = ROOT.TCanvas()
    h2.SetXTitle(f"Value of the cut on {var[0]}") 
    h2.Draw("hist")
    h.SetLineColor(2)
    h.Draw("hist same")
    for ext in formats:
        c.SaveAs(f"{outdir}{var[0]}_optiefficiency.{ext}")
    
    

    
       

if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)
    main()
