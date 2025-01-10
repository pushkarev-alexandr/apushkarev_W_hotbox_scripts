#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Propagate Tile Color
#
#----------------------------------------------------------------------------------------------------------

#v2.0 Pushkarev Aleksandr 2025
#
#copies first selected node's color to other nodes
#gets default color(value 0) from preferences

def copyTileColor():
    nodes = nuke.selectedNodes()
    if nodes:
        nodes.reverse()
        color = nodes[0]['tile_color'].value()
        if color==0:
            pref = nuke.toNode('preferences')
            for knName,kn in pref.knobs().items():
                if knName.startswith('NodeColourSlot') and nodes[0].Class().lower() in kn.value().split():
                    color = pref[knName.replace('Slot','Choice')].value()
                    break
        if color!=0:
            for n in nodes[1:]:
                n['tile_color'].setValue(color)

copyTileColor()