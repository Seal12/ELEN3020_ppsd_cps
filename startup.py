import wx


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
        menuFile.Append(1, "New Project...")
        menuFile.Append(2, "Open...")
        menuFile.Append(3, "&Save")
        menuFile.Append(4, "&Save As...")
        menuFile.AppendSeparator()
        menuFile.Append(5, "&Settings")
        menuFile.AppendSeparator()
        menuFile.Append(6, "&Exit")
        menuBar.Append(menuFile, "&File")

        #Edit Submenu
        menuEdit = wx.Menu()
        menuEdit.Append(8, "&Undo...")
        menuEdit.Append(9, "&Redo...")
        menuEdit.AppendSeparator()
        menuEdit.Append(10, "&Copy")
        menuEdit.Append(11, "&Cut")
        menuEdit.Append(12, "&Paste")
        menuEdit.AppendSeparator()
        menuEdit.Append(13, "&Font...")
        menuBar.Append(menuEdit, "&Edit")

        #View Submenu
        menuView = wx.Menu()
        menuBar.Append(menuView, "&View")

        #Find Submenu
        menuFind = wx.Menu()
        menuFind.Append(14, "&Individual")
        menuFind.Append(15, "&Group")
        menuBar.Append(menuFind, "&Find")

        #Export Submenu
        menuExport = wx.Menu()
        menuExport.Append(16, "&PDF")
        menuExport.Append(17, "&PNG")
        menuExport.Append(18, "&SVG")
        menuBar.Append(menuExport, "&Export")

        #Help Submenu
        menuHelp = wx.Menu()
        menuHelp.Append(19, "&Documentation (link)")
        menuHelp.Append(19, "&FAQ (link)")
        menuHelp.AppendSeparator()
        menuHelp.Append(20, "&Report Issue")
        menuHelp.Append(20, "&Feedback")
        menuHelp.AppendSeparator()
        menuHelp.Append(21, "&Check for Updates...")
        menuHelp.Append(1, "&About")
        menuBar.Append(menuHelp, "&Help")

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Genesis!")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=6)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample",
                      "About Hello World", wx.OK | wx.ICON_INFORMATION, self)


if __name__ == '__main__':
    app = AppMain(False)
    app.MainLoop()
