#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Propagate Tile Color
#
#----------------------------------------------------------------------------------------------------------

def copyTileColor():
    nodes = nuke.selectedNodes()
    if len(nodes)<2:
        return
    nodes.reverse()
    color_to_copy = None
    for node in nodes:
        color = node['tile_color'].value()
        if color!=0:
            color_to_copy = color
            break
    if color_to_copy!=None:
        for node in nodes:
            node['tile_color'].setValue(color_to_copy)

copyTileColor()