# MainController.py

from MainFrame import MainFrame
from CameraPanel import CameraPanel
import wx
import Resources as res

class MainController(object):
    def __init__(self, application):
        self.app = application

        self.mainFrame = MainFrame(None, res.APPLICATION_NAME)
        self.camp = CameraPanel(self.mainFrame.panelWizard)
        self.mainFrame.panelWizard.AddPanel(self.camp, 'Cam')

        self.mainFrame.Show()

    