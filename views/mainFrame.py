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

        newCanvasPanel = pcaGraph.PCAGraph(self.mainPanel)
        pca_dir = "C:\\Users\\Seale\\Documents\\wits\\PPSD\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm-SYMCL.pca.evec"
        phe_dir = "C:\\Users\\Seale\\Documents\\wits\\PPSD\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm.phe"
        newCanvasPanel.import_pca_file(pca_dir)
        newCanvasPanel.import_pheno_file(phe_dir)
        newCanvasPanel.plot_pca(0, 2)

        hBox1 = wx.BoxSizer(wx.HORIZONTAL)
        hBox1.Add(newCanvasPanel, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, proportion=1, border=0)
        self.vBox.Add(hBox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=0)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self.mainPanel, id=536, label='Chenge Title', size=(100, 30))
        hbox2.Add(btn1, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=0)
        self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=0)
        self.Bind(wx.EVT_BUTTON, self.changeTitle, id=536)

        self.mainPanel.SetSizer(self.vBox)
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
        form = PlotGraphFrame(self, "PCA")
        form.Center()
        form.Show()

    def OnPlotAdmix(self, event):
        form = PlotGraphFrame(self, "Admix")
        form.Center()
        form.Show()

    def changeTitle(self, event):
        self.canvasPanel.changeTitle("Chicken farm")

