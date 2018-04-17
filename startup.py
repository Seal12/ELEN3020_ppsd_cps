import wx

from helpers import identityCodes


class AppMain(wx.App):

    def OnInit(self):
        frame = MyFrame("Genesis", (50, 60), (850, 440))
        frame.Show()
        self.SetTopWindow(frame)
        return True


class MyFrame(wx.Frame):

    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuBar = wx.MenuBar()

        #File Submenu
        menuFile = wx.Menu()
        menuFile.Append(identityCodes.FILE_NEW_PROJECT, "New Project...")
        menuFile.Append(identityCodes.FILE_OPEN, "Open...")
        menuFile.Append(identityCodes.FILE_SAVE, "&Save")
        menuFile.Append(identityCodes.FILE_SAVE_AS, "&Save As...")
        menuFile.AppendSeparator()
        menuFile.Append(identityCodes.FILE_SETTINGS, "&Settings")
        menuFile.AppendSeparator()
        menuFile.Append(identityCodes.FILE_EXIT, "&Exit")
        menuBar.Append(menuFile, "&File")

        #Edit Submenu
        menuEdit = wx.Menu()
        menuEdit.Append(identityCodes.EDIT_UNDO, "&Undo...")
        menuEdit.Append(identityCodes.EDIT_REDO, "&Redo...")
        menuEdit.AppendSeparator()
        menuEdit.Append(identityCodes.EDIT_COPY, "&Copy")
        menuEdit.Append(identityCodes.EDIT_CUT, "&Cut")
        menuEdit.Append(identityCodes.EDIT_PASTE, "&Paste")
        menuEdit.AppendSeparator()
        menuEdit.Append(identityCodes.EDIT_FONT, "&Font...")
        menuBar.Append(menuEdit, "&Edit")

        #View Submenu
        menuView = wx.Menu()
        menuBar.Append(menuView, "&View")

        #Find Submenu
        menuFind = wx.Menu()
        menuFind.Append(identityCodes.FIND_INDIVIDUAL, "&Individual")
        menuFind.Append(identityCodes.FIND_GROUP, "&Group")
        menuBar.Append(menuFind, "&Find")

        #Export Submenu
        menuExport = wx.Menu()
        menuExport.Append(identityCodes.EXPORT_PDF, "&PDF")
        menuExport.Append(identityCodes.EXPORT_PNG, "&PNG")
        menuExport.Append(identityCodes.EXPORT_SVG, "&SVG")
        menuBar.Append(menuExport, "&Export")

        #Help Submenu
        menuHelp = wx.Menu()
        menuHelp.Append(identityCodes.HELP_DOCUMENTATION, "&Documentation (link)")
        menuHelp.Append(identityCodes.HELP_FAQ, "&FAQ (link)")
        menuHelp.AppendSeparator()
        menuHelp.Append(identityCodes.HELP_REPORT_ISSUE, "&Report Issue")
        menuHelp.Append(identityCodes.HELP_FEEDBACK, "&Feedback")
        menuHelp.AppendSeparator()
        menuHelp.Append(identityCodes.HELP_CHECK_UPDATES, "&Check for Updates...")
        menuHelp.Append(identityCodes.HELP_ABOUT, "&About")
        menuBar.Append(menuHelp, "&Help")

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Genesis!")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=identityCodes.HELP_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=identityCodes.FILE_EXIT)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample",
                      "About Hello World", wx.OK | wx.ICON_INFORMATION, self)


if __name__ == '__main__':
    app = AppMain(False)
    app.MainLoop()
