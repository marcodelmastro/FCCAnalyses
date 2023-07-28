import ROOT

inputDir = '/sps/atlas/combes/FCCAnalyses/outputs/fccee/higgs/mH-recoil/hzz/final/4jets/Zleptonique/woutfilter/'

outputDir = '/sps/atlas/combes/FCCAnalyses/outputs/fccee/higgs/mH-recoil/hzz/final/4jets/Zleptonique/woutfilter/'



samples = [#'wzp6_ee_mumuH_HZZ_ecm240',
           'wzp6_ee_eeH_HZZ_ecm240',
           'wzp6_ee_mumuH_HWW_ecm240',
           'wzp6_ee_eeH_HWW_ecm240',
           'wzp6_ee_mumuH_Hbb_ecm240',
           'wzp6_ee_eeH_Hbb_ecm240',   
           'wzp6_ee_mumuH_Hcc_ecm240',
           'wzp6_ee_eeH_Hcc_ecm240', 
           'wzp6_ee_mumuH_Hgg_ecm240',
           'wzp6_ee_eeH_Hgg_ecm240', 
           'wzp6_ee_mumuH_Htautau_ecm240',
           'wzp6_ee_eeH_Htautau_ecm240',
           'wzp6_ee_mumuH_Hmumu_ecm240',
           'wzp6_ee_eeH_Hmumu_ecm240',
           'wzp6_ee_mumuH_Hss_ecm240',
           'wzp6_ee_eeH_Hss_ecm240',
           'wzp6_ee_mumuH_Haa_ecm240',
           'wzp6_ee_eeH_Haa_ecm240',
           'wzp6_ee_mumuH_HZa_ecm240',
           'wzp6_ee_eeH_HZa_ecm240',
           'p8_ee_ZZ_ecm240',
           'p8_ee_WW_ecm240'
]

signals = [#'wzp6_ee_mumuH_HZZ_ecm240',
          'wzp6_ee_eeH_HZZ_ecm240']

samplesHWW = [#'wzp6_ee_mumuH_HWW_ecm240',
             'wzp6_ee_eeH_HWW_ecm240',
]

samplesHbb = [#'wzp6_ee_mumuH_Hbb_ecm240',
             'wzp6_ee_eeH_Hbb_ecm240',
]

samplesHtautau = [#'wzp6_ee_mumuH_Htautau_ecm240',
             'wzp6_ee_eeH_Htautau_ecm240',
]

samplesHgg =[#'wzp6_ee_mumuH_Hgg_ecm240',
           'wzp6_ee_eeH_Hgg_ecm240',
]

 

samplesHother = [#'wzp6_ee_mumuH_Hcc_ecm240',
           'wzp6_ee_eeH_Hcc_ecm240',
           'wzp6_ee_mumuH_Hmumu_ecm240',
           'wzp6_ee_eeH_Hmumu_ecm240',
           'wzp6_ee_mumuH_Hss_ecm240',
           'wzp6_ee_eeH_Hss_ecm240', 
           'wzp6_ee_mumuH_Haa_ecm240',
           'wzp6_ee_eeH_Haa_ecm240',
           'wzp6_ee_mumuH_HZa_ecm240',
           'wzp6_ee_eeH_HZa_ecm240',
]

sels = ['sel7','sel0']

var = 'firstZ_m'

