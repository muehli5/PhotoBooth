# CameraPanel.py

import Styles as res

from wx import Panel


class CameraPanel(Panel):
    def __int__(self, parent):
        Panel.__init__(self, parent=parent)
        self.parent = parent

        self.SetBackgroundColour("RED")
