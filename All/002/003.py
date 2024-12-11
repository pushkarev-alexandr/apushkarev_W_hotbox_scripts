#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Copy Class
#
#----------------------------------------------------------------------------------------------------------

from PySide2.QtGui import QGuiApplication as qApp

nodeClasses = '-'.join(sorted([i.Class() for i in nuke.selectedNodes()]))

qApp.clipboard().setText(nodeClasses)