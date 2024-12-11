#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Copy Tile Color
#
#----------------------------------------------------------------------------------------------------------

from PySide2.QtGui import QGuiApplication as qApp

colorsList = []
for i in nuke.selectedNodes():

    interfaceColor = i.knob('tile_color').value()

    if interfaceColor == 0:
        interfaceColor = nuke.defaultNodeColor(i.Class())

    colorsList.append(str(interfaceColor))

nodeColorsString = ' '.join(sorted(colorsList))

qApp.clipboard().setText(nodeColorsString)