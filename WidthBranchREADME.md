 # WIDTH BRANCH README
 
 ## General method

In general, the files to create the histograms can be found in the following directory:
> [/examples/FCCee/higgs/width](/examples/FCCee/higgs/width)

The files are ready for two different cases: 
- The 4-jets channel: */examples/FCCee/higgs/width/4jets*
- The mixed channels: */examples/FCCee/higgs/width/2l2v2j*


*Note:* 
> For the mixed channels, there are three channels which are taken into account in this analysis. The first stage (*stage 1*) is common to the three channels, but the following steps are not. The directory [2l2v2j](/examples/FCCee/higgs/width/2l2v2j) is subdivided into three directories containing their own *stage 2*, *final* and *plots*. There are also four datacards for the fit in the [combine](/combine) directory : one per channel and one for the combination. 

Here are the main steps followed in a general way:
1. stage 1  
file.py: examples/FCCee/higgs/width/choice/stage1/analysis_stage1.py  
input: MC samples  
command: ` fccanalysis run file.py `  

1. stage 2  
file.py: examples/FCCee/higgs/width/choice/stage2/stage2.py  
input: *stage 1* output  
command: ``` fccanalysis run file.py ```  

1. final 
file.py: examples/FCCee/higgs/width/choice/final/final.py  
input: *stage 2* output  
command: ``` fccanalysis final file.py ```  

1. plots  
file.py: examples/FCCee/higgs/width/choice/plots/plots.py  
input: *final* output  
command: ``` fccanalysis plots file.py ```  

1. sum - step used to sum the histograms of the chosen variable (*final* output) before the fit  
file.py: examples/FCCee/higgs/width/choice/final/sum.py  
command: ``` python file.py ```  

1. fit - (new shell without the doing the FCC setup but doing the COMBINE one :  ``` source initCombine.sh  ```)  
datacard.txt : combine/channel/channeldatacard.txt  
    2 commands:   
    ```
    text2workspace.py datacard.txt -o ws.root  -v 10  
    combine -M FitDiagnostics -t -1 ws.root --expectSignal=1 -v 10  
    ```
    (Here is the link to the [COMBINE](http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part2/settinguptheanalysis/) page to help preparing datacards)  

## Smearing

The smearing is applied in the *stage 1*, and which can be found in the file stage1/stage1_smear.py. Then, we need to run again all the steps of the analysis described before to perform the fit in the end.  
To do so, similar files can be found in the directories stage2/ final/ and plots/ (same ones as before).  

1. stage 1 - where we change (manually) the scale factor in the **first** argument of the function *SmearedReconstructedParticle()*  
file.py: examples/FCCee/higgs/width/choice/stage1/stage1_smear.py  
input: MC samples  
output: outputs/.../stage1/smear_sf_scalefactor/ => one subdirectory per scale factor  
command: ``` fccanalysis run file.py ```  

1. stage 2  
file.py: examples/FCCee/higgs/width/choice/stage2/stage2_bdt.py  
input: outputs/.../stage1/smear_sf_scalefactor/  
output:  outputs/.../stage2/smear_sf_scalefactor/  
command: ``` fccanalysis run file.py ```  

1. final  
file.py: examples/FCCee/higgs/width/choice/final/final_bdt.py  
input: outputs/.../stage2/smear_sf_scalefactor/  
output:  outputs/.../final/smear_sf_scalefactor/  
command: ``` fccanalysis final file.py ```  

1. sum - step used to sum the histograms of the chosen variable (*final* output) before the fit  
file.py: examples/FCCee/higgs/width/choice/final/sum.py  
command: ``` python file.py ```  

1. fit - (new shell without the doing the FCC setup but doing the COMBINE one :  ``` source initCombine.sh  ```)  
datacard.txt : combine/channel/channeldatacardsmear.txt  
2 commands:   
    ```
    text2workspace.py datacardsmear.txt -o ws.root  -v 10  
    combine -M FitDiagnostics -t -1 ws.root --expectSignal=1 -v 10  
    ```

## BDT

For the BDT, we will use the same *stage 1* as before (without smear). Then, we run again all the steps described in the first part (General Method). 

1. stage1  
file.py: examples/FCCee/higgs/width/choice/stage1/analysis_stage1.py  
command: ``` fccanalysis run file.py ```  

2. stage 2 - similar to other stage 2 but with new variables that we will use in the BDT (typically, 3D angles determined with the function  *get_angle_general* in ReconstructedParticle) + large pre-BDT filters + filters to preserve orthogonality between the channels (dijet mass and leptonic recoil mass selections)  
file.py: examples/fccee/higgs/mH-recoil/choix/stage2/stage2_bdt.py  
command: ``` fccanalysis run file.py ```  

3. **BDT section**  
    For the BDT itself, there are two commands to run:  
    ```
    python train_test.py config_choice.py  
    python evaluate_test.py config_choice.py  
    ```
    
    The config file is written for either the 4-jets channel in « config_4jets.py » or for one of the mixed channels in config_mixed_channels.py. 
    - variables
    - classes 
    - v (name of the version)
    The only difference in the config file between the training and the evaluation is the path. 
    - for the training, mergedtrees (eeH and mumuH samples should be merged in one single file) 
    - for the evaluation, all the output samples from the stage2_bdt.py command 
    
    4 models are already trained: 
    - 3 '6 classes models' for each *2l2v2j* channel 
    1. model_6classes_lljjvv.pkl
    1. model_6classes_llvvjj.pkl
    1. model_6classes_vvlljj.pkl
    - one for the 4-jets channel : model_test1_4jets.pkl
    
    > *Note:* To run the evaluation with these models, the name of the version (v) must be the same in the config file as the one for the training, the version is given in the name of the model : *model_v.pkl*
    
    The evaluation outputs go in a new directory called pathdirectory_score_v, and the samples are the same as the inputs ones but with the BDT scores as well as the optimal signal/background discriminator called **myScore**. 

4. final  
    file.py: examples/FCCee/higgs/width/choice/final/final_bdt.py  
    input : outputs/.../stage2/bdt_score_v  
    command : ``` fccanalysis final file.py ```  
    
5. sum  
file.py: examples/FCCee/higgs/width/choice/final/sum.py  
input : outputs/.../final/bdt_score_v  
command : ``` python file.py ```  

6. fit  
datacard.txt: combine/channel/channeldatacardBDT.txt  
2 commands:  
    ```
    text2workspace.py datacardBDT.txt -o ws.root  -v 10  
    combine -M FitDiagnostics -t -1 ws.root --expectSignal=1 -v 10  
    ```







