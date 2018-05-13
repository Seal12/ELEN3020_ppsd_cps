#!/usr/bin/env python

"""plotGraph.py: Description"""

__author__ = "Seale Rapolai, Phatho Pukwana"
__credits__ = ["Seale Rapolai","Phatho Pukwana"]
__email__ = "109800@students.wits.ac.za"
__status__ = "Development"


import wx

from views import browseFiles
from helpers import identityCodes


class PlotGraphFrame(wx.Frame):

    title = "Input files: "
    plotType = ""
    dataFile = None
    famFile = None
    phenotypeFile = None
    phenotype_column = None

    graphTitle = None

    pcaX = None
    pcaY = None
    pcaZ = None

    plotGraph = False

    def __init__(self, parent, type):
        wx.Frame.__init__(self, parent, wx.ID_ANY, self.title, size=(600, 400))
        self.Panel = wx.Panel(self)
        self.plotType = type
        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.title = self.title + type

        # Data file
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Data File: ', size=(70, 25))
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.dataTC = wx.TextCtrl(self.Panel)
        hbox1.Add(self.dataTC, proportion=1)
        browse_file1 = wx.Button(self.Panel, id=identityCodes.PLOT_BROWSE_DATA, label='...', size=(30, 25))
        hbox1.Add(browse_file1, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        if type == "Admix":
            self.Bind(wx.EVT_BUTTON, self.OnBrowseAdmixData, id=identityCodes.PLOT_BROWSE_DATA)
            self.InitAdmixUI()
        elif type == "PCA":
            self.Bind(wx.EVT_BUTTON, self.OnBrowsePCAData, id=identityCodes.PLOT_BROWSE_DATA)
            self.InitPCAUI()

        self.SetFocus()


    def InitAdmixUI(self):
        # Fam file
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Fam File: ', size=(70,25))
        hbox2.Add(st1, flag=wx.RIGHT, border=8)
        self.famTC = wx.TextCtrl(self.Panel)
        hbox2.Add(self.famTC, proportion=1)
        browse_file2 = wx.Button(self.Panel, id=identityCodes.PLOT_BROWSE_FAM, label='...', size=(30, 25))
        hbox2.Add(browse_file2, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Phenotype file
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Phenotype: ', size=(70,25))
        hbox3.Add(st1, flag=wx.RIGHT, border=8)
        self.phoneTC = wx.TextCtrl(self.Panel)
        hbox3.Add(self.phoneTC, proportion=1)
        browseFile3 = wx.Button(self.Panel, id=identityCodes.PLOT_BROWSE_PHENO, label='...', size=(30, 25))
        hbox3.Add(browseFile3, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vBox.Add((-1, 20))

        # Graph Title
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Graph Title: ', size=(70, 25))
        hbox2.Add(st1, flag=wx.RIGHT, border=8)
        self.GraphTitle = wx.TextCtrl(self.Panel)
        hbox2.Add(self.GraphTitle, proportion=1)
        self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vBox.Add((-1, 10))

        # Choose admix_pheno data column
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        text = "Which column represents the phenotype data?"
        st1 = wx.StaticText(self.Panel, label=text)
        hbox4.Add(st1, flag=wx.LEFT, border=8)

        choice_list = self.GetColumnList("Column", firstCol=2, lastCol=6)
        self.column_choice = wx.Choice(self.Panel, choices=choice_list)
        hbox4.Add(self.column_choice, flag=wx.LEFT | wx.RIGHT, border=8)

        self.column_choice.Bind(wx.EVT_CHOICE, self.OnSelectColumn)

        self.vBox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 70))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, id=identityCodes.PLOT_CLOSE, label='Cancel', size=(70, 30))

        hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, id=identityCodes.PLOT_SUBMIT, label='Plot', size=(70, 30))
        hbox5.Add(btn1)
        self.vBox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Panel.SetSizer(self.vBox)

        self.Bind(wx.EVT_BUTTON, self.OnBrowseFam, id=identityCodes.PLOT_BROWSE_FAM)
        self.Bind(wx.EVT_BUTTON, self.OnBrowsePheno, id=identityCodes.PLOT_BROWSE_PHENO)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=identityCodes.PLOT_CLOSE)
        self.Bind(wx.EVT_BUTTON, self.OnPlotClick, id=identityCodes.PLOT_SUBMIT)

    def InitPCAUI(self):
        # Phenotype file
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Phenotype: ', size=(70, 25))
        hbox2.Add(st1, flag=wx.RIGHT, border=8)
        self.phoneTC = wx.TextCtrl(self.Panel)
        hbox2.Add(self.phoneTC, proportion=1)
        browseFile3 = wx.Button(self.Panel, id=identityCodes.PLOT_BROWSE_PHENO, label='...', size=(30, 25))
        hbox2.Add(browseFile3, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vBox.Add((-1, 20))

        # Graph Title
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Graph Title: ', size=(70, 25))
        hbox2.Add(st1, flag=wx.RIGHT, border=8)
        self.GraphTitle = wx.TextCtrl(self.Panel)
        hbox2.Add(self.GraphTitle, proportion=1)
        self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vBox.Add((-1, 10))

        # PCA choices
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Choose PCAs to plot: ')
        hbox3.Add(st1)
        self.vBox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        xLabel = wx.StaticText(self.Panel, label='X: ', size=(30, 25))
        hbox4.Add(xLabel, flag=wx.LEFT, border=4)

        choice_list = self.GetColumnList("PCA", lastCol=10)
        self.pcaChoiceX = wx.Choice(self.Panel, choices=choice_list, id=identityCodes.PLOT_PCA_CHOICE_X)
        hbox4.Add(self.pcaChoiceX, flag=wx.LEFT | wx.RIGHT, border=8)

        yLabel = wx.StaticText(self.Panel, label='Y: ', size=(30, 25))
        hbox4.Add(yLabel, flag=wx.LEFT, border=4)

        choice_list = self.GetColumnList("PCA", lastCol=10)
        self.pcaChoiceY = wx.Choice(self.Panel, choices=choice_list, id=identityCodes.PLOT_PCA_CHOICE_Y)
        hbox4.Add(self.pcaChoiceY, flag=wx.LEFT | wx.RIGHT, border=8)

        self.vBox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))


        # Choose pca_pheno data column
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        text = "Which column represents the phenotype data?"
        st1 = wx.StaticText(self.Panel, label=text)
        hbox5.Add(st1, flag=wx.LEFT, border=8)

        choice_list = self.GetColumnList("Column", firstCol=2, lastCol=4)
        self.column_choice = wx.Choice(self.Panel, choices=choice_list)
        hbox5.Add(self.column_choice, flag=wx.LEFT | wx.RIGHT, border=8)

        self.column_choice.Bind(wx.EVT_CHOICE, self.OnSelectColumn)

        self.vBox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, id=identityCodes.PLOT_CLOSE, label='Cancel', size=(70, 30))

        hbox6.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, id=identityCodes.PLOT_SUBMIT, label='Plot', size=(70, 30))
        hbox6.Add(btn1)
        self.vBox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Panel.SetSizer(self.vBox)

        self.Bind(wx.EVT_BUTTON, self.OnBrowsePheno, id=identityCodes.PLOT_BROWSE_PHENO)
        self.Bind(wx.EVT_CHOICE, self.OnChangeX, id=identityCodes.PLOT_PCA_CHOICE_X)
        self.Bind(wx.EVT_CHOICE, self.OnChangeY, id=identityCodes.PLOT_PCA_CHOICE_Y)
        self.Bind(wx.EVT_BUTTON, self.OnPlotClick, id=identityCodes.PLOT_SUBMIT)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=identityCodes.PLOT_CLOSE)

    def OnClose(self, event):
        self.Close()

    def OnBrowseAdmixData(self, event):
        self.dataFile = browseFiles.get_file_dir(self, "Data File", ".Q.*")
        if self.dataFile:
            self.dataTC.write(self.dataFile)

    def OnBrowsePCAData(self, event):
        self.dataFile = browseFiles.get_file_dir(self, "Data File", ".pca.*")
        if self.dataFile:
            self.dataTC.write(self.dataFile)

    def OnBrowseFam(self, event):
        self.famFile = browseFiles.get_file_dir(self, "Fam File", ".fam")
        if self.famFile:
            self.famTC.write(self.famFile)

    def OnBrowsePheno(self, event):
        self.phenotypeFile = browseFiles.get_file_dir(self, "Phenotype File", ".phe")
        if self.phenotypeFile:
            self.phoneTC.write(self.phenotypeFile)

    def OnChangeX(self, event):
        self.pcaX = self.pcaChoiceX.GetCurrentSelection()

    def OnChangeY(self, event):
        self.pcaY = self.pcaChoiceY.GetCurrentSelection()

    def OnSelectColumn(self, event):
        self.phenotype_column = self.column_choice.GetCurrentSelection()

    def OnPlotClick(self, event):
        if self.dataFile is None or self.phenotypeFile is None:
            print("Need data")
            wx.MessageBox("Please choose a Data File and a Phenotype File.",
                          "Missing data", wx.OK | wx.ICON_INFORMATION, self)
            return
        if self.plotType == "PCA":
            if self.pcaX is None or self.pcaY is None:
                print("Must choose")
                wx.MessageBox("Please choose PCAs to plot.",
                              "Missing data", wx.OK | wx.ICON_INFORMATION, self)
                return

        if self.phenotype_column is None:
            print("Need phenotype column")
            wx.MessageBox("Please choose a Phenotype column.",
                          "Missing data", wx.OK | wx.ICON_INFORMATION, self)
            return

        if self.GraphTitle.GetValue() is not None:
            self.graphTitle = self.GraphTitle.GetValue()

        self.plotGraph = True
        self.Close()

    def GetColumnList(self, text, firstCol=0, lastCol=4):
        cols = []
        for i in range(firstCol, lastCol):
            cols.append(text + " " + str(i))

        return cols
