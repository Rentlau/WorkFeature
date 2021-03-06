# -*- coding: utf-8 -*-
import sys
import os.path

# Change this by your own FreeCAD lib path to import FreeCAD
if not sys.path.__contains__("/usr/lib/freecad/lib"):
    sys.path.append("/usr/lib/freecad/lib")

try:
    # try import
    m_current_path = os.path.realpath(__file__)
    m_current_path = os.path.dirname(m_current_path)
    if not sys.path.__contains__(str(m_current_path) + "/WorkFeature"):
        sys.path.append(str(m_current_path) + "/WorkFeature")
    import WorkFeature.WF as WF
except ImportError as error:
    print(sys.path)
    print(error.__class__.__name__ + ": " + error.msg)
    try:
        import FreeCAD
        # first check if the path to WorkFeature was set in the preferences
        param = FreeCAD.ParamGet('User parameter:Plugins/workfeature')
        m_current_path = param.GetString('destination', '')
        if not m_current_path:
            # get the path of the current python script
            m_current_path = os.path.realpath(__file__)
            m_current_path = os.path.dirname(m_current_path)
        # check if this path belongs to the PYTHONPATH variable and if not add it
        if not sys.path.__contains__(str(m_current_path) + "/WorkFeature"):
            sys.path.append(str(m_current_path) + "/WorkFeature")
        # retry import now
        try:
            import WorkFeature.WF as WF
        except ImportError:
            # we still cannot find WorkFeature. Inform the user
            from PySide import QtGui
            msgBox = QtGui.QMessageBox()
            msgBox.setText("ERROR: Cannot load FreeCAD WorkFeature macro path ! \nCheck the installation !")
            msgBox.exec_()
            print("ERROR:cannot load FreeCAD WorkFeature macro path !")
            print("Check the installation !")
            sys.exit(1)
    except ImportError:
        print("ERROR: Cannot load FreeCAD WorkFeature macro path !")
        print("Check the installation !")
        sys.exit(1)

WF.myDialog = WF.WorkFeatureTab()
