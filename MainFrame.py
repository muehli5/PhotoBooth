# MainFrame.py

from wx import Frame
from wx import ID_ANY, EmptyString, DefaultPosition, DisplaySize


from SettingNBPanel import SettingPanel

class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, id=ID_ANY, title=EmptyString, pos=DefaultPosition, size=DisplaySize())
        panel = SettingPanel(self)