def main(): 
    f = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel7_histo.root")
    g = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel0_histo.root")
    hf = f.Get('firstZ_m')
    hg = g.Get('firstZ_m')

   

    for s in signals : 
        f1 = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        g1 = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1 = f1.Get('firstZ_m')
        hg1 = g1.Get('firstZ_m')
        hf.Add(hf1, 1)
        hg.Add(hg1,1)

    hf = 5*10**(6)*hf
    hg = 5*10**(6)*hg

    filesignalsel7 = ROOT.TFile.Open(f"{outputDir}SumSignal_sel7_{var}.root", "RECREATE")
    filesignalsel7.WriteObject(hf, "firstZ_m")
    filesignalsel0 = ROOT.TFile.Open(f"{outputDir}SumSignal_sel0_{var}.root", "RECREATE")
    filesignalsel0.WriteObject(hg, "firstZ_m")


    fS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel7_histo.root")
    gS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel0_histo.root")
    hfS = fS.Get('firstZ_m')
    hgS = gS.Get('firstZ_m')


    for s in samples : 
        fSum = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        gSum = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hfSum = fSum.Get('firstZ_m')
        hgSum = gSum.Get('firstZ_m')
        hfS.Add(hfSum, 1)
        hgS.Add(hgSum, 1)

    hfS = 5*10**(6)*hfS
    hgS = 5*10**(6)*hgS

    filesumsel7 = ROOT.TFile.Open(f"{outputDir}Sum_sel7_{var}.root", "RECREATE")
    filesumsel7.WriteObject(hfS, "firstZ_m")
    filesumsel0 = ROOT.TFile.Open(f"{outputDir}Sum_sel0_{var}.root", "RECREATE")
    filesumsel0.WriteObject(hgS, "firstZ_m")


    fHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_sel7_histo.root")
    gHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_sel0_histo.root")
    hfHWW = fHWW.Get('firstZ_m')
    hgHWW = gHWW.Get('firstZ_m')
    for s in samplesHWW : 
        f1HWW = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        g1HWW = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1HWW = f1HWW.Get('firstZ_m')
        hg1HWW = g1HWW.Get('firstZ_m')
        hfHWW.Add(hf1HWW, 1)
        hgHWW.Add(hg1HWW,1)

    hfHWW = 5*10**(6)*hfHWW
    hgHWW = 5*10**(6)*hgHWW

    fileHWWsel7 = ROOT.TFile.Open(f"{outputDir}SumHWW_sel7_{var}.root", "RECREATE")
    fileHWWsel7.WriteObject(hfHWW, "firstZ_m")
    fileHWWsel0 = ROOT.TFile.Open(f"{outputDir}SumHWW_sel0_{var}.root", "RECREATE")
    fileHWWsel0.WriteObject(hgHWW, "firstZ_m")


    fHbb = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_sel7_histo.root")
    gHbb = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_sel0_histo.root")
    hfHbb = fHbb.Get('firstZ_m')
    hgHbb = gHbb.Get('firstZ_m')
    for s in samplesHbb : 
        f1Hbb = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        g1Hbb = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Hbb = f1Hbb.Get('firstZ_m')
        hg1Hbb = g1Hbb.Get('firstZ_m')
        hfHbb.Add(hf1Hbb, 1)
        hgHbb.Add(hg1Hbb,1)

    hfHbb= 5*10**(6)*hfHbb
    hgHbb = 5*10**(6)*hgHbb

    fileHbbsel7 = ROOT.TFile.Open(f"{outputDir}SumHbb_sel7_{var}.root", "RECREATE")
    fileHbbsel7.WriteObject(hfHbb, "firstZ_m")
    fileHbbsel0 = ROOT.TFile.Open(f"{outputDir}SumHbb_sel0_{var}.root", "RECREATE")
    fileHbbsel0.WriteObject(hgHbb, "firstZ_m")


    fHtt = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_sel7_histo.root")
    gHtt = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_sel0_histo.root")
    hfHtt = fHtt.Get('firstZ_m')
    hgHtt = gHtt.Get('firstZ_m')
    for s in samplesHtautau : 
        f1Htt = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        g1Htt = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Htt = f1Htt.Get('firstZ_m')
        hg1Htt = g1Htt.Get('firstZ_m')
        hfHtt.Add(hf1Htt, 1)
        hgHtt.Add(hg1Htt,1)

    hfHtt= 5*10**(6)*hfHtt  
    print("Htautau region 1 =", hfHtt.Integral())
    hgHtt = 5*10**(6)*hgHtt
    print("Htautau region 2 =", hgHtt.Integral())

    fileHttsel7 = ROOT.TFile.Open(f"{outputDir}SumHtautau_sel7_{var}.root", "RECREATE")
    fileHttsel7.WriteObject(hfHtt, "firstZ_m")
    fileHttsel0 = ROOT.TFile.Open(f"{outputDir}SumHtautau_sel0_{var}.root", "RECREATE")
    fileHttsel0.WriteObject(hgHtt, "firstZ_m")


    fHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_sel7_histo.root")
    gHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_sel0_histo.root")
    hfHgg = fHgg.Get('firstZ_m')
    hgHgg = gHgg.Get('firstZ_m')

    for s in samplesHgg : 
        f1Hgg = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        g1Hgg = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Hgg = f1Hgg.Get('firstZ_m')
        hg1Hgg = g1Hgg.Get('firstZ_m')
        hfHgg.Add(hf1Hgg, 1)
        hgHgg.Add(hg1Hgg,1)

    hfHgg= 5*10**(6)*hfHgg  
    print("Htautau region 1 =", hfHgg.Integral())
    hgHgg = 5*10**(6)*hgHgg
    print("Htautau region 2 =", hgHgg.Integral())

    fileHggsel7 = ROOT.TFile.Open(f"{outputDir}SumHgg_sel7_{var}.root", "RECREATE")
    fileHggsel7.WriteObject(hfHgg, "firstZ_m")
    fileHggsel0 = ROOT.TFile.Open(f"{outputDir}SumHgg_sel0_{var}.root", "RECREATE")
    fileHggsel0.WriteObject(hgHgg, "firstZ_m")


    fHo = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hcc_ecm240_sel7_histo.root")
    gHo = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hcc_ecm240_sel0_histo.root")
    hfHo = fHo.Get('firstZ_m')
    hgHo = gHo.Get('firstZ_m')

    for s in samplesHother : 
        f1Ho = ROOT.TFile.Open(f"{inputDir}{s}_sel7_histo.root")
        g1Ho = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Ho = f1Ho.Get('firstZ_m')
        hg1Ho = g1Ho.Get('firstZ_m')
        hfHo.Add(hf1Ho, 1)
        hgHo.Add(hg1Ho,1)

    hfHo= 5*10**(6)*hfHo 
    print("Htautau region 1 =", hfHo.Integral())
    hgHo = 5*10**(6)*hgHo
    print("Htautau region 2 =", hgHo.Integral())

    fileHosel7 = ROOT.TFile.Open(f"{outputDir}SumHother_sel7_{var}.root", "RECREATE")
    fileHosel7.WriteObject(hfHo, "firstZ_m")
    fileHosel0 = ROOT.TFile.Open(f"{outputDir}SumHother_sel0_{var}.root", "RECREATE")
    fileHosel0.WriteObject(hgHo, "firstZ_m")
    
    


    #myFile = ROOT.TFile.Open(f"{outputDir}SumHWW.root", "RECREATE")
    #myFile.WriteObject(h, "secondZ_m_38")

    #myFile = ROOT.TFile.Open(f"{outputDir}SumHbb.root", "RECREATE")
    #myFile.WriteObject(h, "secondZ_m_38")


    

    #myFile = ROOT.TFile.Open(f"{outputDir}WWnorm.root", "RECREATE")
    #myFile.WriteObject(h, "secondZ_m_38")

    #myFile = ROOT.TFile.Open(f"{outputDir}NunuHZZnorm.root", "RECREATE")
    #myFile.WriteObject(h, "secondZ_m_38")

      

    

    #myFile = ROOT.TFile.Open(f"{outputDir}SumwoutWW.root", "RECREATE")
    #myFile.WriteObject(h, "secondZ_m_38")


    
    
    z1 = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_sel7_histo.root")
    z2 = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_sel0_histo.root")
    hz1 = z1.Get('firstZ_m')
    hz2 = z2.Get('firstZ_m')
    hz1 = 5*10**(6)*hz1
    hz2 = 5*10**(6)*hz2
    fileZZsel7 = ROOT.TFile.Open(f"{outputDir}ZZnorm_sel7_{var}.root", "RECREATE")
    fileZZsel7.WriteObject(hz1, "firstZ_m")
    fileZZsel0 = ROOT.TFile.Open(f"{outputDir}ZZnorm_sel0_{var}.root", "RECREATE")
    fileZZsel0.WriteObject(hz2, "firstZ_m")


    w1 = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_sel7_histo.root")
    w2 = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_sel0_histo.root")
    hw1 = w1.Get('firstZ_m')
    hw2 = w2.Get('firstZ_m')
    hw1 = 5*10**(6)*hw1
    hw2 = 5*10**(6)*hw2
    fileWWsel7 = ROOT.TFile.Open(f"{outputDir}WWnorm_sel7_{var}.root", "RECREATE")
    fileWWsel7.WriteObject(hw1, "firstZ_m")
    fileWWsel0 = ROOT.TFile.Open(f"{outputDir}WWnorm_sel0_{var}.root", "RECREATE")
    fileWWsel0.WriteObject(hw2, "firstZ_m")

if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
