# BIP OpenSim

Basilio Goncalves - basilio.goncalves@univie.ac.at
Hans Kainz - hans.kainz@univie.ac.at

![Alt text](.\Presentation\Snippets\1.0.2_NRG.png) 
![Alt text](.\Presentation\Snippets\1.0.2_UniVie.png)

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

# --------------------------------------- 
#               Day 1            
# ---------------------------------------  

# 1. Intro - 3h (start at 14h00)

## 1.1 Quick examples based on presentations (20 min - 14h10)

https://www.sciencedirect.com/science/article/abs/pii/S0278591920305068
hnttps://www.sciencedirect.com/science/article/abs/pii/S0021929009003169
https://www.sciencedirect.com/science/article/abs/pii/S0966636223010044


## 1.2 What is an MSK Skeletal Model? Open your first model (30 min - 14h30)

- Open the folder "Hello_world_of_simulations"
- Open OpenSim
- Load model "gait2392_simbody.osim"
- Let's go through the different components step by step
- Explore the different commands and tools
- Use the tool "Preview Experimetnal Data" to view marker and grf 
    - subject01_walk1.trc
    - subject01_walk1.trc

![Alt text](.\Presentation\Snippets\1.1.2_preview_data.png) 

### Questions:
- What are the components of a model?
- How can a model be edited? (GUI, text editor, scripting)
- How many bodies does this model have?
- How many muscles does this model have in each leg?
- What is the maximum isometric force of rect_fem_r?
- How many dof hip and knee joint have?
- How heavy is the tibia segment?
- Load experimental markers. Why are the markers doing a moon walk?
- Load experimental GRF. Why are the forces not below the feet markers? Make them alignned


## 1.3 Getting to know the files and plotting tool (30 min - 15h00)
- Open the files in their respective software:
    - Use Mokka for .c3d files
    - Use excel for .trc, .mot, .sto 
    - Use NotePad++ for .xml
    - Use OpenSim for .osim
- For those who cannot, we will provide assistance during a break


### Questions:
- What is the maximum moment arm of psoas during hip_flexion_r?
- Why are moment arms negative?
- Plot the mtu length of the psoas_r during hip_flexion_r. Explain the figure.
- Plot mtu length of lat_gas_r and bflh_r during hip flexion. Why are they so different?
- Plot active, passive, and total-fiber force. 

## ------------- 10 min Break ------------- (15h30)

## 1.4 Run all the steps of the simulation Gait2392 (60 min - 15h40)
- Run scale tool (subject01_Setup_Scale.xml)
- Inverse kinematics tool (subject01_Setup_Scale.xml)
- Inverse dynamics tool (subject01_Setup_Scale.xml)
- Static optimization (subject01_Setup_Scale.xml)
- Analyze tool (subject01_Setup_Analyze.xml)
- Plot simulation results for each step (load the results files first)


![Alt text](.\Presentation\Snippets\1.4.1mtu_length_hams_walking.png) 

### Questions
- What are the range of marker errors during the inverse kinematics step?
- What are the peak hip, knee, and ankle angles?
- what are the peak sagittal joint moments hip, knee, and ankle?
- What are the lat_gas and rect_fem peak forces and activation?
- What are the mtu lengths for bflh_r and soleus_r. 
- What are the maximum reserves moments hip_flexion_r, hip_adduction_r,	hip_rotation_r,	knee_angle_r,	ankle_angle_r
- What is the peak vertical component of hip contact loads, relative to participants body weight?


# Summary and questions (16h40)

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
    "Tutorials\Sprinting\009\session1\"
    model name "Rajagopal_generic.osim"
- Run the scale tool using "setup_Scale_1.xml"
- Show how to adjust and apply proper scaling settings
- Go throught the problems with the scalling
    Marker errors
    Marker weights
    How to se

- Scale the same model with two different sets of weights (1000 vs 500 vs 1 for anatomical landmarks)
    1. Load the model "Tutorials\Sprinting\009\session1\Rajagopal_generic.osim"
    2. Change the weights and save new setup file
    3. Run Scale tool
    4. Overlay experimental markers (right click "subject01 -> Motions -> static pose")
    5. Load subject01_Setup_IK.xml and run IK tool
    6. Assess marker errors
    7. Repeat with different weights 

    Note: Right click the models to show/hide, change offset, etc... 

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

![Alt text](.\Presentation\Snippets\2.2.2_fixed_vs_not_fixed.png)

## ------------- 10 min Break ------------- 

## 2.3 Visualize GRF and set up .xml file (10 min)
- Associate motion data "subject01_walk1_grf.mot"
- Check if the force vecotrs are syncronized with motion (if there is a delay or offset, restart opensim)
- run inverse dynamics tool 
- plot right and left ankle moments

### 2.3.1 Questions 
- What are the peak plantar flexion moment?
- Why is the left ankle moment so much smaller compared with right?

![Alt text](.\Presentation\Snippets\2.3.1_wrong_grf_application.png)

## 2.4 Apply GRF to correct bodies (30 min)
- Load the setup_ID.xml
- Change the point of application of the forces
- run inverse dynamics tool

### 2.4.1 Questions 
- Compare hip, knee, and ankle moments
- How did moments change during stance?
- How did moments change during swing?

![Alt text](.\Presentation\Snippets\2.3.1_correct_grf_application.png)

## 2.5 Residual reduction analysis (45 min)
- Theory about RRA 
    https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+RRA+Works 
- Load .\Run_baseline\setup_RRA.xml and run RRATool
- Plot results for pelvis moments from .\Run_baseline\inverse_dynamics.sto
- Plot results for pelvis moments from .\Run_baseline\RRA\_Actuation_force.sto

![Alt text](.\Presentation\Snippets\2.4.1_id_residuals.png)

![Alt text](.\Presentation\Snippets\2.4.1_optimal_residuals.png)

Note: the presnet residuals are recomendations for walking, during running residuals are expected to be higher.

![Alt text](.\Presentation\Snippets\2.4.1_rra_residuals.png)

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


![Alt text](.\Presentation\Snippets\3.1.1_muscle_activations.png)

![Alt text](.\Presentation\Snippets\3.1.1_muscle_activations_large_actuators_250.png)

![Alt text](.\Presentation\Snippets\3.1.1_researves_large_actuators_250.png)


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
- How did the MTU length of the rect_fem_r change?

# --------------------------------------- 
#               Day 5           
# ---------------------------------------  

# 5. Future directions and questions (3h) 

## Scripting commands 

run a simple setup file from cmd 
```
opensim-cmd run-tool \path\to\xmlFile\arm26_Setup_InverseKinematics.xml
```


