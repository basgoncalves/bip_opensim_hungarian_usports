
import opensim 
import subprocess
import os

def run_tool(xmlPath):
    try:
        command = 'opensim-cmd run-tool ' + xmlPath
        os.chdir(os.path.dirname(xmlPath))
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command output:", result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr.decode('utf-8'))

trialPath = r'C:\Users\Bas\Documents\OpenSim\4.4\Models\Gait2392_Simbody'

run_tool(os.path.join(trialPath,'subject01_Setup_Scale.xml')) # Scale
# ... plot

run_tool(os.path.join(trialPath,'subject01_Setup_IK.xml')) # IK
# ... plot

run_tool(os.path.join(trialPath,'subject01_Setup_RRA.xml')) # RRA
# ... plot

run_tool(os.path.join(trialPath,'subject01_Setup_CMC.xml')) # CMC
# ... plot

run_tool(os.path.join(trialPath,'subject01_Setup_Analyze_BG.xml')) # Analyze
# ... plot