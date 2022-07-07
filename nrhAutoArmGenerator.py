# ik/fk arm auto rig v002
# Nate Hancock

import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
import math

# import importlib
# import armAutorigv002
# importlib.reload(armAutorigv002)

print("Initializing...")




debug = False
class armRig:
    print("Class call successful")

    def __init__(self, namespace=None):
        if namespace!=None:
            self.namespace=namespace+':'
        else:
            self.namespace=None


        self.window = None
        self.windowsName = ('armrig_UI')
        self.title = ('arm auto rigger')

        UI_created = self.create_arm_ui()
        print ('call UI')

    def create_arm_ui(self):

        if pm.window(self.windowsName, ex=True):
            pm.deleteUI(self.windowsName)

        window = cmds.window(self.windowsName, mm=True, bgc=(0.0, 0.1, 0.1))
        cmds.rowColumnLayout(nc=2)
        global asymmetrical_checked
        asymmetrical_checked = pm.checkBox(value=False, label='Asymmetrical Placement')
        global symmetrical_checked
        symmetrical_checked = pm.checkBox(value=False, label='Symmetrical Placement')

        # if pm.checkBox(symmetrical_checked, query=True, value=True):
        #     pm.checkBox(asymmetrical_checked, value=False)
        # if pm.checkBox(asymmetrical_checked, query=True, value=True):
        #     pm.checkBox(symmetrical_checked, value=False)

        cmds.columnLayout('Main', cal='left')
        global locator_created
        locator_created= cmds.button(w=300, ebg=True, bgc=(0, 0, 0), l='Create Locators for Arm Joint Placement', c=self.create_arm_locators)
        cmds.button(w=300, ebg=True, bgc=(0, 0, 0), l='Create Joints Based on Generated Locators', c=lambda *args: self.create_joints_on_locators(arm_position_locator))
        cmds.button(w=300, ebg=True, bgc=(0, 0, 0), l='Create Joints Based on Selections')

        print(locator_created)
        cmds.showWindow(self.windowsName)

        return (locator_created)
    # clean up an object
    def nrh_cleanup(self, obj):
        # delete object history
        deleteHistory = cmds.delete(constructionHistory=True)
        # freeze objects transforms
        freezeTransforms = cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        # center pivot
        sel = cmds.ls(selection=True)
        for obj in sel:
            cmds.xform(obj, centerPivots=True)

    def checkbox_evalutaion(self):
        global asymmetrical_checked
        global symmetrical_checked
        asym_check = pm.checkBox(asymmetrical_checked, query=True, value=True)
        sym_check = pm.checkBox(symmetrical_checked, query=True, value=True)

        if asym_check:
            print('You have checked the Asymmetrical option')
        elif sym_check:
            print('You have checked the Symmetrical option')
        '''Will add an else that automatically makes the system mirrored if nothing is checked at the start'''

    '''start off by creating 4 locators that are parented to a locators
    these locators will be for placing joints and will replaced with joints
    create joints on locators in order clavicle, shoulder, elbow, wrist'''
    def create_arm_locators(self, *args):
        """Function that create locators necessary to for the placement of the arm joints"""
        # count = 1

        # create locators
        clavicleLoc = pm.spaceLocator(name='clavicleLoc', p=(0, 0, 0))
        # clavicleLoc = pm.sphere(n='clavicleLoc', p=(0,0,0), polygon=0)
        '''will create a lambet and set to yellow and assign to nurbs spheres'''
        # self.nrh_cleanup(clavicleLoc)
        clavicleLoc_group = pm.group(clavicleLoc, n='clavicle_Loc_Grp')
        shoulderLoc = pm.spaceLocator(name='shoulder_Loc', p=(2, 0, -0.5))
        # shoulderLoc = pm.sphere(name='shoulder_Loc', p=(2, 0, -0.5), polygon=0)
        # self.nrh_cleanup(shoulderLoc)
        shoulderLoc_group = pm.group(n='shoulder_Loc_Grp')
        parent_shoulderGrp_clavGrp = pm.parent(shoulderLoc_group, clavicleLoc_group)
        elbowLoc = pm.spaceLocator(name='elbow_Loc', p=(5, 0, -1.5))
        # elbowLoc = pm.sphere(name='elbow_Loc', p=(5, 0, -1.5), polygon=0)
        # self.nrh_cleanup(elbowLoc)
        wristLoc = pm.spaceLocator(name='wrist_Loc', p=(9, 0, -0.5))
        # wristLoc = pm.sphere(name='wrist_Loc', p=(9, 0, -0.5), polygon=0)
        # self.nrh_cleanup(wristLoc)

        parent_wrist_shoulderGrp = pm.parent(wristLoc, shoulderLoc_group)
        parent_elbow_shoulderGrp = pm.parent(elbowLoc, shoulderLoc_group)
        # parent_shoulder_shoulderGrp = pm.parent(shoulderLoc, shoulderLoc_group)
        # parent_shoulderGrp_clavGrp = pm.parent(shoulderLoc_group, clavicleLoc_group)

        pm.ls(selection=False)

        pm.xform(clavicleLoc_group, relative= True, translation=(3.188069, 28.0, 0.0))
