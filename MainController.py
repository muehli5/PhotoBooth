# MainController.py

from MainFrame import MainFrame

import wx
import Resources as res

class MainController(object):
    def __init__(self, application):
        self.app = application

        self.mainFrame = MainFrame(None)
        self.mainFrame.SetTitle(res.APPLICATION_NAME)

        self.mainFrame.Show()

    