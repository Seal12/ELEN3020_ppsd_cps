import wx
from views import browseFiles
from helpers import identityCodes


class PlotGraphFrame(wx.Frame):

    title = "Input files: "
    dataFile = None
    famFile = None
    phenotypeFile = None

    pcaX = None
    pcaY = None
    pcaZ = None

    def __init__(self, parent, type):
        wx.Frame.__init__(self, parent, wx.ID_ANY, self.title, size=(500, 250))
        self.Panel = wx.Panel(self)
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

        self.Bind(wx.EVT_BUTTON, self.OnBrowseData, id=identityCodes.PLOT_BROWSE_DATA)

        if type == "Admix":
            self.InitAdmixUI()
        elif type == "PCA":
            self.InitPCAUI()


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
        self.vBox.Add((-1, 10))

        # Choose pca_pheno data column
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        text = "Which column represents the phenotype data?"
        st1 = wx.StaticText(self.Panel, label=text)
        hbox4.Add(st1, flag=wx.LEFT, border=8)

        choiseList = self.GetColumnList("Column", 5)
        choice = wx.Choice(self.Panel, choices=choiseList)
        hbox4.Add(choice, flag=wx.LEFT | wx.RIGHT, border=8)

        self.vBox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, id=identityCodes.PLOT_CLOSE, label='Cancel', size=(70, 30))

        hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, label='Plot', size=(70, 30))
        hbox5.Add(btn1)
        self.vBox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Panel.SetSizer(self.vBox)

        self.Bind(wx.EVT_BUTTON, self.OnBrowseFam, id=identityCodes.PLOT_BROWSE_FAM)
        self.Bind(wx.EVT_BUTTON, self.OnBrowsePheno, id=identityCodes.PLOT_BROWSE_PHENO)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=identityCodes.PLOT_CLOSE)

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
        self.vBox.Add((-1, 10))


        # PCA choices
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Choose PCAs to plot: ')
        hbox3.Add(st1)
        self.vBox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        xLabel = wx.StaticText(self.Panel, label='X: ', size=(30, 25))
        hbox4.Add(xLabel, flag=wx.LEFT, border=4)

        choiseList = self.GetColumnList("PCA", 5)
        self.pcaChoiceX = wx.Choice(self.Panel, choices=choiseList, id=identityCodes.PLOT_PCA_CHOICE_X)
        hbox4.Add(self.pcaChoiceX, flag=wx.LEFT | wx.RIGHT, border=8)

        yLabel = wx.StaticText(self.Panel, label='Y: ', size=(30, 25))
        hbox4.Add(yLabel, flag=wx.LEFT, border=4)

        choiseList = self.GetColumnList("PCA", 5)
        self.pcaChoiceY = wx.Choice(self.Panel, choices=choiseList, id=identityCodes.PLOT_PCA_CHOICE_Y)
        hbox4.Add(self.pcaChoiceY, flag=wx.LEFT | wx.RIGHT, border=8)

        zLabel = wx.StaticText(self.Panel, label='Z: ', size=(30, 25))
        hbox4.Add(zLabel, flag=wx.LEFT, border=4)

        choiseList = self.GetColumnList("PCA", 5)
        self.pcaChoiceZ = wx.Choice(self.Panel, choices=choiseList, id=identityCodes.PLOT_PCA_CHOICE_Z)
        hbox4.Add(self.pcaChoiceZ, flag=wx.LEFT | wx.RIGHT, border=8)

        self.vBox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))


        # Choose pca_pheno data column
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        text = "Which column represents the phenotype data?"
        st1 = wx.StaticText(self.Panel, label=text)
        hbox5.Add(st1, flag=wx.LEFT, border=8)

        choiseList = self.GetColumnList("Column", 5)
        self.ChoicePheno = wx.Choice(self.Panel, choices=choiseList)
        hbox5.Add(self.ChoicePheno, flag=wx.LEFT | wx.RIGHT, border=8)

        self.vBox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, id=identityCodes.PLOT_CLOSE, label='Cancel', size=(70, 30))

        hbox6.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, label='Plot', size=(70, 30))
        hbox6.Add(btn1)
        self.vBox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Panel.SetSizer(self.vBox)

        self.Bind(wx.EVT_BUTTON, self.OnBrowsePheno, id=identityCodes.PLOT_BROWSE_PHENO)
        self.Bind(wx.EVT_CHOICE, self.OnChangeX, id=identityCodes.PLOT_PCA_CHOICE_X)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=identityCodes.PLOT_CLOSE)

    def OnClose(self, event):
        self.Close()

    def OnBrowseData(self, event):
        self.dataFile = browseFiles.get_file_dir(self, "Data File", ".Q.*")
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

    def OnChangeZ(self, event):
        self.pcaZ = self.pcaChoiceZ.GetCurrentSelection()

    def OnPlotClick(self, event):
        print("Pass data to print method")

    def GetColumnList(self, text, numCols):
        cols = []
        for i in range(0, numCols):
            cols.append(text + " " + str(i+1))

        return cols
