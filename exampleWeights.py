import pymel.core as pm 

def finalize_boxes():
    # collect weights
    boxes = collect_proxy_boxes()
    jnts = [box.getParent() for box in boxes]
    weights = []
    for i, box in enumerate(boxes):
        weights.extend([i] * len(box.vtx))

    # mergeboxes
    polyUnite = pymel.createNode('polyUnite')
    itt = 0
    for box in boxes:
        for shape in box.getShapes():
            pymel.connectAttr(shape.worldMatrix, polyUnite.inputMat[itt])
            pymel.connectAttr(shape.outMesh, polyUnite.inputPoly[itt])
            itt += 1
    outputMesh = pymel.createNode('mesh')
    pymel.connectAttr(polyUnite.output, outputMesh.inMesh)
    #pymel.delete(boxes)

    # set skin weights
    pymel.skinCluster(jnts, outputMesh.getParent(), toSelectedBones=True)
    skinCluster = next((hist for hist in outputMesh.listHistory() if isinstance(hist, pymel.nodetypes.SkinCluster)), None)
    for vtx, inf in zip(iter(outputMesh.vtx), weights)
