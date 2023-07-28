import ROOT

inputDir = 'outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/woutfilter_score_6classes_lljjvv/'

outputDir = 'outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/final/woutfilter_score_6classes_lljjvv/' 




samples = [#'wzp6_ee_mumuH_HZZ_ecm240',
           'wzp6_ee_eeH_HZZ_ecm240',
           'wzp6_ee_nunuH_HZZ_ecm240',
           'wzp6_ee_mumuH_HWW_ecm240',
           'wzp6_ee_eeH_HWW_ecm240',
#           'wzp6_ee_nunuH_HWW_ecm240',
           'wzp6_ee_mumuH_Hbb_ecm240',
           'wzp6_ee_eeH_Hbb_ecm240',   
           'wzp6_ee_nunuH_Hbb_ecm240',
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
           'wzp6_ee_nunuH_HZa_ecm240',
           'p8_ee_ZZ_ecm240',
           'p8_ee_WW_ecm240'
]

signals = [#'wzp6_ee_mumuH_HZZ_ecm240',
          'wzp6_ee_eeH_HZZ_ecm240',
          'wzp6_ee_nunuH_HZZ_ecm240']

samplesHWW = [#'wzp6_ee_mumuH_HWW_ecm240',
             'wzp6_ee_eeH_HWW_ecm240',
             #'wzp6_ee_nunuH_HWW_ecm240'
]

samplesHbb = [#'wzp6_ee_mumuH_Hbb_ecm240',
             'wzp6_ee_eeH_Hbb_ecm240',
             'wzp6_ee_nunuH_Hbb_ecm240'
]

samplesHtautau = [#'wzp6_ee_mumuH_Htautau_ecm240',
             'wzp6_ee_eeH_Htautau_ecm240',
             #'wzp6_ee_nunuH_Htautau_ecm240'
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
           'wzp6_ee_nunuH_HZa_ecm240',
           
]

sels = ['sel5','sel0']

#var = 'HZZ'
var = 'myScore_new_zoom'

