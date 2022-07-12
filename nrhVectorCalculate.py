from maya import cmds, OpenMaya
import pymel.core as pm

shoulderJnt = pm.xform('shoulder_ik', q=1, ws =1, t=1)
elbowJnt = pm.xform('elbow_ik', q=1, ws =1, t=1)
wristJnt = pm.xform('wrist_ik', q=1, ws =1, t=1)

shoulder_vector = OpenMaya.MVector(shoulderJnt[0], shoulderJnt[1], shoulderJnt[2])
elbow_vector = OpenMaya.MVector(elbowJnt[0], elbowJnt[1], elbowJnt[2])
wrist_vector = OpenMaya.MVector(wristJnt[0], wristJnt[1], wristJnt[2])

shoulderToWrist = wrist_vector - shoulder_vector
shoulderToElbow = elbow_vector - shoulder_vector

dotProduct = shoulderToElbow * shoulderToWrist

projectionLength = float(dotProduct) / float(shoulderToWrist.length())

shoulderToWrist_normalize = shoulderToWrist.normal()

projectionVector = shoulderToWrist_normalize * projectionLength

arrowVector = shoulderToElbow - projectionVector
arrowVector *= 5
finalVector = arrowVector + elbow_vector

pvControl = 'l_arm_pv_ctrl_grp'

pm.xform(pvControl, ws=1, t=(finalVector.x, finalVector.y, finalVector.z))
