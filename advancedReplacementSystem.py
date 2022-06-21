import pymel.core as pm
import maya.cmds as cmds
from pymel.core import *
import pymel.core.datatypes as dt


'''My Original format when writing out the outline to get the task to complete'''
# def locators_created():
#     test_locator_one = pm.spaceLocator(name='Test 01')
#     pm.xform(test_locator_one, t=(2, 5, 0))
#     pm.select(cl=True)
#
#     test_locator_two = pm.spaceLocator(name='Test 02')
#     pm.xform(test_locator_two, t=(3, 4, 0))
#     pm.select(cl=True)
#
#     test_locator_three = pm.spaceLocator(name='Test 03')
#     pm.xform(test_locator_three, t=(4, 3, 0))
#     pm.select(cl=True)
#
#     test_locators = (test_locator_one, test_locator_two, test_locator_three)
#     pm.group(test_locators, name='locator_Grp')
#
#     for i in test_locators:
#         position_output = pm.pointPosition(i, world=True)
#         # print (position_output)
#
#     return (position_output)
#
#    '''moved to the create_joints_on_locators function because it cause the data types to change
#     coming from outside the function and adding those items to a list plus i needed the commands to execute one after
#     another for each item so it didnt make sense to pull from outside since i can just convert each item in the list as it goes through.'''
#      position_output = []
#
#      for i in test_locators:
#         items = pm.pointPosition(i, world=True)
#         # print (items)
#         position_output.append(items)
#
# created_locators = locators_created()
#
#
# # print (created_locators)
#
# def create_joints_on_locators(item):
#     print(item)
#     count = 1
#     name = 'test'
#     suffix = 'Jnt'
#
#     for items in item:
#         test_joints = pm.joint(position=item)
#     print(test_joints)
#
#     for joints in test_joints:
#         new_name = '{0}_{1}_{2}'.format(name, suffix, count)
#         pm.rename(test_joints, new_name)
#
#         count += 1
#         # pm.delete(items)
#
#      for i in item:
#          position_output = pm.pointPosition(i, world=True)
#
#
# joint_replace_locators = create_joints_on_locators(created_locators)
#
# def rename_created_joints(joints):
#     print(joints)
#     count = 1
#     name = 'test'
#     suffix = 'Jnt'
#
#     for items in joints:
#         count += 1
#         new_name = '{0}_{1}_{2}'.format(name, suffix, count)
#         pm.rename(items, new_name)
#
#
#
#
# rename_joints = rename_created_joints(joint_replace_locators)
#
# def reorient_joints(joints):
#     for k in joints:
#        pm.joint(joints, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='yup')
#
# reorient_joints(joint_replace_locators)

'''My final script after refinement, the locators are more of a example of the item that you would get and then replace
 the joints with, technically this could work for any list created it doesnt have to be these specific locators'''
def locators_created():
    test_locator_one = pm.spaceLocator(name='Test 01')
    pm.xform(test_locator_one, t=(2, 5, 0))
    pm.select(cl=True)

    test_locator_two = pm.spaceLocator(name='Test 02')
    pm.xform(test_locator_two, t=(3, 4, 0))
    pm.select(cl=True)

    test_locator_three = pm.spaceLocator(name='Test 03')
    pm.xform(test_locator_three, t=(4, 3, 0))
    pm.select(cl=True)

    test_locators = (test_locator_one, test_locator_two, test_locator_three)
    # pm.group(test_locators, name='locator_Grp')

    return (test_locators)


created_locators = locators_created()
print(created_locators)


def create_joints_on_locators(item):
    position_output = []
    joint_list = []

    '''getting the point position data of the things in the list and pinning their position in space'''
    for i in item:
        items = pm.pointPosition(i, world=True)
        # print (items)
        position_output.append(items)

        print (position_output)



    '''for the things in position_output create joints based on their location'''
    for j in position_output:
        test_joints = pm.joint(name='', position=j)
        print(test_joints)
        joint_list.append(test_joints)

        count = 0
        name = 'arm'
        suffix = 'Jnt'
        prefix = 'L'

        for names in test_joints:

            # print(test_joints)
            new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, suffix, count)
            pm.rename(test_joints, new_name)
            count += 1

    pm.delete(item)
    pm.select(cl=True)

    for k in joint_list:
        pm.joint(joint_list, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='yup')
        pm.rotate(joint_list,0, -45, 0, r=1, os=1, fo=1)
        pm.joint(joint_list, spa=1, ch=1, e=1)
        pm.rotate(joint_list,0, 45, 0, r=1, os=1, fo=1)

    return (joint_list)

joint_replace_locators = create_joints_on_locators(created_locators)
print (joint_replace_locators)
