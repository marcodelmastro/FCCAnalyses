#include "FCCAnalyses/ZH_Whizard.h"
#include "FCCAnalyses/MCParticle.h"
#include <iostream>
#include <algorithm>
#include <set>


namespace FCCAnalyses{

namespace MCParticle{

  ZHZZ fill_ZHZZ_decay(const ROOT::VecOps::RVec<edm4hep::MCParticleData> &in,
                       const ROOT::VecOps::RVec<int> &ind) {
    ZHZZ res;

    // check if we have a HZZ decay, and collect H and ZZ indices
    ROOT::VecOps::RVec<int> HZZ_indices = get_indices(25, {23, 23}, false, false, false, false)(in, ind);

    if (HZZ_indices.empty()) {
      return res;
    }

    res.Higgs.push_back(in[HZZ_indices[0]]);
    int ind_Z_on_shell = 0;
    int ind_Z_off_shell = 0;
    if (in[HZZ_indices[1]].mass > in[HZZ_indices[2]].mass) {
      ind_Z_on_shell = HZZ_indices[1];
      ind_Z_off_shell = HZZ_indices[2];
    }
    else {
      ind_Z_on_shell = HZZ_indices[2];
      ind_Z_off_shell = HZZ_indices[1];
    }
    std::vector<int> Z1_idx = get_list_of_particles_from_decay(ind_Z_on_shell, in, ind);
    res.Z1_decay.push_back(in[Z1_idx[0]]);
    res.Z1_decay.push_back(in[Z1_idx[1]]);
    std::vector<int> Z1_idxstable = get_list_of_stable_particles_from_decay(ind_Z_on_shell, in, ind);
    std::set<int> Z1_idxstable_uniq(Z1_idxstable.begin(), Z1_idxstable.end());
    for (int idx : Z1_idxstable_uniq) {
      res.Z1_completedecay.push_back(in[idx]);
      //std::cout << in[Z1_idx[i]].generatorStatus << std::endl;
    }

    std::vector<int> Z2_idx = get_list_of_particles_from_decay(ind_Z_off_shell, in, ind);
    res.Z2_decay.push_back(in[Z2_idx[0]]);
    res.Z2_decay.push_back(in[Z2_idx[1]]);
    std::vector<int> Z2_idxstable = get_list_of_stable_particles_from_decay(ind_Z_off_shell, in, ind);
    std::set<int> Z2_idxstable_uniq(Z2_idxstable.begin(), Z2_idxstable.end());
    for (int idx : Z2_idxstable_uniq) {
      res.Z2_completedecay.push_back(in[idx]);
    }

    res.Z_decay.push_back(in[8]);
    res.Z_decay.push_back(in[9]);

    return res;
  }

  
  thetaphi fill_thetaphi_Zdecay(const ZHZZ &HZZ){
    thetaphi res; 
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z1_finaldecay;
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z2_finaldecay;
    
							       
    for (auto & p: HZZ.Z1_completedecay) {
      //std::cout << p.generatorStatus << std::endl;
      if (p.generatorStatus == 1) {
	Z1_finaldecay.push_back(p);
      } 
    }
    for (auto & q: HZZ.Z2_completedecay) {
      if (q.generatorStatus == 1) {
	Z2_finaldecay.push_back(q);
      }
    }
 
    res.Z1_theta = get_theta(Z1_finaldecay);
    res.Z1_phi = get_phi(Z1_finaldecay);
    res.Z1_energy = get_e(Z1_finaldecay);
    res.Z2_theta = get_theta(Z2_finaldecay);
    res.Z2_phi = get_phi(Z2_finaldecay);
    res.Z2_energy = get_e(Z2_finaldecay);
 

    return res;
  }



    

  

  float invariant_mass(const ROOT::VecOps::RVec<edm4hep::MCParticleData> &in) {
    TLorentzVector res;
    for (auto & p: in) {
      TLorentzVector tlv;
      tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
      res += tlv;
    }
    return res.M();
  }

}//end NS MCParticle

}//end NS FCCAnalyses
