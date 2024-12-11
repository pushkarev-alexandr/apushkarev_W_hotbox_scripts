#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Copy Knob Class
#
#----------------------------------------------------------------------------------------------------------

def versionRelatedCopy(txt):
    if nuke.NUKE_VERSION_MAJOR>10:
        from PySide2.QtGui import QGuiApplication as qApp
        qApp.clipboard().setText(txt)
    else:
        import subprocess
        subprocess.check_call('echo '+txt.strip()+'|clip', shell=True)

def copyKnobClass():
    input = nuke.getInput('Start of knob name...')
    node = nuke.selectedNode()
    knobs = node.knobs()
    for kn in knobs:
        if kn.startswith(input):
            cl = knobs[kn].Class()
            print(cl)
            versionRelatedCopy(cl)
            return

copyKnobClass()