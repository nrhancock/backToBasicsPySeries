import maya.cmds as cmds
import pymel.core as pm

skinClusters = pm.ls(typ='skinCluster') 
skinnedMeshes = []
 
for node in skinClusters:
    skinnedMeshes.append( node.outputGeometry.connections() )

#skinnedMeshes = [a for b in [node.outputGeometry.connections() for node in skinClusters] for a in b]


'''or'''

#clusters = cmds.ls(type='skinCluster')
#meshes = set(sum([cmds.skinCluster(c, q=1, g=1) for c in clusters], []))
