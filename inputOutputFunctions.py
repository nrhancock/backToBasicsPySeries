#example of utilizing functions with outputs 

import pymel.core as pm
import maya.cmds as cmds

def state_and_cities():
    #ask for the users city
    result = cmds.promptDialog(
        title='City name',
        message='Please Enter Your City:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'OK':
        global city
        city = cmds.promptDialog(query=True, text=True)
        
        #ask for the users state
    result = cmds.promptDialog(
        title='State Name',
        message='Please Enter Your State:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'OK':
        global state
        state = cmds.promptDialog(query=True, text=True)
        
    return (city, state)
 
print (state_and_cities())

def combo_function(item1, item2):
    funtionOut =  ('You have entered {0}, {1}, United States.'.format(item1, item2))
    return funtionOut


formatedString_functionOutput = (combo_function(city,state))

print (formatedString_functionOutput)
