import pymel.core as pm

selection = pm.ls(sl=True)
pm.joint(selection, e=True, ch=True, oj='xyz')
