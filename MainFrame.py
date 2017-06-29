# MainFrame.py

from CameraPanel import CameraPanel

from wx import Frame
from wx import ID_ANY, EmptyString, DefaultPosition, DisplaySize
from wx import BoxSizer, VERTICAL, EXPAND
import wx


class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, id=ID_ANY, title=EmptyString, pos=DefaultPosition, size=DisplaySize())

        panel1 = CameraPanel(self)

        box = wx.BoxSizer(wx.VERTICAL)

        box.Add(panel1, 1, wx.EXPAND)

        self.SetAutoLayout(True)

        self.SetSizer(box)

        self.Layout()
