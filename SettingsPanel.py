#SettingsPanel.py
from wx import Panel

import wx

class SettingsPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        sizer = self.create_controls()
        self.SetSizer(sizer)

    def create_controls(self):
        box = self.create_box()
        #buttons = self.create_buttons()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(box, 1, wx.EXPAND | wx.ALL, 50)
        #sizer.Add(buttons, 0, wx.EXPAND | wx.BOTTOM, 10)
        return sizer

    def create_box(self):
        contents = self.create_box_contents()
        box = wx.StaticBox(self, -1, 'Haupteinstellungen')
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        sizer.Add(contents, 1, wx.EXPAND | wx.ALL, 10)
        return sizer

    def create_box_contents(self):
        male = wx.CheckBox(self, -1, 'Male')
        married = wx.CheckBox(self, -1, 'Married')
        age = self.create_age()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(male)
        sizer.AddSpacer(10)
        sizer.Add(married)
        sizer.AddSpacer(10)
        sizer.Add(age)
        return sizer

    def create_age(self):
        age = wx.SpinCtrl(self, -1, '28', min=0, max=100, size=(64, -1))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, -1, 'Age')
        sizer.Add(text, 0, wx.ALIGN_CENTER_VERTICAL)
        sizer.AddSpacer(10)
        sizer.Add(age)
        return sizer

    def create_buttons(self):
        button = wx.Button(self, wx.ID_OK, 'OK')
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(button)
        sizer.AddStretchSpacer(1)
        return sizer

