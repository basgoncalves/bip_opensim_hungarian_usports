# BIP OpenSim

![Alt text](.\Snippets\1.0.2_NRG.png) ![Alt text](\Snippets\1.0.2_UniVie.png)

## Required Software
- OpenSim (version 4.4 preferable)
- Mokka 
- Windows OS (tutorial works for Mac with minor adjustments)

useful tutorials:
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/Tutorial+1+-+Intro+to+Musculoskeletal+Modeling
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/Workshops+and+Events
- https://simtk-confluence.stanford.edu:8443/display/OpenSim/ESMAC+Workshop+September+2022

useful tools:
- VSCode or other IDE

## Check the cheat_sheet.pdf for detailed information on terminology used throughout
- Bodies
- Actuators
- Probes
- Markers

# 1. Intro - 3h

## Quick examples based on presentations (15 min)

For years, we've been fascinated with measuring muscle and joint loads. 

### Paper 1 - Komi 1982

Let's start by simulating running quickly and examining tendon forces. Later, we'll compare our findings with those presented in Komi's paper.

### Paper 2 - Loads on the Body

Ever wondered how many loads are placed on the shoulder while lifting a cup? Check out this [research paper](https://www.sciencedirect.com/science/article/abs/pii/S0021929009003169).
Let's simulate a shoulder movement as a quick demonstration.

### Paper 3 - Bone Deformities

Explore bone deformities in this [research paper](https://www.sciencedirect.com/science/article/abs/pii/S0966636223010044).
Now, let's proceed with a quick demonstration.


## What is an MSK Skeletal Model? Open your first model (30 min)

- Open OpenSim
- Load the model ('C:\')
- Let's go through the different components step by step
- Show the different commands and tools

### Questions:
- What are the components of a model?
- How can a model be edited? (GUI, text editor, scripting)
- 

## Bad example tutorial (30 min)
- Data from walking compared with invivo results 

## ------------- 10 min Break ------------- 

## Getting to know the files and olotting tool (30 min)
- Open the folder
- Ensure everyone can open .trc, .mot, .xml files (test everyone's software)
- For those who can't, we'll provide assistance during a break

## Run all the steps of the simulation Gait2

- 
- Plot of right hip, knee, ankle sagittal angles.
- Plot 

### Questions
- What is the peak hip flexion, hip


# 2. The importance of scalling and marker registration (3h)

## 2.1 Scaling, Inverse kinematics (1h)
- Theory
    https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+Scaling+Works
    https://simtk-confluence.stanford.edu:8443/display/OpenSim/How+Inverse+Kinematics+Works
- Load the model
- Open the setup file
- Attempt scaling with incorrect settings
- Show how to adjust and apply proper scaling settings

- Scale the same model with two different sets of weights (1000 vs 500 vs 1 for anatomical landmarks)
    1. Load subject01_Setup_Scale.xml 
    2. Change the weights and save new setup file
    3. Run Scale tool
    4. Overlay experimental markers (right click "subject01 -> Motions -> static pose")
    5. Load subject01_Setup_IK.xml and run IK tool
    6. Assess marker errors
    7. Repeat with different weights 

    Note: Right click the models to show/hide, change offset,... 

### Questions 
- How do marker weights change scale factors?
- What are, approximately, total, RMS, and maximum marker errors?
- Plot hip, knee, and ankle angles
- What is the peak hip flexion angle during walking?
- What is the peak knee flexion angle during walking?
- What is the peak knee flexion angle during walking?


## 2.2 Register markers (30 min)
- Add markerset to the osim model in the xml
- Create a new model with all the markers set to "fixed" (Tip: use the replace function in the tex editor)
- Save model as "gait2392_simbody_withMarkerSet.osim"
- Load the new model and run scale (untick "Add markerset from files")
- Run inverse kinematics

### Questions
- What happened to the marker errors during scalling?
- Compare hip, knee, and ankle angles between the two models.
- Describe what happened to each joint angle. 

![Alt text](\Snippets\2.2.2_fixed_vs_not_fixed.png)

## ------------- 10 min Break ------------- 

## Visualize GRF and set up .xml file (10 min)
- Associate motion data "subject01_walk1_grf.mot"
- Check if the force vecotrs are syncronized with motion (if there is a delay or offset, restart opensim)
- run inverse dynamics tool 
- plot hip, knee, and ankle sagittal moments

### Questions 
- What are the peak hip extension, knee extension, and ankle plantar flexor moments?

## Apply GRF to different bodies (30 min)
- Load the setup_ID.xml
- Change the point of application of the forces
- run inverse dynamics tool

### Questions 
- Compare hip, knee, and ankle moments
- How did moments change during stance?
- How did moments change during swing?

# 3. Muscle and joint contact forces 

## 

### Questions
- What is the difference between CMC and Static Optimization?


# Tutorial OpenSim Gait2392 Model Tutorial 

## Introduction

Welcome to the OpenSim Gait2392 Model tutorial. In this tutorial, you will learn how to work with the Gait2392 model in OpenSim to analyze and simulate human gait. The Gait2392 model is a widely used biomechanical model for studying human walking.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- [OpenSim](https://opensim.stanford.edu/)
- [Gait2392 Model](https://simtk.org/projects/gait2392)

## Getting Started

### Step 1: Download the Gait2392 Model

You can download the Gait2392 model from the [official OpenSim website](https://simtk.org/projects/gait2392). Follow the instructions provided to download and install the model.

### Step 2: Import Gait2392 Model into OpenSim

Once you have downloaded and installed the Gait2392 model, launch OpenSim and import the model into your workspace.

```python
# Sample code for importing the Gait2392 model in OpenSim
import opensim

gait2392_model = opensim.Model('path/to/gait2392.osim')
```

## Step 3: Explore Model Components

Explore the various components of the Gait2392 model, such as the musculoskeletal structure, joints, muscles, and markers. Familiarize yourself with the model's anatomy and properties.

## Simulating Gait

### Step 4: Set Up a Gait Simulation

To simulate human gait using the Gait2392 model, you need to define a simulation setup. This includes specifying initial conditions, forces, and controllers.

### Step 5: Run the Simulation

Execute the gait simulation in OpenSim.

```python
# Sample code for running a gait simulation
simulator = opensim.Simulator(gait2392_model)
simulator.setInitialTime(0.0)
simulator.setFinalTime(1.0)
simulator.integrate()
```

## Step 6: Analyze Simulation Results

Once the simulation has completed, it's time to analyze the results. OpenSim provides various tools and libraries for post-processing and visualization. You can use Python or OpenSim's built-in tools to analyze the data generated during the simulation.

Here are some common analyses you can perform:

- **Inverse Kinematics**: Estimate joint angles and movements throughout the gait cycle to understand how the model's joints behave.

- **Muscle Analysis**: Examine muscle and tendon kinematics and muscle moment arms.

- **Static Optimization**: Estimate of individual muscle forces from .

- **Joint Reaction Analysis**: Estimate net joint forces resulting from the sum of muscle and intergmental forces.

- **Energy Expenditure**: Calculate the energy expenditure of the model during the simulation to gain insights into the metabolic cost of gait.

Remember to document your findings and visualize the results to present your analysis effectively.

## Conclusion

In this tutorial, you've learned how to work with the OpenSim Gait2392 model for simulating and analyzing human gait. You've covered the following key steps:

1. Downloading and importing the Gait2392 model into OpenSim.
2. Exploring the model's components, including the musculoskeletal structure, joints, muscles, and markers.
3. Setting up a gait simulation by defining initial conditions, forces, and controllers.
4. Running the simulation to generate data.
5. Analyzing the simulation results, including joint kinematics, muscle activity, ground reaction forces, and energy consumption.

The Gait2392 model is a valuable resource for biomechanical research, and with the knowledge gained in this tutorial, you can conduct in-depth studies on human gait. Feel free to explore further, experiment with different scenarios, and use the model for your specific research or analysis needs.






# Scripting commands 

run a simple setup file from cmd 
```
opensim-cmd run-tool \path\to\xmlFile\arm26_Setup_InverseKinematics.xml
```



# Questions

## What is an MSK Skeletal Model





## Inverse Kinematics

## Inverse Dynamics 

## Comupted muscle control
- Differences from static optimization?