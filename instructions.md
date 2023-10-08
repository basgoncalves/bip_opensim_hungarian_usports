# BIP OpenSim

Basilio Goncalves - basilio.goncalves@univie.ac.at
Hnas Kainz - hans.kainz@univie.ac.at

![Alt text](.\Snippets\1.0.2_NRG.png) ![Alt text](\Snippets\1.0.2_UniVie.png)

## Required Software
- OpenSim (version 4.4 preferable)
- Mokka 
- Windows OS (tutorial works for Mac with minor adjustments)

## Useful tutorials:
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/Tutorial+1+-+Intro+to+Musculoskeletal+Modeling
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/Workshops+and+Events
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/ESMAC+Workshop+September+2022
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/Overview+of+OpenSim+Workflows#OverviewofOpenSimWorkflows-SimulationPipelines(Workflows)

# Useful tools:
- VSCode or other IDE

## Check the cheat_sheet.pdf for detailed information on terminology used throughout
- Bodies
- Actuators
- Probes
- Markers

# --------------------------------------- 
#               Day 1            
# ---------------------------------------  

# 1. Intro - 3h

## 1.1 Quick examples based on presentations (20 min)

For years, we've been fascinated with measuring muscle and joint loads. But not easy to measure in-vivo.

### Paper 1 - Komi 1982
Let's start by simulating running quickly and examining tendon forces. Later, we'll compare our findings with those presented in Komi's paper.


