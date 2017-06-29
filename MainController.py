# MainController.py

from MainFrame import MainFrame
from CameraPanel import CameraPanel

from wx import BoxSizer

class MainController(object):
    def __init__(self, application):
        self.app = application

        self.mainFrame = MainFrame(None)
        self.mainFrame.Show()
