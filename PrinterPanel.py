#PrinterPanel.py

from wx import Panel, StaticText

class PrinterPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        t = StaticText(self, -1, "This is a PageTddhree object", (60, 200))