### Paper 2 - Loads on the Body
Ever wondered how many loads are placed on the shoulder while lifting a cup? Check out this [research paper](https://www.sciencedirect.com/science/article/abs/pii/S0021929009003169).
Let's simulate a shoulder movement as a quick demonstration.

### Paper 3 - Bone Deformities
Explore bone deformities in this [research paper](https://www.sciencedirect.com/science/article/abs/pii/S0966636223010044).
Now, let's proceed with a quick demonstration.


## 1.2 What is an MSK Skeletal Model? Open your first model (30 min)

- Open the folder "Hello_world_of_simulations"
- Open OpenSim
- Load model 
- Let's go through the different components step by step
- Show the different commands and tools
- Preview experimetnal data (markers and grf)

![Alt text](.\Snippets\24.8_job_not_finished.png) 

### Questions:
- What are the components of a model?
- How can a model be edited? (GUI, text editor, scripting)
- How many bodies does this model have?
- How many muscles does this model have in each leg?
- What is the maximum isometric force of recfem?
- How many dof hip and knee joint have?
- How heavy is the tibia segment?
- Load experimetal trc. Why are the markers doing a moon walk?


## 1.3 Getting to know the files and plotting tool (30 min)
- Open the files 
- Ensure everyone can open .trc, .mot, .xml files (test everyone's software)
- For those who cannot, we will provide assistance during a break

![Alt text](.\Snippets\24.8_job_not_finished.png) 

### Questions:
- 
- What is the max moment arm of psoas during hip flexion?
- Why are moment arms negative?
- Plot the mtu lenght of the Psoas during hip flexion. Explain the figure.

## ------------- 10 min Break ------------- 

## 1.4 Run all the steps of the simulation Gait2392 (60 min)
- Run scale tool
- Inverse kinematics tool
- Inverse dynamics tool
- Static optimization
- Analyze tool
- Plot simulation results for each step

![Alt text](.\Snippets\1.4.1mtu_length_hams_walking.png) 

![Alt text](.\Snippets\24.8_job_not_finished.png) 

### Questions
- What are the peak hip, knee, and ankle angles?
- what are the peak joint moments?
- What are the RF forces and activation?
- How many body weights does the model output during the JRA for the vertical compontent of hip contact loads?


# Summary and questions

# --------------------------------------- 
#               Day 2            
# ---------------------------------------  

# 2. The importance of scalling and marker registration (3h)

## 2.0 Add markers to the model

## 2.1 Scaling, Inverse kinematics (1h)
- Theory
    https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+Scaling+Works
    https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+Inverse+Kinematics+Works
- Load the model
- Open the setup file
- Attempt scaling with incorrect settings
- Show how to adjust and apply proper scaling settings

- Scale the same model with two different sets of weights (1000 vs 500 vs 1 for anatomical landmarks)
    1. Load C:\Git\BIP_OpenSim_Hungarian_USports\ExampleData\Sprinting\009\  ( make sure model is called Rajagopal_with_deep_hip_muscles)
    2. Change the weights and save new setup file
    3. Run Scale tool
    4. Overlay experimental markers (right click "subject01 -> Motions -> static pose")
    5. Load subject01_Setup_IK.xml and run IK tool
    6. Assess marker errors
    7. Repeat with different weights 

    Note: Right click the models to show/hide, change offset,... 

### 2.1.1 Questions 
- How do marker weights change scale factors?
- What are, approximately, total, RMS, and maximum marker errors?
- Plot hip, knee, and ankle angles
- What is the peak hip flexion angle during sprinting?
- What is the peak knee flexion angle during sprinting?
- What is the peak ankle plantarflexion angle during sprinting?
- How can you increase the trust on your results?

## 2.2 Register markers (30 min)
- Create a new model with all the markers set to not "fixed" (Tip: use the replace function in the tex editor)
- Save model
- Load the new model and run scale
- Run inverse kinematics

### 2.2.1 Questions
- What happened to the marker errors during scalling?
- Compare hip, knee, and ankle angles between the two models.
- Describe what happened to each joint angle. 

![Alt text](\Snippets\2.2.2_fixed_vs_not_fixed.png)

## ------------- 10 min Break ------------- 

## 2.3 Visualize GRF and set up .xml file (10 min)
- Associate motion data "subject01_walk1_grf.mot"
- Check if the force vecotrs are syncronized with motion (if there is a delay or offset, restart opensim)
- run inverse dynamics tool 
- plot right and left ankle moments

### 2.3.1 Questions 
- What are the peak plantar flexion moment?
- Why is the left ankle moment so much smaller compared with right?

![Alt text](\Snippets\2.3.1_wrong_grf_application.png)

## 2.4 Apply GRF to correct bodies (30 min)
- Load the setup_ID.xml
- Change the point of application of the forces
- run inverse dynamics tool

### 2.4.1 Questions 
- Compare hip, knee, and ankle moments
- How did moments change during stance?
- How did moments change during swing?

![Alt text](\Snippets\2.3.1_correct_grf_application.png)

## 2.5 Residual reduction analysis (45 min)
- Theory about RRA 
    https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+RRA+Works 
- Load .\Run_baseline\setup_RRA.xml and run RRATool
- Plot results for pelvis moments from .\Run_baseline\inverse_dynamics.sto
- Plot results for pelvis moments from .\Run_baseline\RRA\_Actuation_force.sto

![Alt text](\Snippets\2.4.1_id_residuals.png)

![Alt text](\Snippets\2.4.1_optimal_residuals.png)

Note: the presnet residuals are recomendations for walking, during running residuals are expected to be higher.

![Alt text](\Snippets\2.4.1_rra_residuals.png)

### 2.4.1 Questions 
- What changes in the trunk segment properties?
- What changed more hip flexion or trunk extension angles?
- How did the residual moments change after RRA?
- Are the residual moments acceptable? 






# --------------------------------------- 
#               Day 3            
# ---------------------------------------  

# 3. Muscle and joint contact forces (3h)

## Theory (15 min)
https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+Static+Optimization+Works


## 3.1 Calculate muscle forces during sprinting (60 min)
- Load rra adjusted model 
- Run SO tool
- Plot muscle forces and muscle activations (bflh_r and gaslat_r)

### Questions
- What is the main difference between the actuator.xml files from RRA and SO?
- What are peak force of biceps femoris and soleus muscles?
- How do the muscle activations look?
- What are the errors that show up on the messages window?
- Double the maximum isometric force of all muscles and re-run the simulations. What changed?


![Alt text](\Snippets\3.1.1_muscle_activations.png)

![Alt text](\Snippets\3.1.1_muscle_activations_large_actuators_250.png)

![Alt text](\Snippets\3.1.1_researves_large_actuators_250.png)

![Alt text](\Snippets\)

![Alt text](\Snippets\)


## ------------- 10 min Break ------------- 

## 3.3 Calculate joint reaction loads (30 min)
- Load rra ajudsted model 
- Open Analyze tool and run setup_Analyze.xml
- Plot the three components of hip contact force

### 3.3.1 Questions
- 

## 3.4 Explore muscle analysis (45 min)
- plot moment arms (all the hip muscles)
- plot muscle-tendon lengths (all the hip muscles)
- Increase the radius of wrapping surface of Gmax1_r to 0.055 and plot results again
- Do the same for one knee muscle

### 3.4.1 Questions
- Are there any muscle moment arm dicontinuities?
- What is the hip muscle with longest length during sprinting?
- 

## 3.5 Summary 


# --------------------------------------- 
#               Day 4           
# ---------------------------------------  

# 4. Practical examples (3h)

## 4.1 Bone deformities (45 min)

Protocol described here: https://www.sciencedirect.com/science/article/abs/pii/S0966636223010044 

- For each participant follow these steps
- Load torsion model (Bone_deformities\P01\pre\Torsion_model_generic.osim)
- Load scaled model for each participant (Bone_deformities\P01\pre\Static03\Setup_Scale.xml)
- Plot moment arms Glutes and change wrapping surfaces
- Run IK, ID, SO, and JRA for both participants (one trial)
- Plot kinematics, moments, muscle forces (recfem, gmax1, psoas)
- Plot hip contact forces

### Questions
- How do subjects differ in kinematics
- How were moments arms affected by the torsion



## 4.2 Compare muscle forces before and after maximal repeated sprints (45 min)

Protocol described here: https://www.sciencedirect.com/science/article/abs/pii/S1440244021000608 

- Load scaled model 
- Run IK, ID, RRA, and SO for trial Run_post_fatigue (use the RRA adjusted model)
- Plot muscle forces and muscle activations (bflh_r and gaslat_r)

### Questions
- What are peak force of biceps femoris and soleus muscles?



## 4.3 Simulation and Analysis of a Tendon Transfer Surgery (45 min)

Protocol described here: https://simtk-confluence.stanford.edu:8443/pages/viewpage.action?pageId=92110947 

### Questions




# --------------------------------------- 
#               Day 5           
# ---------------------------------------  

# 5. Future directions and questions (3h) 

## Scripting commands 

run a simple setup file from cmd 
```
opensim-cmd run-tool \path\to\xmlFile\arm26_Setup_InverseKinematics.xml
```

