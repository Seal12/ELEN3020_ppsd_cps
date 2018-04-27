import wx

from views import mainFrame


class AppMain(wx.App):

    def OnInit(self):
        frame = mainFrame.MyFrame("Genesis", (50, 60), (1020, 660))
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    app = AppMain(False)
    app.MainLoop()