#         pm.xform(elbowLoc, relative=True, translation=(0, -1.5, 0.0))
#         pm.xform(wristLoc, relative=True, translation=(0, -3.0, 0.0))
        # pm.xform(shoulderLoc_group, relative= True, rotation=(0.0, 0.0, -35.0))

        # nrhCleanup(clavicleLoc_group)

        '''create a list of variables to grab and replace with joints'''

        global arm_position_locator
        arm_position_locator = (clavicleLoc, shoulderLoc_group, shoulderLoc, elbowLoc, wristLoc)

        '''testing a way to get the value of the check box in the UI'''
        # global locator_created
        # for asymmetrical_checked in locator_created:
        #     if pm.checkBox(asymmetrical_checked,query=True, value=True):
        #         print('You have checked the Asymmetrical option')

        self.checkbox_evalutaion()
        # leftArm_locators = create_arm_locators()
        print('Left arm locators created')

        return arm_position_locator

    '''will eventually want to have the locators different colors as to help differentiate sides and which limb
    is being laid out add in modularity so if mesh  is not symmetrical they can pose and replace both sides with
    locators or if symmetrical then the can simple have it build for them automatically'''

    def create_joints_on_locators(self, item):
        print ('Initiate Joint swap')
        position_output = []
        joint_list = []

        '''getting the point position data of the things in the list and pinning their position in space'''
        for i in item:
            items = pm.pointPosition(i, world=True)
            print ('item added to position outputs')
            position_output.append(items)

            print(position_output)

        pm.delete(item)

        '''for the things in position_output create joints based on their location'''
        for j in position_output:
            test_joints = pm.joint(name='', position=j, absolute=True)
            print ('item added to joint list')
            # pm.parent(world=True)
            joint_list.append(test_joints)

            # '''will need to rename arm joints in series (joints : 'clav', 'clav end', 'shoulder', 'elbow', 'arm end')'''
            # '''May move this to a seperate function altogether, especially since loop causes count issue'''
            # count = 0
            # name = 'arm'
            # suffix = 'Jnt'
            # prefix = 'L'
            #
            # for names in test_joints:
            #     # print(test_joints)
            #     new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, suffix, count)
            #     pm.rename(test_joints, new_name)
            #     count += 1

        pm.select(cl=True)
        print (item)

        '''takes the 3 joint in the chain (the shoulder in this case) and orients joints and sets secondary axis'''
        # pm.parent(joint_list[2], world=True)
        pm.joint(joint_list[2], e=True, ch=True, oj='xyz', secondaryAxisOrient='yup')

        '''Set pref angle for the joints'''

        # pm.rotate(joint_list[2], 0, 45, 0, r=1, os=1, fo=1)
        # pm.joint(joint_list[2], edit=True, children=True, setPreferredAngles=True)
        # pm.rotate(joint_list[2], 0, -45, 0, r=1, os=1, fo=1)


        # pm.rotate(joint_list[3], 0, -45, 0, r=1, os=1, fo=1)
        # pm.joint(joint_list[3], edit=True, children=True, setPreferredAngles=True)
        # pm.rotate(joint_list[3], 0, 45, 0, r=1, os=1, fo=1)

        '''create a single chain ik handle for clavicle
        then create 2 more joint chain off the new joints with IK and FK names instead on Jnt
        parent these new joints to the main arm joint system (shoulder, elbow, wrist)'''

        # pm.delete('clavicle_Loc_Grp')

        clav_jnt = pm.rename(joint_list[0], 'L_clavicle_Jnt')
        clav_end = pm.rename(joint_list[1], 'L_clavicle_End')

        '''Creates the clavicle IK'''
        clavicle_Ik = pm.ikHandle(sj=joint_list[0], ee=joint_list[1], name='clav_IK', sol='ikSCsolver', autoPriority=True)

        shoulder_jnt = pm.rename(joint_list[2], 'L_shoulder_Jnt')
        elbow_jnt = pm.rename(joint_list[3], 'L_elbow_Jnt')
        wrist_jnt = pm.rename(joint_list[4], 'L_wrist_Jnt')

        ikarm_grp = []
        fkarm_grp = []

        clavJnt_grp = pm.group(joint_list[0], name='Clav_Jnt_Grp')
        shoulderJnt_grp = pm.group(joint_list[2], name='Arm_Joints_Grp')

        ikshoulder = ikarm_grp.append(pm.duplicate(joint_list[2], parentOnly=True, name='shoulder_ik'))
        ikelbow = ikarm_grp.append(pm.duplicate(joint_list[3], parentOnly=True, name='elbow_ik'))
        ikwrist = ikarm_grp.append(pm.duplicate(joint_list[4], parentOnly=True, name='wrist_ik'))

        pm.parent(ikarm_grp[2], ikarm_grp[1])
        pm.parent(ikarm_grp[1], ikarm_grp[0])

        fkshoulder = fkarm_grp.append(pm.duplicate(joint_list[2], parentOnly=True, name='shoulder_fk'))
        fkelbow = fkarm_grp.append(pm.duplicate(joint_list[3], parentOnly=True, name='elbow_fk'))
        fkwrist = fkarm_grp.append(pm.duplicate(joint_list[4], parentOnly=True, name='wrist_fk'))

        pm.parent(fkarm_grp[2], fkarm_grp[1])
        pm.parent(fkarm_grp[1], fkarm_grp[0])
        pm.parent(shoulderJnt_grp, clav_end)

        '''create the arm Ik'''
        l_armIk = pm.ikHandle(sj='shoulder_ik', ee='wrist_ik', name='L_arm_IK', sol='ikRPsolver',
                                  autoPriority=True)

        left_poleVectorCtrl = pm.circle(name='l_arm_pv_Ctrl', c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))
        cvSelection = pm.select('l_arm_pv_Ctrl.cv[2]','l_arm_pv_Ctrl.cv[0]', 'l_arm_pv_Ctrl.cv[6]', 'l_arm_pv_Ctrl.cv[4]')
        cmds.scale(0.0411462, 0.0411462, 0.0411462, ocp=1, r=1)
        pm.select(left_poleVectorCtrl)
        cmds.rotate(90, 0, 0, r=1, os=1, fo=1)
        # freeze objects transforms
        freezeTransforms = cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        # delete object history
        deleteHistory = cmds.delete(constructionHistory=True)

        created_grp = pm.group(name='l_arm_pv_ctrl_grp')
        proxy_constraint = pm.parentConstraint('elbow_ik', 'l_arm_pv_Ctrl', mo=False)
        pm.delete(proxy_constraint)
        pm.xform(t=(0,0,-10))

        # freeze objects transforms
        freezeTransforms = cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        # delete object history
        deleteHistory = cmds.delete(constructionHistory=True)
        cmds.xform('l_arm_pv_ctrl_grp', centerPivots=True)
        pm.select(cl=True)
        
        

        # pm.poleVectorConstraint('l_arm_pv_Ctrl', 'L_arm_IK')


        return (joint_list, ikarm_grp, fkarm_grp)

    # pose test

run_arm_class = armRig()
