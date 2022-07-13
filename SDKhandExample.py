        r_hand_icon = self.create_nrhStar()
        pm.rename(r_hand_icon, 'r_hand_ctrl')

        '''create hand ctrl and switch attr'''
        self.create_hand_attributes(r_hand_icon)

        r_hand_ctrr_offset = pm.group(r_hand_icon, n='r_handCtrr_offset')
        r_trash_parent = pm.parentConstraint('r_wrist_Jnt', 'r_handCtrr_offset', mo=False)
        pm.delete(r_trash_parent)


        pm.move(r_hand_ctrr_offset, 0,2.3,0, r=1, os=1, wd=1)
        pm.parentConstraint('r_wrist_Jnt', r_hand_ctrr_offset, mo=True)
        # pm.xform(r_hand_icon, t=(4.5, 1.5, 0), ro=(13, 0, 0))
        # nrh_cleanup()

        arm_01_contraint = pm.orientConstraint('r_shoulder_ik', 'r_shoulder_fk', 'r_shoulder_Jnt', mo=False)
        arm_02_contraint = pm.orientConstraint('r_elbow_ik', 'r_elbow_fk', 'r_elbow_Jnt', mo=False)

        arm_01_weights = arm_01_contraint.getWeightAliasList()
        arm_01_weights[0].set(1)
        arm_01_weights[1].set(0)

        arm_02_weights = arm_02_contraint.getWeightAliasList()
        arm_02_weights[0].set(1)
        arm_02_weights[1].set(0)

        pm.setDrivenKeyframe(arm_01_weights, currentDriver='r_hand_ctrl.ikFk')
        pm.setDrivenKeyframe(arm_01_weights, currentDriver='r_hand_ctrl.ikFk')
        pm.setDrivenKeyframe(arm_02_weights, currentDriver='r_hand_ctrl.ikFk')
        pm.setDrivenKeyframe(arm_02_weights, currentDriver='r_hand_ctrl.ikFk')

        # print('ikfk key 1 is set')
        pm.setAttr('r_hand_ctrl.ikFk', 10)

        arm_01_weights[0].set(0)
        arm_01_weights[1].set(1)

        arm_02_weights[0].set(0)
        arm_02_weights[1].set(1)

        pm.setDrivenKeyframe(arm_01_weights, currentDriver='r_hand_ctrl.ikFk')
        pm.setDrivenKeyframe(arm_01_weights, currentDriver='r_hand_ctrl.ikFk')
        pm.setDrivenKeyframe(arm_02_weights, currentDriver='r_hand_ctrl.ikFk')
        pm.setDrivenKeyframe(arm_02_weights, currentDriver='r_hand_ctrl.ikFk')

        # print('ikfk 2nd key is set')

        pm.setAttr("r_hand_ctrl.ikFk", 0)

        pm.setAttr("r_armIK_ctrl.visibility", 1)
        pm.setDrivenKeyframe('r_armIK_ctrl.visibility', currentDriver='r_hand_ctrl.ikFk')
        print('ikfk key 1 is set')

        pm.setAttr("r_hand_ctrl.ikFk", 10)

        pm.setAttr("r_armIK_ctrl.visibility", 0)
        pm.setDrivenKeyframe('r_armIK_ctrl.visibility', currentDriver='r_hand_ctrl.ikFk')
        print('ikfk 2nd key is set')

        pm.setAttr("r_hand_ctrl.ikFk", 0)

        pm.setAttr("r_fk_01_ctrl.visibility", 0)
        pm.setDrivenKeyframe('r_fk_01_ctrl.visibility', currentDriver='r_hand_ctrl.ikFk')
        print('ikfk key 3 is set')

        pm.select('r_fk_01_ctrl', r=1)
        pm.select('r_hand_ctrl', r=1)
        pm.setAttr("r_hand_ctrl.ikFk", 10)
        pm.setAttr("r_fk_01_ctrl.visibility", 1)
        pm.setDrivenKeyframe('r_fk_01_ctrl.visibility', currentDriver='r_hand_ctrl.ikFk')
        print('ikfk key 4 is set')

        pm.setAttr("r_hand_ctrl.ikFk", 0)