def main(): 
    f = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel5_histo.root")
    g = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel0_histo.root")
    hf = f.Get('myScore_new_zoom')
    hg = g.Get('myScore_new_zoom')

   

    for s in signals : 
        f1 = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        g1 = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1 = f1.Get('myScore_new_zoom')
        hg1 = g1.Get('myScore_new_zoom')
        hf.Add(hf1, 1)
        hg.Add(hg1,1)

    hf = 5*10**(6)*hf
    print("signal region 1 =", hf.Integral())
    hg = 5*10**(6)*hg
    print("signal region 2 =", hg.Integral())
    filesignalsel5 = ROOT.TFile.Open(f"{outputDir}SumSignal_sel5_{var}.root", "RECREATE")
    filesignalsel5.WriteObject(hf, "myScore_new_zoom")
    filesignalsel0 = ROOT.TFile.Open(f"{outputDir}SumSignal_sel0_{var}.root", "RECREATE")
    filesignalsel0.WriteObject(hg, "myScore_new_zoom")


    fS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel5_histo.root")
    gS = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HZZ_ecm240_sel0_histo.root")
    hfS = fS.Get('myScore_new_zoom')
    hgS = gS.Get('myScore_new_zoom')


    for s in samples : 
        fSum = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        gSum = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hfSum = fSum.Get('myScore_new_zoom')
        hgSum = gSum.Get('myScore_new_zoom')
        hfS.Add(hfSum, 1)
        hgS.Add(hgSum, 1)

    hfS = 5*10**(6)*hfS
    print("sum without WW region 1  =", hfS.Integral())
    hgS = 5*10**(6)*hgS
    print("sum withtout WW region 2 =", hgS.Integral()) 


    filesumsel5 = ROOT.TFile.Open(f"{outputDir}Sum_sel5_{var}.root", "RECREATE")
    filesumsel5.WriteObject(hfS, "myScore_new_zoom")
    filesumsel0 = ROOT.TFile.Open(f"{outputDir}Sum_sel0_{var}.root", "RECREATE")
    filesumsel0.WriteObject(hgS, "myScore_new_zoom")


    fHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_sel5_histo.root")
    gHWW = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_HWW_ecm240_sel0_histo.root")
    hfHWW = fHWW.Get('myScore_new_zoom')
    hgHWW = gHWW.Get('myScore_new_zoom')
    for s in samplesHWW : 
        f1HWW = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        g1HWW = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1HWW = f1HWW.Get('myScore_new_zoom')
        hg1HWW = g1HWW.Get('myScore_new_zoom')
        hfHWW.Add(hf1HWW, 1)
        hgHWW.Add(hg1HWW,1)

    hfHWW = 5*10**(6)*hfHWW
    print("HWW region 1 =", hfHWW.Integral())
    hgHWW = 5*10**(6)*hgHWW
    print("HWW region 2 =", hgHWW.Integral())
 
    fileHWWsel5 = ROOT.TFile.Open(f"{outputDir}SumHWW_sel5_{var}.root", "RECREATE")
    fileHWWsel5.WriteObject(hfHWW, "myScore_new_zoom")
    fileHWWsel0 = ROOT.TFile.Open(f"{outputDir}SumHWW_sel0_{var}.root", "RECREATE")
    fileHWWsel0.WriteObject(hgHWW, "myScore_new_zoom")


    fHbb = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_sel5_histo.root")
    gHbb = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hbb_ecm240_sel0_histo.root")
    hfHbb = fHbb.Get('myScore_new_zoom')
    hgHbb = gHbb.Get('myScore_new_zoom')
    for s in samplesHbb : 
        f1Hbb = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        g1Hbb = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Hbb = f1Hbb.Get('myScore_new_zoom')
        hg1Hbb = g1Hbb.Get('myScore_new_zoom')
        hfHbb.Add(hf1Hbb, 1)
        hgHbb.Add(hg1Hbb,1)

    hfHbb= 5*10**(6)*hfHbb  
    print("Hbb region 1 =", hfHbb.Integral())
    hgHbb = 5*10**(6)*hgHbb
    print("Hbb region 2 =", hgHbb.Integral())

    fileHbbsel5 = ROOT.TFile.Open(f"{outputDir}SumHbb_sel5_{var}.root", "RECREATE")
    fileHbbsel5.WriteObject(hfHbb, "myScore_new_zoom")
    fileHbbsel0 = ROOT.TFile.Open(f"{outputDir}SumHbb_sel0_{var}.root", "RECREATE")
    fileHbbsel0.WriteObject(hgHbb, "myScore_new_zoom")


    fHtt = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_sel5_histo.root")
    gHtt = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Htautau_ecm240_sel0_histo.root")
    hfHtt = fHtt.Get('myScore_new_zoom')
    hgHtt = gHtt.Get('myScore_new_zoom')
    for s in samplesHtautau : 
        f1Htt = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        g1Htt = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Htt = f1Htt.Get('myScore_new_zoom')
        hg1Htt = g1Htt.Get('myScore_new_zoom')
        hfHtt.Add(hf1Htt, 1)
        hgHtt.Add(hg1Htt,1)

    hfHtt= 5*10**(6)*hfHtt  
    print("Htautau region 1 =", hfHtt.Integral())
    hgHtt = 5*10**(6)*hgHtt
    print("Htautau region 2 =", hgHtt.Integral())

    fileHttsel5 = ROOT.TFile.Open(f"{outputDir}SumHtautau_sel5_{var}.root", "RECREATE")
    fileHttsel5.WriteObject(hfHtt, "myScore_new_zoom")
    fileHttsel0 = ROOT.TFile.Open(f"{outputDir}SumHtautau_sel0_{var}.root", "RECREATE")
    fileHttsel0.WriteObject(hgHtt, "myScore_new_zoom")


    fHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_sel5_histo.root")
    gHgg = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hgg_ecm240_sel0_histo.root")
    hfHgg = fHgg.Get('myScore_new_zoom')
    hgHgg = gHgg.Get('myScore_new_zoom')
    for s in samplesHgg : 
        f1Hgg = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        g1Hgg = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Hgg = f1Hgg.Get('myScore_new_zoom')
        hg1Hgg = g1Hgg.Get('myScore_new_zoom')
        hfHgg.Add(hf1Hgg, 1)
        hgHgg.Add(hg1Hgg,1)

    hfHgg= 5*10**(6)*hfHgg  
    print("Htautau region 1 =", hfHgg.Integral())
    hgHgg = 5*10**(6)*hgHgg
    print("Htautau region 2 =", hgHgg.Integral())

    fileHggsel5 = ROOT.TFile.Open(f"{outputDir}SumHgg_sel5_{var}.root", "RECREATE")
    fileHggsel5.WriteObject(hfHgg, "myScore_new_zoom")
    fileHggsel0 = ROOT.TFile.Open(f"{outputDir}SumHgg_sel0_{var}.root", "RECREATE")
    fileHggsel0.WriteObject(hgHgg, "myScore_new_zoom")


    fHo = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hcc_ecm240_sel5_histo.root")
    gHo = ROOT.TFile.Open(f"{inputDir}wzp6_ee_mumuH_Hcc_ecm240_sel0_histo.root")
    hfHo = fHo.Get('myScore_new_zoom')
    hgHo = gHo.Get('myScore_new_zoom')
    for s in samplesHother : 
        f1Ho = ROOT.TFile.Open(f"{inputDir}{s}_sel5_histo.root")
        g1Ho = ROOT.TFile.Open(f"{inputDir}{s}_sel0_histo.root")
        hf1Ho = f1Ho.Get('myScore_new_zoom')
        hg1Ho = g1Ho.Get('myScore_new_zoom')
        hfHo.Add(hf1Ho, 1)
        hgHo.Add(hg1Ho,1)

    hfHo= 5*10**(6)*hfHo 
    print("Htautau region 1 =", hfHo.Integral())
    hgHo = 5*10**(6)*hgHo
    print("Htautau region 2 =", hgHo.Integral())

    fileHosel5 = ROOT.TFile.Open(f"{outputDir}SumHother_sel5_{var}.root", "RECREATE")
    fileHosel5.WriteObject(hfHo, "myScore_new_zoom")
    fileHosel0 = ROOT.TFile.Open(f"{outputDir}SumHother_sel0_{var}.root", "RECREATE")
    fileHosel0.WriteObject(hgHo, "myScore_new_zoom")
    


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


    
    
    z1 = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_sel5_histo.root")
    z2 = ROOT.TFile.Open(f"{inputDir}p8_ee_ZZ_ecm240_sel0_histo.root")
    hz1 = z1.Get('myScore_new_zoom')
    hz2 = z2.Get('myScore_new_zoom')
    hz1 = 5*10**(6)*hz1
    print("ZZ region 1=", hz1.Integral())
    hz2 = 5*10**(6)*hz2
    print("ZZ region 2=", hz2.Integral())
    fileZZsel5 = ROOT.TFile.Open(f"{outputDir}ZZnorm_sel5_{var}.root", "RECREATE")
    fileZZsel5.WriteObject(hz1, "myScore_new_zoom")
    fileZZsel0 = ROOT.TFile.Open(f"{outputDir}ZZnorm_sel0_{var}.root", "RECREATE")
    fileZZsel0.WriteObject(hz2, "myScore_new_zoom")

    w1 = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_sel5_histo.root")
    w2 = ROOT.TFile.Open(f"{inputDir}p8_ee_WW_ecm240_sel0_histo.root")
    hw1 = w1.Get('myScore_new_zoom')
    hw2 = w2.Get('myScore_new_zoom')
    hw1 = 5*10**(6)*hw1
    hw2 = 5*10**(6)*hw2
    fileWWsel8 = ROOT.TFile.Open(f"{outputDir}WWnorm_sel5_{var}.root", "RECREATE")
    fileWWsel8.WriteObject(hw1, "myScore_new_zoom")
    fileWWsel7 = ROOT.TFile.Open(f"{outputDir}WWnorm_sel0_{var}.root", "RECREATE")
    fileWWsel7.WriteObject(hw2, "myScore_new_zoom")


   


if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
