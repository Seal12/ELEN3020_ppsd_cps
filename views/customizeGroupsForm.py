import wx
import wx.lib.scrolledpanel


class CustomizeGroupsForm(wx.Frame):
    title = "Customize PCA Groups: "
    markers = ['o', 'x', '*', '^']
    markerChoices = []
    markerSizes = []

    def __init__(self, parent, pcaGroupList):
        wx.Frame.__init__(self, parent, wx.ID_ANY, self.title, size=(600, 400))

        self.parent = parent
        self.Panel = wx.lib.scrolledpanel.ScrolledPanel(self)
        self.Panel.SetupScrolling()
        self.Panel.SetBackgroundColour("#FFFFFF")
        self.Panel.SetScrollbar(20, 20, 50, 50)
        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.pcaGroups = pcaGroupList

        counter = 0
        for group in pcaGroupList:
            # Group properties
            label = "Group " + str(counter) + ": " + group.name
            hbox1 = wx.BoxSizer(wx.HORIZONTAL)
            st1 = wx.StaticText(self.Panel, label=label)
            hbox1.Add(st1)
            self.vBox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

            hbox2 = wx.BoxSizer(wx.HORIZONTAL)
            markerLabel = wx.StaticText(self.Panel, label='Marker: ', size=(60, 25))
            hbox2.Add(markerLabel, flag=wx.LEFT, border=4)

            markerChoice = wx.Choice(self.Panel, choices=self.markers, id=wx.ID_ANY)
            self.markerChoices.append(markerChoice)
            hbox2.Add(markerChoice, flag=wx.LEFT | wx.RIGHT, border=8)

            markerSizeLabel = wx.StaticText(self.Panel, label='Marker Size: ', size=(100, 25))
            hbox2.Add(markerSizeLabel, flag=wx.LEFT, border=4)

            markerSize = wx.SpinCtrl(self.Panel, id=wx.NewId())
            markerSize.SetValue(12)
            self.markerSizes.append(markerSize)
            hbox2.Add(markerSize, flag=wx.LEFT | wx.RIGHT, border=8)

            self.vBox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
            self.vBox.Add((-1, 30))
            counter += 1


        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn2 = wx.Button(self.Panel, id=wx.ID_ANY, label='Cancel', size=(70, 30))

        hbox6.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn1 = wx.Button(self.Panel, id=wx.ID_ANY, label='Update', size=(70, 30))
        hbox6.Add(btn1)
        self.vBox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Bind(wx.EVT_BUTTON, self.OnCancel, btn2)
        self.Bind(wx.EVT_BUTTON, self.OnUpdate, btn1)

        self.Panel.SetSizer(self.vBox)
        self.Center()
        self.Show()

    def OnCancel(self, event):
        self.Close()

    def OnUpdate(self, event):
        for i in range(0, len(self.pcaGroups)):
            markderIndex = self.markerChoices[i].GetCurrentSelection()
            if(markderIndex > -1):
                newMarker = self.markers[markderIndex]
                print("Group " + str(i) + ": " + newMarker)
                self.parent.set_group_marker(self.pcaGroups[i].name, newMarker)
                self.parent.set_group_marker_size(self.pcaGroups[i].name, self.markerSizes[i].GetValue())


        self.Close()
