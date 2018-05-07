import wx

import test_plot
from helpers import identityCodes
from views.mainMenu import mainMenuViews
from views.plotGraph import PlotGraphFrame
from controllers import pcaGraph


class MyFrame(wx.Frame):

    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.mainPanel = wx.Panel(self)
        self.InitUI()

    def InitUI(self):

        menuBar = wx.MenuBar()

        # File Submenu
        menuBar.Append(mainMenuViews.create_menu_file(), "&File")

        # Edit Submenu
        menuBar.Append(mainMenuViews.create_menu_edit(), "&Edit")

        # View Submenu
        menuBar.Append(mainMenuViews.create_menu_plot(), "&Plot")

        # Find Submenu
        menuBar.Append(mainMenuViews.create_menu_find(), "&Find")

        # Export Submenu
        menuBar.Append(mainMenuViews.create_menu_export(), "&Export")

        # Help Submenu
        menuBar.Append(mainMenuViews.create_menu_help(), "&Help")


        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Genesis!")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=identityCodes.HELP_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=identityCodes.FILE_EXIT)
        self.Bind(wx.EVT_MENU, self.OnPlotPCA, id=identityCodes.PLOT_PCA)
        self.Bind(wx.EVT_MENU, self.OnPlotAdmix, id=identityCodes.PLOT_ADMIX)

        self.Center()
        self.Show()

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample",
                      "About Hello World", wx.OK | wx.ICON_INFORMATION, self)

    def OnPlotPCA(self, event):
        self.plotForm = PlotGraphFrame(self, "PCA")
        self.plotForm.Bind(wx.EVT_CLOSE, self.OnPlotAdmixFormClose)
        self.plotForm.Center()
        self.plotForm.Show()

    def OnPlotAdmix(self, event):
        self.plotForm = PlotGraphFrame(self, "Admix")
        self.plotForm.Bind(wx.EVT_CLOSE, self.OnPlotAdmixFormClose)
        self.plotForm.Center()
        self.plotForm.Show()

    def OnPlotAdmixFormClose(self, event):
        event.Skip()

        if self.plotForm.plotGraph:

            newCanvasPanel = pcaGraph.PCAGraph(self.mainPanel)
            newCanvasPanel.import_pca_file(self.plotForm.dataFile)
            newCanvasPanel.import_pheno_file(self.plotForm.phenotypeFile)
            newCanvasPanel.plot_pca(self.plotForm.pcaX, self.plotForm.pcaY)

            hBox1 = wx.BoxSizer(wx.HORIZONTAL)
            hBox1.Add(newCanvasPanel, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, proportion=1, border=0)
            self.vBox.Add(hBox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=0)
            self.mainPanel.SetSizer(self.vBox)

