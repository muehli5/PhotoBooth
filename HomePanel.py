#HomePanel.py

from wx import Panel, Button, BoxSizer, VERTICAL,CENTER, ALL

class HomePanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self,parent)



        startButon = Button(self, label="Start Photobox",size=((300,100)))


        homeSizer = BoxSizer(VERTICAL)
        homeSizer.AddStretchSpacer()
        homeSizer.Add(startButon, 0, CENTER)
        homeSizer.AddStretchSpacer()


        self.SetSizer(homeSizer)
