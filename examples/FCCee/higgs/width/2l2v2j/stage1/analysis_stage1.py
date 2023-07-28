#Mandatory: List of processes

processList = {'wzp6_ee_mumuH_HZZ_ecm240':{},
               'wzp6_ee_mumuH_HWW_ecm240':{},
               'wzp6_ee_mumuH_HZa_ecm240':{},
               'wzp6_ee_mumuH_Haa_ecm240':{},
               'wzp6_ee_mumuH_Hbb_ecm240':{},
               'wzp6_ee_mumuH_Hcc_ecm240':{},
               'wzp6_ee_mumuH_Hgg_ecm240':{},
               'wzp6_ee_mumuH_Hmumu_ecm240':{},
               'wzp6_ee_mumuH_Hss_ecm240':{},
               'wzp6_ee_mumuH_Htautau_ecm240':{},
               'wzp6_ee_nunuH_HZZ_ecm240':{},
               'wzp6_ee_nunuH_HWW_ecm240':{},
               'wzp6_ee_nunuH_HZa_ecm240':{},
               'wzp6_ee_nunuH_Haa_ecm240':{},
               'wzp6_ee_nunuH_Hbb_ecm240':{},
               'wzp6_ee_nunuH_Hcc_ecm240':{},
               'wzp6_ee_nunuH_Hgg_ecm240':{},
               'wzp6_ee_nunuH_Hmumu_ecm240':{},
               'wzp6_ee_nunuH_Hss_ecm240':{},
               'wzp6_ee_nunuH_Htautau_ecm240':{},
               'wzp6_ee_eeH_HZZ_ecm240':{},
               'wzp6_ee_eeH_HWW_ecm240':{},
               'wzp6_ee_eeH_HZa_ecm240':{},
               'wzp6_ee_eeH_Haa_ecm240':{},
               'wzp6_ee_eeH_Hbb_ecm240':{},
               'wzp6_ee_eeH_Hcc_ecm240':{},
               'wzp6_ee_eeH_Hgg_ecm240':{},
               'wzp6_ee_eeH_Hmumu_ecm240':{},
               'wzp6_ee_eeH_Hss_ecm240':{},
               'wzp6_ee_eeH_Htautau_ecm240':{},
               'wzp6_ee_ee_Mee_30_150_ecm240':{},
               'p8_ee_ZZ_ecm240':{}, #Run the full statistics in one output file named <outputDir>/p8_ee_ZZ_ecm240.root
               'p8_ee_WW_ecm240':{} #Run 50% of the statistics in two files named <outputDir>/p8_ee_WW_ecm240/chunk<N>.root
    #'p8_ee_ZH_#ecm240':{'fraction':0.2, 'output':'p8_ee_ZH_ecm240_out'} #Run 20% of the statistics in one file named <outputDir>/p8_ee_ZH_ecm240_out.root (example on how to change the output name)
               }

#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
prodTag     = "FCCee/winter2023/IDEA/" #IDEA concept de detecteur

#Optional: output directory, default is local running directory
#outputDir   = "outputs/fccee/higgs/mH-recoil/hzz/stage1/"
outputDir   = "outputs/fccee/higgs/mH-recoil/neutrinos/stage1/"


#Optional: analysisName, default is ""
analysisName = "Testanalysis"

#Optional: ncpus, default is 4
nCPUS       = 128

#Optional running on HTCondor, default is False
#runBatch    = False

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
#compGroup = "group_u_FCC.local_gen"

#Optional test file
#testFile ="root://eospublic.cern.ch//eos/experiment/fcc/ee/generation/DelphesEvents/spring2021/IDEA/p8_ee_ZH_ecm240/events_101027117.root"




