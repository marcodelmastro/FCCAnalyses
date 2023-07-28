#ifndef  ZH_WHIZARD_ANALYZERS_H
#define  ZH_WHIZARD_ANALYZERS_H

#include <cmath>
#include <vector>

#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"
#include "edm4hep/MCParticleData.h"
#include "edm4hep/ParticleIDData.h"
#include "edm4hep/Vector3f.h"
#include "edm4hep/Vector3d.h"
#include "edm4hep/Vector2i.h"


/** ZH_Whizard interface.
This represents a set functions and utilities to access ZH final state, and especially classify ZHZZ events
*/
namespace FCCAnalyses{

namespace MCParticle{

  struct ZHZZ {
    //'lonely'Z
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z_decay;
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Higgs;
    //on shell Z from the Higgs
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z1_decay;
    //off shell Z from the Higgs
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z2_decay;
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z1_completedecay;
    ROOT::VecOps::RVec<edm4hep::MCParticleData> Z2_completedecay;
  };

  struct thetaphi {
    ROOT::VecOps::RVec<float> Z1_theta;
    ROOT::VecOps::RVec<float> Z1_phi;
    ROOT::VecOps::RVec<float> Z1_energy;
    ROOT::VecOps::RVec<float> Z2_theta;
    ROOT::VecOps::RVec<float> Z2_phi;
    ROOT::VecOps::RVec<float> Z2_energy;
  };

  thetaphi fill_thetaphi_Zdecay(const ZHZZ &HZZ);

  // fill a struct with information from ZH, H->ZZ decays
  ZHZZ fill_ZHZZ_decay(const ROOT::VecOps::RVec<edm4hep::MCParticleData> &in,
                       const ROOT::VecOps::RVec<int> &ind);

  // return the invariant mass of particles in the input collection
  float invariant_mass(const ROOT::VecOps::RVec<edm4hep::MCParticleData> &in);


}//end NS MCParticle

}//end NS FCCAnalyses
#endif
