import wx

from helpers import identityCodes
from views.mainMenu import mainMenuViews
from views.plotGraph import PlotGraphFrame
from controllers import pcaGraph
from controllers import admixGraph
from views import graphTabs


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

        self.tabInterface = graphTabs.TabInterface(self.mainPanel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.tabInterface, wx.ID_ANY, wx.EXPAND | wx.ALL, 0)
        self.mainPanel.SetSizer(vbox)

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Genesis!")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=identityCodes.HELP_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=identityCodes.FILE_EXIT)
        self.Bind(wx.EVT_MENU, self.OnPlotPCA, id=identityCodes.PLOT_PCA)
        self.Bind(wx.EVT_MENU, self.OnPlotAdmix, id=identityCodes.PLOT_ADMIX)
        self.Bind(wx.EVT_MENU, self.OnFindIndividual, id=identityCodes.FIND_INDIVIDUAL)

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
            if self.plotForm.plotType == "PCA":
                newCanvasPanel = pcaGraph.PCAGraph(self.tabInterface.Notebook3)
                newCanvasPanel.import_data(evec_file_path=self.plotForm.dataFile,
                                           pheno_file_path=self.plotForm.phenotypeFile,
                                           column=2)
                newCanvasPanel.plot_pca(self.plotForm.pcaX, self.plotForm.pcaY)

                self.tabInterface.addGraphPage(newCanvasPanel, "PCA")
            elif self.plotForm.plotType == "Admix":
                newCanvasPanel = admixGraph.AdmixGraph(self.tabInterface.Notebook3)
                newCanvasPanel.import_data(self.plotForm.famFile, self.plotForm.dataFile, self.plotForm.phenotypeFile, 1)
                newCanvasPanel.plot_admix()

                self.tabInterface.addGraphPage(newCanvasPanel, "Admix")


    def OnFindIndividual(self, event):
        print("Find Nemo")