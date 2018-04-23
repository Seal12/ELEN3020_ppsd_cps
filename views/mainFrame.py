import wx

from helpers import identityCodes
from views.mainMenu import mainMenuViews


class MyFrame(wx.Frame):

    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        self.InitUI()

    def InitUI(self):
        menuBar = wx.MenuBar()

        #File Submenu
        menuBar.Append(mainMenuViews.create_menu_file(), "&File")

        #Edit Submenu
        menuBar.Append(mainMenuViews.create_menu_edit(), "&Edit")

        #View Submenu
        menuBar.Append(mainMenuViews.create_menu_view(), "&View")

        #Find Submenu
        menuBar.Append(mainMenuViews.create_menu_find(), "&Find")

        #Export Submenu
        menuBar.Append(mainMenuViews.create_menu_export(), "&Export")

        #Help Submenu
        menuBar.Append(mainMenuViews.create_menu_help(), "&Help")

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Genesis!")
        self.Bind(wx.EVT_MENU, self.OnNewGraph, id=identityCodes.FILE_NEW_GRAPH)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=identityCodes.HELP_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=identityCodes.FILE_EXIT)

        self.Center()
        self.Show()

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample",
                      "About Hello World", wx.OK | wx.ICON_INFORMATION, self)

    def OnNewGraph(self, event):
        wx.MessageBox("Give options about ploting graph",
                      "Hy you", wx.OK | wx.ICON_HAND, self)

