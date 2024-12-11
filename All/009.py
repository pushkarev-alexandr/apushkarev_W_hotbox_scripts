#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set/Remove Viewer IP
#
#----------------------------------------------------------------------------------------------------------

#returns True if  selected node is inside selected backdrop
def isInsideBackdrop(node,backdrop):
    nXl = node.xpos()
    nYt = node.ypos()
    nXr = nXl+node.screenWidth()
    nYb = nYt+node.screenHeight()
    bXl = backdrop.xpos()
    bYt = backdrop.ypos()
    bXr = bXl+backdrop.screenWidth()
    bYb = bYt+backdrop.screenHeight()
    if ((nXl<bXr and nXl>bXl) or (nXr<bXr and nXr>bXl)) and ((nYt<bYb and nYt>bYt) or (nYb<bYb and nYb>bYt)):
        return True
    else:
        return False

#returns list of backdrops where selected node is inside
def insideBackdropsList(node):
    lst = []
    for backdrop in nuke.allNodes('BackdropNode'):
        if backdrop.name()!=node.name() and isInsideBackdrop(node,backdrop):
            lst.append(backdrop)
    return lst
#if only one node selected, sets this node to currently active viewer input process
#if nothing is selected removes ip node
def setRemoveViewerInput():
    if not nuke.activeViewer():
        nuke.message('No active viewer')
        return
    viewer = nuke.activeViewer().node()
    kn = viewer.knob('input_process_node')
    sel = nuke.selectedNodes()
    if not sel:#if nothing selected delete ip node
        ip_node = nuke.toNode(kn.value())
        if ip_node:
            lst = insideBackdropsList(ip_node)
            if len(lst)==1 and lst[0]['label'].value().lower() in ['<center>ip','ip']:#delete ip backdrop
                nuke.delete(lst[0])
            nuke.delete(ip_node)
        kn.setValue('VIEWER_INPUT')
        return
    elif len(sel)!=1:
        nuke.message('Select only one node')
        return
    
    node = sel[0]
    if kn.value()!=node.name():
        prev_node = nuke.toNode(kn.value())
        if prev_node:#delete backdrop for previous node
            lst = insideBackdropsList(prev_node)
            if len(lst)==1 and lst[0]['label'].value().lower() in ['<center>ip','ip']:
                nuke.delete(lst[0])
        kn.setValue(node.name())
        viewer.knob('input_process').setValue(True)
        #--------backdrop--------
        import nukescripts
        backdrop = nukescripts.autobackdrop.autoBackdrop()
        offset = 15
        backdrop['xpos'].setValue(int(backdrop['xpos'].value()-offset))
        backdrop['bdwidth'].setValue(backdrop['bdwidth'].value()+offset*2)
        backdrop['bdheight'].setValue(backdrop['bdheight'].value()+offset)
        backdrop['label'].setValue('<center>IP')
        backdrop['note_font_size'].setValue(25)

setRemoveViewerInput()