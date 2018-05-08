import wx
from models import graph


class Page(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "THIS IS A PAGE OBJECT", (40,40))

class TabInterface(wx.Panel):
    GraphList = []
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        vbox.Add(hbox)

        self.Notebook3 = wx.Notebook(self)
        vbox.Add(self.Notebook3, 2, flag=wx.EXPAND)

        self.SetSizer(vbox)

        self.pageCounter = 0

    def addPage(self):
        self.pageCounter += 1
        page = Page(self.Notebook3)
        pageTitle = "Page: {0}".format(str(self.pageCounter))
        self.Notebook3.AddPage(page, pageTitle)

    def addGraphPage(self, panelGrph, type):
        self.pageCounter += 1
        pageTitle = "Graph: {0}".format(str(self.pageCounter))

        newGraphPanel = graph.Graph(self.pageCounter, type, panelGrph)
        self.GraphList.append(newGraphPanel)
        self.Notebook3.AddPage(panelGrph, pageTitle)

    def removeGraph(self, graphId):
        index = 0
        for graph in self.GraphList:
            if graph.id == graphId:
                self.GraphList.remove(graph)
                self.Notebook3.DeletePage(index)
                return True
            index += 1

        return False