#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (
            df
            .Alias("Muon0", "Muon#0.index")
            .Alias("Electron0", "Electron#0.index")


            #.Define("vrai_Z", "MCParticle::sel_pdgID(23, true)(Particle)")


            .Define("muons",                "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
            .Define("electrons",            "ReconstructedParticle::get(Electron0, ReconstructedParticles)")

#on sélectionne des muons/électrons qui sont isolés + dans un certain intervalle de momentum : ne devraient pas venir des jets 

            .Define("selected_muons",       "ReconstructedParticle::sel_p(25,80)(muons)")
            .Define("selected_electrons",   "ReconstructedParticle::sel_p(25,80)(electrons)")
            .Define("selected_leptons",     "ReconstructedParticle::merge(selected_muons, selected_electrons)")


            .Define("LooseMuons",       "ReconstructedParticle::sel_p(10)(muons)")
            .Define("LooseElectrons",   "ReconstructedParticle::sel_p(10)(electrons)")
            .Define("LooseLeptons",     "ReconstructedParticle::merge(LooseMuons, LooseElectrons)")

            .Define("LooseMuons_2",       "ReconstructedParticle::sel_p(2)(muons)")                  
            .Define("LooseElectrons_2",   "ReconstructedParticle::sel_p(2)(electrons)")
            .Define("LooseLeptons_2",     "ReconstructedParticle::merge(LooseMuons_2, LooseElectrons_2)") 
	    
            .Define("LooseMuons_1",       "ReconstructedParticle::sel_p(1)(muons)")                  
            .Define("LooseElectrons_1",   "ReconstructedParticle::sel_p(1)(electrons)")
            .Define("LooseLeptons_1",     "ReconstructedParticle::merge(LooseMuons_1, LooseElectrons_1)") 


	    .Define("N_LooseLeptons", "ReconstructedParticle::get_n(LooseLeptons)")
            .Define("N_LooseLeptons_2", "ReconstructedParticle::get_n(LooseLeptons_2)")
            .Define("N_LooseLeptons_1", "ReconstructedParticle::get_n(LooseLeptons_1)")

            .Define("LooseLeptons_pt", "ReconstructedParticle::get_pt(LooseLeptons)")
            .Define("LooseLeptons_theta", "ReconstructedParticle::get_theta(LooseLeptons)")
            .Define("LooseLeptons_phi", "ReconstructedParticle::get_phi(LooseLeptons)")
            .Define("LooseLeptons_p", "ReconstructedParticle::get_p(LooseLeptons)")
            
#pt de ces particules
            
            .Define("selected_muons_pt",    "ReconstructedParticle::get_pt(selected_muons)")
            .Define("selected_electrons_pt","ReconstructedParticle::get_pt(selected_electrons)")
            .Define("selected_leptons_pt",  "ReconstructedParticle::get_pt(selected_leptons)")

#px 

            .Define("selected_muons_px",    "ReconstructedParticle::get_px(selected_muons)")
            .Define("selected_electrons_px","ReconstructedParticle::get_px(selected_electrons)")
            .Define("selected_leptons_px",  "ReconstructedParticle::get_px(selected_leptons)")

#py 

            .Define("selected_muons_py",    "ReconstructedParticle::get_py(selected_muons)")
            .Define("selected_electrons_py","ReconstructedParticle::get_py(selected_electrons)")
            .Define("selected_leptons_py",  "ReconstructedParticle::get_py(selected_leptons)")

#pz 

            .Define("selected_muons_pz",    "ReconstructedParticle::get_pz(selected_muons)")
            .Define("selected_electrons_pz","ReconstructedParticle::get_pz(selected_electrons)")
            .Define("selected_leptons_pz",  "ReconstructedParticle::get_pz(selected_leptons)")

#rapidité
            
            .Define("selected_muons_y",     "ReconstructedParticle::get_y(selected_muons)")
            .Define("selected_electrons_y", "ReconstructedParticle::get_y(selected_electrons)")
            .Define("selected_leptons_y",   "ReconstructedParticle::get_y(selected_leptons)")


#momentum
            
            .Define("selected_muons_p",     "ReconstructedParticle::get_p(selected_muons)")
            .Define("selected_electrons_p", "ReconstructedParticle::get_p(selected_electrons)")
            .Define("selected_leptons_p",   "ReconstructedParticle::get_p(selected_leptons)")


#energie

            .Define("selected_muons_e",     "ReconstructedParticle::get_e(selected_muons)")
            .Define("selected_electrons_e", "ReconstructedParticle::get_e(selected_electrons)")
            .Define("selected_leptons_e",   "ReconstructedParticle::get_e(selected_leptons)")


#nombre de muons/électrons et de la somme (merge : leptons) qui ont passé la sélection

            .Define("N_selected_muons",     "ReconstructedParticle::get_n(selected_muons)")
            .Define("N_selected_electrons", "ReconstructedParticle::get_n(selected_electrons)")
            .Define("N_selected_leptons",   "ReconstructedParticle::get_n(selected_leptons)")

#on sélectionne 2 muons (ou 0 si pas de muons) étant les meilleurs candidats au Z ; findZleptons garde les leptons, ne construit pas le Z
#on crée le Z/somme avec resonanceBuilder
#on enlève ces deux muons des selected muons et on réitère la procédure puisque l'on peut avoir jusqu'à trois paires de muons venant des 3 Z*

            .Define("zed_muons",         "ReconstructedParticle::findZleptons(selected_muons)")

            
            .Define("zed_muonic",        "ReconstructedParticle::resonanceBuilder(91)(zed_muons)") 
            .Define("sselected_muons",   "ReconstructedParticle::remove(selected_muons, zed_muons)")
            .Define("zed_muonsbis",      "ReconstructedParticle::findZleptons(sselected_muons)")
            .Define("zed_muonic2",       "ReconstructedParticle::resonanceBuilder(91)(zed_muonsbis)")
            .Define("ssselected_muons",  "ReconstructedParticle::remove(sselected_muons, zed_muonsbis)")
            .Define("zed_muonsbisbis",   "ReconstructedParticle::findZleptons(ssselected_muons)")
            .Define("zed_muonic3",       "ReconstructedParticle::resonanceBuilder(91)(zed_muonsbisbis)")

#on fait une liste avec les muons qui n'ont pas pu former de paires, dans un cas de nombre impair 

            .Define("extramuons",        "ReconstructedParticle::remove(ssselected_muons, zed_muonsbisbis)")
            .Define("N_extramuons",      "ReconstructedParticle::get_n(extramuons)")

#même procédure que pour les muons mais avec les électrons

            .Define("zed_electrons",     "ReconstructedParticle::findZleptons(selected_electrons)")

            .Define("zed_electronic",    "ReconstructedParticle::resonanceBuilder(91)(zed_electrons)")
            .Define("sselected_electrons", "ReconstructedParticle::remove(selected_electrons, zed_electrons)")
            .Define("zed_electronsbis",      "ReconstructedParticle::findZleptons(sselected_electrons)")
            .Define("zed_electronic2",     "ReconstructedParticle::resonanceBuilder(91)(zed_electronsbis)")
            .Define("ssselected_electrons","ReconstructedParticle::remove(sselected_electrons, zed_electronsbis)")
            .Define("zed_electronsbisbis", "ReconstructedParticle::findZleptons(ssselected_electrons)")
            .Define("zed_electronic3",     "ReconstructedParticle::resonanceBuilder(91)(zed_electronsbisbis)")

#liste des électrons isolés/dans le range de p mais qui n'ont pas formé de paires

            .Define("extraelectrons",      "ReconstructedParticle::remove(ssselected_electrons, zed_electronsbisbis)")
            .Define("N_extraelectrons",    "ReconstructedParticle::get_n(extraelectrons)")

#on veut regrouper les 3 Z ensemble, donc les 3 muonic d'abord

            .Define("mergemuonic1",         "ReconstructedParticle::merge(zed_muonic, zed_muonic2)")
            .Define("mergemuonic2",         "ReconstructedParticle::merge(mergemuonic1, zed_muonic3)")

#et les 3 electronic (mais il n'y en aura qu'au maximum 3/6 non vides puisque trois Z max, ou alors bckg)
            
            .Define("mergeelectronic1",     "ReconstructedParticle::merge(zed_electronic, zed_electronic2)")
            .Define("mergeelectronic2",     "ReconstructedParticle::merge(mergeelectronic1, zed_electronic3)")

#et là on merge les 6 pour donner zed_leptonic 

            .Define("zed_leptonic",         "ReconstructedParticle::merge(mergemuonic2, mergeelectronic2)")

#on fait la liste de tous les leptons qui sont sélectionnés mais qui n'ont pas pu former de paires compatibles au Z

            .Define("extraleptons",         "ReconstructedParticle::merge(extramuons, extraelectrons)")

#puis on regarde le nombre de paires de Z et d'extraleptons

            .Define("N_zed_leptonic",       "ReconstructedParticle::get_n(zed_leptonic)")
            .Define("N_extraleptons",       "ReconstructedParticle::get_n(extraleptons)")
            

            

            #get_e ne fonctionne pas sur zed_leptonic donc on peut le faire sur les leptons directement puis on sommera [0] et [1] pour avoir la composante d'énergie du tlv du Z (on n'a qu'un seul candidat au Z en stage 2 avec le fitlre donc on fait ça qu'avec les premières paires (et meilleures) d'électrons et muons de findZleptons 

            .Define("zed_electrons_e", "ReconstructedParticle::get_e(zed_electrons)")
            .Define("zed_muons_e", "ReconstructedParticle::get_e(zed_muons)")
            .Define("zed_leptons", "ReconstructedParticle::merge(zed_electrons, zed_muons)")
            .Define("zed_leptons_e", "ReconstructedParticle::get_e(zed_leptons)")
            


#propriétés de nos paires Z
            .Define("zed_leptonic_e",       "ReconstructedParticle::get_e(zed_leptonic)")
            .Define("zed_leptonic_m",       "ReconstructedParticle::get_mass(zed_leptonic)")
            .Define("zed_leptonic_pt",      "ReconstructedParticle::get_pt(zed_leptonic)")
            .Define("zed_leptonic_px",      "ReconstructedParticle::get_px(zed_leptonic)")
            .Define("zed_leptonic_py",      "ReconstructedParticle::get_py(zed_leptonic)") 
            .Define("zed_leptonic_pz",      "ReconstructedParticle::get_pz(zed_leptonic)")
            .Define("zed_leptonic_p",       "ReconstructedParticle::get_p(zed_leptonic)")
            .Define("zed_leptonic_recoil",  "ReconstructedParticle::recoilBuilder(240)(zed_leptonic)")
            .Define("zed_leptonic_recoil_m","ReconstructedParticle::get_mass(zed_leptonic_recoil)")            
            .Define("zed_leptonic_charge",  "ReconstructedParticle::get_charge(zed_leptonic)")
            .Define("zed_leptonic_theta",   "ReconstructedParticle::get_theta(zed_leptonic)")
            .Define("zed_leptonic_phi",     "ReconstructedParticle::get_phi(zed_leptonic)")
            .Define("zed_leptonic_y",       "ReconstructedParticle::get_y(zed_leptonic)")
            .Define("zed_leptonic_eta",     "ReconstructedParticle::get_eta(zed_leptonic)") 
            .Define("zed_leptonic_cos",     "cos(ReconstructedParticle::get_theta(zed_leptonic))")

#on fait la liste des leptons qui ont servi pour les paires : donc les selected - les extra
            
            .Define("taken_leptons",    "ReconstructedParticle::remove(selected_leptons, extraleptons)")
            .Define("N_taken_leptons",  "ReconstructedParticle::get_n(taken_leptons)")

#on sélectionne toutes les particules - celles utilisées pour les paires de Z pour reconstruire les jets
#puis on crée des pseudo-jets avec 

            .Define("my_recoparticles",  "ReconstructedParticle::remove(ReconstructedParticles, taken_leptons)")
            .Define("RP_px", "ReconstructedParticle::get_px(my_recoparticles)")
            .Define("RP_py", "ReconstructedParticle::get_py(my_recoparticles)")
            .Define("RP_pz", "ReconstructedParticle::get_pz(my_recoparticles)")
            .Define("RP_e", "ReconstructedParticle::get_e(my_recoparticles)")
            .Define("pseudo_jets",  "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")


            #Durham N=2

#construction des jets selon l'algo durham kt pour N=2 + (ligne2) mise en objet "pseudo_jets", dont on peut extraire des informations cinématiques
            .Define("FCCAnalysesJets_ee_genkt2",  "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)")
            .Define("jets_ee_genkt2",  "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_genkt2)")
        

            .Define("jets_px2",  "JetClusteringUtils::get_px(jets_ee_genkt2)")
            .Define("jets_py2",  "JetClusteringUtils::get_py(jets_ee_genkt2)")
            .Define("jets_pz2",  "JetClusteringUtils::get_pz(jets_ee_genkt2)")
            .Define("jets_p2",   "JetClusteringUtils::get_p(jets_ee_genkt2)")
            .Define("jets_e2",   "JetClusteringUtils::get_e(jets_ee_genkt2)")
            .Define("jets_m2",   "JetClusteringUtils::get_m(jets_ee_genkt2)")
            .Define("jets_pt2",  "JetClusteringUtils::get_pt(jets_ee_genkt2)")
            .Define("jets_y2",   "JetClusteringUtils::get_y(jets_ee_genkt2)")
            .Define("jets_eta2", "JetClusteringUtils::get_eta(jets_ee_genkt2)")
            .Define("jets_theta2", "JetClusteringUtils::get_theta(jets_ee_genkt2)")
            .Define("jets_phi2", "JetClusteringUtils::get_phi(jets_ee_genkt2)")

            .Define("jetconstituents_ee_genkt2", "JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_genkt2)")
            .Define("jetconstituents_ee_2", "JetConstituentsUtils::build_constituents_cluster(my_recoparticles, jetconstituents_ee_genkt2)")
            .Define("jetconstituents_2", "JetConstituentsUtils::count_consts(jetconstituents_ee_2)")
            
            

#j'ai l'impression que ça (la fonction get_constituents) donne le nombre de particules dans le jet 

            .Define("dmerge_2_45", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 4)")
            .Define("dmerge_2_34", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 3)")
            .Define("dmerge_2_23", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 2)")
            .Define("dmerge_2_12", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt2, 1)")


            
            #Durham N=3

#construction des jets selon l'algo durham kt pour N=2 + (ligne2) mise en objet "pseudo_jets", dont on peut extraire des informations cinématiques
            .Define("FCCAnalysesJets_ee_genkt3",  "JetClustering::clustering_ee_kt(2, 3, 1, 0)(pseudo_jets)")
            .Define("jets_ee_genkt3",  "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_genkt3)")
        



            .Define("jets_px3",  "JetClusteringUtils::get_px(jets_ee_genkt3)")
            .Define("jets_py3",  "JetClusteringUtils::get_py(jets_ee_genkt3)")
            .Define("jets_pz3",  "JetClusteringUtils::get_pz(jets_ee_genkt3)")
            .Define("jets_p3",   "JetClusteringUtils::get_p(jets_ee_genkt3)")
            .Define("jets_e3",   "JetClusteringUtils::get_e(jets_ee_genkt3)")
            .Define("jets_m3",   "JetClusteringUtils::get_m(jets_ee_genkt3)")
            .Define("jets_pt3",  "JetClusteringUtils::get_pt(jets_ee_genkt3)")
            .Define("jets_y3",   "JetClusteringUtils::get_y(jets_ee_genkt3)")
            .Define("jets_eta3", "JetClusteringUtils::get_eta(jets_ee_genkt3)")
            .Define("jets_theta3", "JetClusteringUtils::get_theta(jets_ee_genkt3)")
            .Define("jets_phi3", "JetClusteringUtils::get_phi(jets_ee_genkt3)")

            .Define("jetconstituents_ee_genkt3", "JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_genkt3)")
            .Define("jetconstituents_ee_3", "JetConstituentsUtils::build_constituents_cluster(my_recoparticles, jetconstituents_ee_genkt3)")
            .Define("jetconstituents_3", "JetConstituentsUtils::count_consts(jetconstituents_ee_3)")
            
            

#j'ai l'impression que ça (la fonction get_constituents) donne le nombre de particules dans le jet 

            .Define("dmerge_3_45", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 4)")
            .Define("dmerge_3_34", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 3)")
            .Define("dmerge_3_23", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 2)")
            .Define("dmerge_3_12", "JetClusteringUtils::get_exclusive_dmerge(FCCAnalysesJets_ee_genkt3, 1)")


            
            
            
            
            

            
#hzz monte carlo

            .Alias("Particle1", "Particle#1.index")
            .Define("hzz_decay", "MCParticle::fill_ZHZZ_decay(Particle, Particle1)")

            .Define("inv_mass_Z", "MCParticle::invariant_mass(hzz_decay.Z_decay)")
            .Define("pdg_Z", "MCParticle::get_pdg(hzz_decay.Z_decay)")

            .Define("inv_mass_Z1", "MCParticle::invariant_mass(hzz_decay.Z1_decay)")
            .Define("pdg_Z1", "MCParticle::get_pdg(hzz_decay.Z1_decay)")

            .Define("inv_mass_Z2", "MCParticle::invariant_mass(hzz_decay.Z2_decay)")
            .Define("pdg_Z2", "MCParticle::get_pdg(hzz_decay.Z2_decay)")

#testé ici mais va au stage 2 Zleptonique
            #.Define("Zelectronique", "MCParticle::sel_pdgID(11, true)(hzz_decay.Z_decay)")
            #.Define("Zmuonique","MCParticle::sel_pdgID(13, true)(hzz_decay.Z_decay)")
            #.Define("Zleptonique", "MCParticle::mergeParticles(Zelectronique, Zmuonique)")

            
#prendre les MCParticles qui ont passé le filtre de Z leptonique : liste Zleptonique 
#il faut faire pareil que pour Z mais pour Z1 et Z2 (l'un après l'autre c'est ok je pense à chaque fois faut juste prendre la liste qui a subi les sélections) , mais là attention il faut faire un sel_pdgID avec des sortes de où pour avoir tous les quarks/gluon : écrire une fonction ? en se basant sur sel_pdgID mais en rajoutant + d'arguments en entrée et un ou dans les condit

            .Define("emiss", "MissingET.energy[0]")
            .Define("pxmiss", "MissingET.momentum.x[0]")
            .Define("pymiss", "MissingET.momentum.y[0]")
            .Define("pzmiss", "MissingET.momentum.z[0]")
            .Define("missing_tlv", "ReconstructedParticle::get_tlv(MissingET)")
            .Define("etmiss", "sqrt((MissingET.momentum.x[0])*(MissingET.momentum.x[0]) + (MissingET.momentum.y[0])*(MissingET.momentum.y[0]))")
            .Define("visible_4vector", "ReconstructedParticle::get_P4vis(ReconstructedParticles)")
            .Define("visible_mass_predef", "visible_4vector.M()")

            )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
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

            "N_selected_muons",
            "N_selected_electrons",
            "N_selected_leptons",
            "N_extramuons",
            "N_extraelectrons",
            "N_taken_leptons",

            "N_zed_leptonic",
            "zed_leptonic_e",
            "zed_leptonic_pt",
            "zed_leptonic_px",
            "zed_leptonic_py", 
            "zed_leptonic_pz",
            "zed_leptonic_p",
            "zed_leptonic_m",
            "zed_leptonic_charge",
            "zed_leptonic_recoil_m",
            "zed_leptonic_phi",
            "zed_leptonic_theta",
            "zed_leptonic_cos",
            "zed_leptonic_y",
            "zed_leptonic_eta",

            "jets_px2",
            "jets_py2",
            "jets_pz2",
            "jets_p2",
            "jets_e2",
            "jets_m2",
            "jets_pt2",
            "jets_y2",
            "jets_eta2",
            "jets_theta2",
            "jets_phi2",
            "jetconstituents_ee_genkt2",
            "jetconstituents_ee_2",
            "jetconstituents_2",
            "dmerge_2_45",
            "dmerge_2_34",
            "dmerge_2_23",
            "dmerge_2_12",
            
            "jets_px3",
            "jets_py3",
            "jets_pz3",
            "jets_p3",
            "jets_e3",
            "jets_m3",
            "jets_pt3",
            "jets_y3",
            "jets_eta3",
            "jets_theta3",
            "jets_phi3",
            "jetconstituents_ee_genkt3",
            "jetconstituents_ee_3",
            "jetconstituents_3",
            "dmerge_3_45",
            "dmerge_3_34",
            "dmerge_3_23",
            "dmerge_3_12",


            
            "hzz_decay",
            "inv_mass_Z",
            "pdg_Z",

            "inv_mass_Z1",
            "pdg_Z1",

            "inv_mass_Z2",
            "pdg_Z2",

            "emiss",
            "pxmiss",
            "pymiss",
            "pzmiss",
            "etmiss",
	    "missing_tlv",

            "visible_mass_predef",

            "N_LooseLeptons",
	    "N_LooseLeptons_2",
            "N_LooseLeptons_1",
            "LooseLeptons_pt",
            "LooseLeptons_theta", 
            "LooseLeptons_phi", 
            "LooseLeptons_p",
            
            "zed_electrons_e",
            "zed_muons_e",
            "zed_leptons_e"
            

            
]

        return branchList


