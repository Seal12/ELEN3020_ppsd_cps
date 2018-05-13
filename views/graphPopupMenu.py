import wx


from views import editGraphLabels
from views import customizeGroupsForm


class GraphPopupMenu(wx.Menu):
    edit = None

    def __init__(self, parent, type):
        super(GraphPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Edit Title')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnEditTitle, mmi)

        if type == "PCA":
            editGroups = wx.MenuItem(self, wx.NewId(), "Edit Groups")
            self.Append(editGroups)
            self.Bind(wx.EVT_MENU, self.OnEditGroups, editGroups)

        cmi = wx.MenuItem(self, wx.NewId(), 'Refresh')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnEditTitle, mmi)


    def OnEditTitle(self, event):
        self.editGraphLabels = editGraphLabels.EditGraphLabelingFrame(self.parent)

    def OnRefesh(self):
        self.parent.refresh_graph()

    def OnEditGroups(self, event):
        print("Show edit groups interface")
        groupList = self.parent.get_groups()
        customizeGroupsForm.CustomizeGroupsForm(self.parent, groupList)
