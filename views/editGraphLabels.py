#!/usr/bin/env python

"""editGraphLabels.py: Description"""

__author__ = "Seale Rapolai"
__credits__ = ["Seale Rapolai"]
__email__ = "109800@students.wits.ac.za"
__status__ = "Development"


import wx

from helpers import identityCodes


class PlotGraphFrame(wx.Frame):
    def __init__(self, parent, type):
        wx.Frame.__init__(self, parent, wx.ID_ANY, self.title, size=(300, 100))

        self.Panel = wx.Panel(self)
        self.vBox = wx.BoxSizer(wx.VERTICAL)

        # Data file
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Graph Title: ', size=(70, 25))
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.titleTC = wx.TextCtrl(self.Panel)
        hbox1.Add(self.titleTC, proportion=1)
        self.vBox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, id=identityCodes.PLOT_CLOSE, label='Cancel', size=(70, 30))

        hbox2.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, id=identityCodes.PLOT_SUBMIT, label='Update', size=(70, 30))
        hbox2.Add(btn1)
        self.vBox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Panel.SetSizer(self.vBox)

