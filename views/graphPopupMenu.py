import wx


from views import editGraphLabels


class GraphPopupMenu(wx.Menu):
    edit = None

    def __init__(self, parent):
        super(GraphPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Edit Title')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnEditTitle, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Refresh')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnEditTitle, mmi)


    def OnEditTitle(self, event):
        self.editGraphLabels = editGraphLabels.EditGraphLabelingFrame(self.parent)

    def OnRefesh(self):
        self.parent.refresh_graph()
