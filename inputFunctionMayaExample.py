#simple example of getting an input from the user and using it to modify steps in a function
#basically showing how to use a input function 

import pymel.core as pm 
import maya.cmds as cmds 
import maya.mel as mel

#ask for the users name
result = cmds.promptDialog(
                title='Namet',
                message='Please Enter Your Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')
#if ok is clicked store the inputas names
if result == 'OK':
        names = cmds.promptDialog(query=True, text=True)

titleSuffix = ('the Great') 
#function that take the input which is == userName and formats it in the print statements
def greetingWithName(userName, title):
    print ('Greetings {0} {1}'.format(userName, titleSuffix))
    print ('Nice to meet you {0}'.format(userName))

#we call the function and use the variable "names" to essentially modify the parts of the function: 'userName'
#and the second part with the title   
greetingWithName(names, titleSuffix)
