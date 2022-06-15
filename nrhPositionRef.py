import pymel.core as pm 
import maya.cmds as cmds 

test_locator = pm.spaceLocator(name= 'Test 01')
pm.xform(test_locator, t = (2, 5, 0))
pm.select(cl= True)

position_output = pm.pointPosition(test_locator)

print (position_output)

test_joint = pm.joint(name = 'Test Jnt', position = position_output)

pm.delete (test_locator)
