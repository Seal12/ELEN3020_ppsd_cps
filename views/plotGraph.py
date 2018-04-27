import wx


class PlotGraphFrame(wx.Frame):

    title = "Input files: "

    def __init__(self, parent, type):
        wx.Frame.__init__(self, parent, wx.ID_ANY, self.title, size=(500, 250))
        self.Panel = wx.Panel(self)
        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.title = self.title + type

        # Data file
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Data File: ', size=(70, 25))
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(self.Panel)
        hbox1.Add(tc, proportion=1)
        browse_file1 = wx.Button(self.Panel, label='...', size=(30, 25))
        hbox1.Add(browse_file1, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        if type == "Admix":
            self.InitAdmixUI()


    def InitAdmixUI(self):
        # Fam file
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Fam File: ', size=(70,25))
        hbox2.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(self.Panel)
        hbox2.Add(tc, proportion=1)
        browse_file2 = wx.Button(self.Panel, label='...', size=(30, 25))
        hbox2.Add(browse_file2, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Phenotype file
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.Panel, label='Phenotype: ', size=(70,25))
        hbox3.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(self.Panel)
        hbox3.Add(tc, proportion=1)
        browseFile3 = wx.Button(self.Panel, label='...', size=(30, 25))
        hbox3.Add(browseFile3, flag=wx.LEFT, border=8)
        self.vBox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vBox.Add((-1, 10))


        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        text = "Which column represents the phenotype data?"
        st1 = wx.StaticText(self.Panel, label=text)
        hbox4.Add(st1, flag=wx.LEFT, border=8)

        choiseList = self.GetColumnList(5)
        choice = wx.Choice(self.Panel, choices=choiseList)
        hbox4.Add(choice, flag=wx.LEFT | wx.RIGHT, border=8)

        self.vBox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.vBox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, label='Cancel', size=(70, 30))
        self.Bind(wx.EVT_MENU, self.OnClose, btn2)
        hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, label='Plot', size=(70, 30))
        hbox5.Add(btn1)
        self.vBox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Panel.SetSizer(self.vBox)

    def OnClose(self, event):
        print("I must perform boshido")
        self.Close()

    def GetColumnList(self, numCols):
        cols = []
        for i in range(0, numCols):
            cols.append("Column " + str(i+1))

        return cols
