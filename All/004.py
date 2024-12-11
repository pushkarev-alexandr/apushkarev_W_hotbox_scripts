#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Dissable oposite
#
#----------------------------------------------------------------------------------------------------------

selected = nuke.selectedNodes()
selected.reverse()
l = len(selected)
for i in range(1,l):
    selected[i].knob('disable').setExpression('!'+selected[0].name()+'.disable')