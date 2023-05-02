import pymel.core as pm

# Get the selected joint chain
joints = pm.ls(selection=True, type='joint')

# Create a curve from the joint positions
positions = [joint.getTranslation(space='world') for joint in joints]
curve = pm.curve(degree=1, point=positions)

# Rename the curve and move it to the same group as the joint chain
curve.rename(joints[0].name().replace('_jnt', '_crv'))
curve.setParent(joints[0].getParent())

print('Curve created: {}'.format(curve.name()))
