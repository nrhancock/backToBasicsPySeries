'''create a pivot changer on selected control with negation'''
'''by Nate Hancock, 7/20/2022, v001'''

import pymel.core as pm


'''1.select the control you wish to add pivot control on'''
'''2.select the joint you wish to constrain to control system'''
'''3.run script '''
def create_base():
    selections = pm.ls(sl=True)
    base_item = selections[0]
    parent_item = selections[1]

    # pivot_control = pm.circle(name=base_item+'_pivot_control', c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=16, r=1, tol=0.01, nr=(0, 1, 0))

    pivot_control = pm.circle(name=base_item+'_pivot_control', c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0.01, s=16, ch=1)
    pm.xform(pivot_control[0].cv[0::2], s=[3, 3, 3])
    # pm.makeIdentity(pivot_control, apply=True, t=1, r=1, s=1, n=0)

    translation_offset = pm.shadingNode('multiplyDivide', asUtility=1)

    pm.setAttr(translation_offset+".input2Z", -1)
    pm.setAttr(translation_offset+".input2X", -1)
    pm.setAttr(translation_offset+".input2Y", -1)

    empty_transform = pm.group(em=True, n=base_item+'_negate_grp')

    pm.connectAttr(pivot_control[0]+".translate", translation_offset+".input1", f=1)
    pm.parent(pivot_control[0], base_item)
    pm.connectAttr(translation_offset+'.output', empty_transform+'.translate', f=1)

    pm.connectAttr(pivot_control[0]+'.translate', '{0}.{1}'.format(base_item, 'rotatePivot'), f=1)
    pm.parent(empty_transform, pivot_control[0])
    empty_transform.setAttr('visibility', 0)

    # unit_convert= pm.shadingNode('unitConversion', asUtility=1)
    # pm.connectAttr(base_item+'.rotate', unit_convert+'.input', f=1)
    # unit_convert.setAttr('conversionFactor', -1)
    # pm.connectAttr(unit_convert+'.output', pivot_control[0]+'.rotate', f=1)
    # pm.setAttr(pivot_control[0]+'.rotateOrder', 5)

    this_line = pm.parentConstraint(empty_transform, parent_item, mo=True)
    # this_line = pm.pointConstraint(empty_transform, parent_item, mo=True)
    # pm.orientConstraint(selections, empty_transform, mo=True)


create_base()

'''The script will parent constraint the empty transform offset to the second selected 
object, if you want to create the pivot controls without constraining, comment out "this_line"'''
