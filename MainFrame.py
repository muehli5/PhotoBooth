# MainFrame.py
from WizardPanel import WizardPanel

from wx import Frame, Panel
from wx import ID_ANY, EmptyString, DefaultPosition, DisplaySize
import wx


class MainFrame(Frame):
    def __init__(self, parent, title):
        Frame.__init__(self, parent, id=ID_ANY, title=title, pos=DefaultPosition, size=DisplaySize())

        self.panelWizard = WizardPanel(self)
