

% load opensim comands
import org.opensim.modeling.*

% open osim model
OsimModel = Model(modelpath);

% add components to model
OsimModel.addBody()
OsimModel.addForce()
OsimModel.addJoint()
...