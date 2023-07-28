inputDir    = "outputs/fccee/higgs/mH-recoil/neutrinos/stage1/smear_sf_2_5/"

#Optional: output directory, default is local dir
outputDir   = "outputs/fccee/higgs/mH-recoil/neutrinos/lljjvv/stage2/smear_sf_2_5/"

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
              #  #'wzp6_ee_mumu_ecm240':{},
              # 'wzp6_ee_nunuH_HZZ_ecm240':{},
              # 'wzp6_ee_nunuH_HWW_ecm240':{},
              # 'wzp6_ee_nunuH_HZa_ecm240':{},
              # 'wzp6_ee_nunuH_Haa_ecm240':{},
              # 'wzp6_ee_nunuH_Hbb_ecm240':{},
              # 'wzp6_ee_nunuH_Hcc_ecm240':{},
              # 'wzp6_ee_nunuH_Hgg_ecm240':{},
              # 'wzp6_ee_nunuH_Hmumu_ecm240':{},
              # 'wzp6_ee_nunuH_Hss_ecm240':{},
              # 'wzp6_ee_nunuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HZZ_ecm240':{}
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


#Optional: ncpus, default is 4
nCPUS       = 64 

#Optional running on HTCondor, default is False
#runBatch    = False

#USER DEFINED CODE
import ROOT
ROOT.gInterpreter.Declare("""
bool myFilter(ROOT::VecOps::RVec<float> mass) {
    for (size_t i = 0; i < mass.size(); ++i) {
        if (mass.at(i)>80. && mass.at(i)<100.)
            return true;
    }
    return false;
}
""")
#END USER DEFINED CODE

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (df
               #pour tourner que sur du signal donc sur du hzz
               #.Filter("hzz_decay.Z_decay.size()>0")

               #on stocke la valeur ABSOLUE du pdg de Z ; attention, pdg_Z stocke 2 variables donc il faut en choisir une avant d'appliquer le filtre, en l'occurence pour hzz truth les deux valeurs sont juste de signe opposé donc on prend la valeur absolue et voilà
               #.Define("abs_pdg_Z", "abs(MCParticle::get_pdg(hzz_decay.Z_decay)[0])")
               #on applique le filtre pour avoir un decay du Z seul en leptons (électrons ou muons)
               #.Filter("abs_pdg_Z == 11 || abs_pdg_Z == 13")
               
               #même chose mais maintenant pour les deux Z du Higgs 

               #on veut le Z on shell en deux neutrinos électroniques ou muoniques ou tau neutrinos?
               #.Define("abs_pdg_Z1", "abs(MCParticle::get_pdg(hzz_decay.Z1_decay)[0])")
               #.Filter("abs_pdg_Z1 == 1 || abs_pdg_Z1 == 2 || abs_pdg_Z1 == 3 || abs_pdg_Z1 == 4 || abs_pdg_Z1 == 5")
               #
	       #.Define("abs_pdg_Z2", "abs(MCParticle::get_pdg(hzz_decay.Z2_decay)[0])")
               #.Filter("abs_pdg_Z2 == 12 || abs_pdg_Z2 == 14 || abs_pdg_Z2 == 16") 
               
#maintenant, on est plus que sur des évènements où le Z seul est en leptons et le higgs en deux Z eux meme en 2 jets (4jets)

               .Filter("size(jets_e2)>0") 
               #Filter to have exactly one Z candidate for the reconstructed particles
               .Filter("zed_leptonic_m.size() == 1")
               .Define("Zcand_e","zed_leptonic_e[0]")
               .Define("Zcand_m","zed_leptonic_m[0]")
               .Define("Zcand_recoil_m","zed_leptonic_recoil_m[0]")
               .Define("Zcand_pt","zed_leptonic_pt[0]")
               .Define("Zcand_px","zed_leptonic_px[0]")
               .Define("Zcand_py","zed_leptonic_py[0]")
               .Define("Zcand_pz","zed_leptonic_pz[0]")
               .Define("Zcand_p","zed_leptonic_p[0]")
               .Define("Zcand_q","zed_leptonic_charge[0]")
               .Define("Zcand_phi", "zed_leptonic_phi[0]")
               .Define("Zcand_theta", "zed_leptonic_theta[0]")
               .Define("Zcand_cos","zed_leptonic_cos[0]")
               .Define("Zcand_y", "zed_leptonic_y[0]")
               .Define("Zcand_eta", "zed_leptonic_eta[0]")

        
               
               .Define("secondZ", "ReconstructedParticle::jetsum(jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("secondZ_m", "secondZ.M()")
               .Define("secondZ_px", "secondZ.Px()")
               .Define("secondZ_py", "secondZ.Py()")
               .Define("secondZ_pz", "secondZ.Pz()")
               .Define("secondZ_p", "secondZ.P()")
               .Define("secondZ_pt", "secondZ.Pt()")
               .Define("secondZ_theta", "secondZ.Theta()")
               .Define("secondZ_phi", "secondZ.Phi()")
               .Define("secondZ_eta", "secondZ.Eta()")

               #durham trie naturellement les jets dans l'ordre décroissant de p

               .Define("jet1_p", "jets_p2[0]")
               .Define("jet2_p", "jets_p2[1]")

               .Define("jet1_pt", "jets_pt2[0]")
               .Define("jet2_pt", "jets_pt2[1]")

               .Define("jet1_e", "jets_e2[0]")
               .Define("jet2_e", "jets_e2[1]")

               .Define("jet1_px", "jets_px2[0]")
               .Define("jet2_px", "jets_px2[1]")
               
               .Define("jet1_py", "jets_py2[0]")
               .Define("jet2_py", "jets_py2[1]")

               .Define("jet1_pz", "jets_pz2[0]")
               .Define("jet2_pz", "jets_pz2[1]")

               .Define("jet1_theta", "jets_theta2[0]")
               .Define("jet2_theta", "jets_theta2[1]")
               
               .Define("jet1_phi", "jets_phi2[0]")
               .Define("jet2_phi", "jets_phi2[1]")

               .Define("jet1_eta", "jets_eta2[0]")
               .Define("jet2_eta", "jets_eta2[1]")

               .Define("jet1_Nconst", "jetconstituents_2[0]")
               .Define("jet2_Nconst", "jetconstituents_2[1]")
               
               .Define("minNconst", "min(jet1_Nconst, jet2_Nconst)")
               .Define("maxNconst", "max(jet1_Nconst, jet2_Nconst)")
               .Define("meanNconst", "(jet1_Nconst + jet2_Nconst)/2")
               


               .Define("diffthetajets", "abs(jet1_theta - jet2_theta)")
               
               
               #.Define("visible_mass", "ReconstructedParticle::get_visible_mass(zed_leptonic_e, zed_leptonic_px, zed_leptonic_py, zed_leptonic_pz, secondZ)")
               
               #.Define("diff", "abs(visible_mass - visible_mass_predef)")
               
               #Durham N=3 

               .Define("jet1_3_Nconst", "jetconstituents_3[0]")
               .Define("jet2_3_Nconst", "jetconstituents_3[1]")
               .Define("jet3_3_Nconst", "jetconstituents_3[2]")
               
               .Define("minNconst_12_3", "min(jet1_3_Nconst, jet2_3_Nconst)")
               .Define("minNconst_3", "min(minNconst_12_3, jet3_3_Nconst)")
               
               .Define("maxNconst_12_3", "max(jet1_3_Nconst, jet2_3_Nconst)")
               .Define("maxNconst_3", "max(maxNconst_12_3, jet3_3_Nconst)")

               .Define("meanNconst_3", "(jet1_3_Nconst + jet2_3_Nconst + jet3_3_Nconst)/3")
               
	       .Define("new_missing_theta", "new_missing_tlv.Theta()") 
	       #.Define("delta_theta_miss_jet1", "abs(missing_theta - jet1_theta)")
               #.Define("delta_theta_miss_jet2", "abs(missing_theta - jet2_theta)")
	       #.Define("min_delta_theta_miss_jet", "min(delta_theta_miss_jet1, delta_theta_miss_jet2)")
	       #.Define("max_delta_theta_miss_jet", "max(delta_theta_miss_jet1, delta_theta_miss_jet2)") 

               .Define("new_angle_miss_jet", "ReconstructedParticle::get_angle(new_missing_tlv, jets_e2, jets_px2, jets_py2, jets_pz2)")
               .Define("new_angle_miss_jet1", "new_angle_miss_jet[0]")
               .Define("new_angle_miss_jet2", "new_angle_miss_jet[1]")
               .Define("new_min_angle_miss_jet", "min(new_angle_miss_jet1, new_angle_miss_jet2)")
               .Define("new_max_angle_miss_jet", "max(new_angle_miss_jet1, new_angle_miss_jet2)")

        
               )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list.
    def output():
        branchList = [
            "selected_muons_pt",
            "selected_electrons_pt",
            "selected_leptons_pt",

            "selected_muons_px",
            "selected_electrons_px",
            "selected_leptons_px",

            "selected_muons_py",
            "selected_electrons_py",
            "selected_leptons_py",

            "selected_muons_pz",
            "selected_electrons_pz",
            "selected_leptons_pz",

            "selected_muons_y",
            "selected_electrons_y",
            "selected_leptons_y",

            "selected_muons_p",
            "selected_electrons_p",
            "selected_leptons_p",

            "selected_muons_e",
            "selected_electrons_e",
            "selected_leptons_e",

            "N_zed_leptonic",
            "N_selected_leptons",
            
            "Zcand_e",
            "Zcand_m",
            "Zcand_recoil_m",
            "Zcand_pt",
            "Zcand_px",
            "Zcand_py",
            "Zcand_pz",
            "Zcand_p",
            "Zcand_q",
            "Zcand_phi",
            "Zcand_theta",
            "Zcand_cos",
            "Zcand_y",
            "Zcand_eta",

            
            "secondZ_m",
            "secondZ_px",
            "secondZ_py",
            "secondZ_pz",
            "secondZ_p",
            "secondZ_pt",
            "secondZ_theta",  
            "secondZ_eta",
            "secondZ_phi",
            

            "jet1_p",
            "jet1_pt",
            "jet1_e",
            "jet1_px",
            "jet1_py",
            "jet1_pz",
            "jet1_theta", 
            "jet1_phi",
            "jet1_eta",
            "jet1_Nconst",

            "jet2_p",
            "jet2_pt",
            "jet2_e",
            "jet2_px",
            "jet2_py",
            "jet2_pz",
            "jet2_theta", 
            "jet2_phi",
            "jet2_eta",
            "jet2_Nconst",

            
            "diffthetajets",
            
            
            "newemiss",
            "newpxmiss",
            "newpymiss",
            "newpzmiss",
            "newetmiss",
            
            "dmerge_2_45",
            "dmerge_2_34",
            "dmerge_2_23",
            "dmerge_2_12", 

            "new_visible_mass_predef", 

            "N_LooseLeptons",
	    "N_LooseLeptons_2",
            "LooseLeptons_pt",
            "LooseLeptons_theta", 
            "LooseLeptons_phi", 
            "LooseLeptons_p",

            "minNconst",
            "maxNconst",
            "meanNconst",

            "minNconst_3",
            "maxNconst_3",
            "meanNconst_3",

	    "new_missing_theta",
            "new_angle_miss_jet1",
            "new_angle_miss_jet2", 
            "new_min_angle_miss_jet", 
            "new_max_angle_miss_jet"
           # "delta_theta_miss_jet1",
           # "delta_theta_miss_jet2", 
	   # "min_delta_theta_miss_jet",
	   # "max_delta_theta_miss_jet"	
            

            
        ]
        return branchList
