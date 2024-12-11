#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: List of knob names
#
#----------------------------------------------------------------------------------------------------------

input = nuke.getInput('Start of knob name...')
if input:
    lst = []
    for node in nuke.selectedNodes():
        for kname in node.knobs():
            if kname.startswith(input):
                lst.append(kname)
    if lst:
        nuke.message('\n'.join(lst))