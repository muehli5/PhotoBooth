#DiashowPanel.py

from wx import Panel, StaticText

class DiashowPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        t = StaticText(self, -1, "This is a PageThree object", (60, 200))