import pymel.core as pm 
import maya.cmds as cmds
from pymel.core import *
import pymel.core.datatypes as dt

def locators_created():
    
    test_locator_one = pm.spaceLocator(name= 'Test 01')
    pm.xform(test_locator_one, t = (2, 5, 0))
    pm.select(cl= True)
    
    test_locator_two = pm.spaceLocator(name= 'Test 02')
    pm.xform(test_locator_two, t = (3, 4, 0))
    pm.select(cl= True)
    
    test_locator_three = pm.spaceLocator(name= 'Test 03')
    pm.xform(test_locator_three, t = (4, 3, 0))
    pm.select(cl= True)
    
    test_locators = (test_locator_one, test_locator_two, test_locator_three)
    locator_grp = pm.group(test_locators, name='locator_Grp')
    
    position_output= []
    
    for i in test_locators:
        items = pm.pointPosition(i, world=True)
        #print (items)
        position_output.append(items)
        
    
    
    return (position_output)
   
created_locators = locators_created()
print (created_locators)

def create_joints_on_locators(item):    
    for items in item:
        test_joints = pm.joint(position = item)
        print (test_joints)
        return test_joints

joint_replace_locators = create_joints_on_locators(created_locators)

def rename_created_joints(joints):
    print (joints)
    count = 0
    name = 'test'
    suffix = 'Jnt'
    
    for item in joints:
        new_name = '{0}_{1}_{2}'.format(name, suffix, count)
        pm.rename(joints, new_name)
        
        count += 1
        #pm.delete(items)
    
#rename_joints = rename_created_joints(joint_replace_locators)
