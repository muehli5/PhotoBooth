from wx import Panel, StaticText, BoxSizer, EXPAND, Notebook,  VERTICAL, ALL

import Resources as res

from HomePanel import HomePanel
from InfoPanel import InfoPanel
from SettingsPanel import SettingsPanel
from PrinterPanel import PrinterPanel
from DiashowPanel import DiashowPanel

class SettingPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self,parent)

        nb = Notebook(self)

        homePanel = HomePanel(nb)
        infoPanel = InfoPanel(nb)
        settingsPanel = SettingsPanel(nb)
        printerPanel = PrinterPanel(nb)
        diashowPanel = DiashowPanel(nb)
        nb.AddPage(homePanel, res.HOME_NAME)
        nb.AddPage(infoPanel, res.INFO_NAME)
        nb.AddPage(settingsPanel, res.SETTING_NAME)
        nb.AddPage(printerPanel, res.PRINTER_NAME)
        nb.AddPage(diashowPanel, res.DIASHOW_NAME)

        sizer = BoxSizer(VERTICAL)
        sizer.Add(nb,1, EXPAND|ALL,100)

        self.SetSizer(sizer)

