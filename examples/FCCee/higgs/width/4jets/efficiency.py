#!/usr/bin/env python

import ROOT

inputdir = '/scratch/combes/final/'
outdir = 'outputs/fccee/higgs/mH-recoil/hzz/plots/4jets/'

signals = ['wzp6_ee_mumuH_HZZ_ecm240',
           'wzp6_ee_eeH_HZZ_ecm240']
backgrounds = ['wzp6_ee_mumuH_HWW_ecm240',
               'wzp6_ee_mumuH_HZa_ecm240',
#               'wzp6_ee_mumuH_Haa_ecm240',
               'wzp6_ee_mumuH_Hbb_ecm240',
               'wzp6_ee_mumuH_Hcc_ecm240',
               'wzp6_ee_mumuH_Hgg_ecm240',
               'wzp6_ee_mumuH_Hmumu_ecm240',
               'wzp6_ee_mumuH_Hss_ecm240',
               'wzp6_ee_mumuH_Htautau_ecm240',
               'wzp6_ee_mumu_ecm240',
               'wzp6_ee_eeH_HWW_ecm240',
               'wzp6_ee_eeH_HZa_ecm240',
 #              'wzp6_ee_eeH_Haa_ecm240',
               'wzp6_ee_eeH_Hbb_ecm240',
               'wzp6_ee_eeH_Hcc_ecm240',
               'wzp6_ee_eeH_Hgg_ecm240',
               'wzp6_ee_eeH_Hmumu_ecm240',
               'wzp6_ee_eeH_Hss_ecm240',
               'wzp6_ee_eeH_Htautau_ecm240',
               'wzp6_ee_ee_Mee_30_150_ecm240',
               'p8_ee_ZZ_ecm240',
               'p8_ee_WW_ecm240']

var = ['mz'] #par exemple, mais osef
sels = ['sel0', 'sel1', 'sel2', 'sel3', 'sel4', 'sel5', 'sel6','sel7']



formats = ['png', 'pdf']

def main():
    sumssel0 = 0
    sumbsel0 = 0 
    n = len(sels)
    h = ROOT.TH1F("signaleff", "Signal and Background Efficiencies", n, 0, n)
    h2 = ROOT.TH1F("backgroundeff", "Signal and Background Efficiencies", n, 0, n)
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
            
        news = sums/sumssel0
        print(news)
        #print(sumssel0)
        #print(sums)
        h.SetBinContent(i+1,news)
                
        for b in backgrounds: 
                fb = ROOT.TFile.Open(f"{inputdir}{b}_sel{i}_histo.root")
                for vb in var: 
                    hb = fb.Get(vb) 
                sumb = sumb + hb.Integral()
        if i == 0:
            sumbsel0 = sumb

        newb = sumb/sumbsel0
        print(newb)
        h2.SetBinContent(i+1, newb)
                
      
        

    c = ROOT.TCanvas()
    h2.SetXTitle("Index of the selection") 
    h2.Draw("hist")
    h.SetLineColor(2)
    h.Draw("hist same")
    for ext in formats:
        c.SaveAs(f"{outdir}efficiency.{ext}")
    
    

    
       

if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)
    main()
