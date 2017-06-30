# WizardPanel.py

from wx import Panel
from wx import BoxSizer, VERTICAL, EXPAND, ALL

class WizardPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent=parent)
        self.panels = {}
        self.currentPanelKey = 0

        self.sizer = BoxSizer(VERTICAL)
        self.SetSizer(self.sizer)

    def AddPanel(self, newPanel, panelKey):
        panel = newPanel
        self.sizer.Add(panel, 1, EXPAND|ALL)
        self.panels[panelKey] = panel
        if(len(self.panels) > 1):
            panel.Hide()
            self.Layout()
        else:
            self.currentPanelKey = panelKey

    def SetActivePanel(self, panelKey):
        if panelKey in self.panels.keys():
            self.panels[self.currentPanelKey].Hide()
            self.panels[panelKey].Show()
            self.currentPanelKey = panelKey
            self.sizer.Layout()