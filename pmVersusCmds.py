import pymel.core as pm
import maya.cmds

#names
pymelObject = ('Pymel_Object')
pythonObject = ('PythonCmds_Object')

#variables for the object created using pymel and python cmds respectively
object_one = pm.polySphere(name = pymelObject)
object_two = cmds.polySphere(name = pythonObject)

#please look at the output and take not at the information that is returned to you about the node
print (object_one)
print (object_two)
