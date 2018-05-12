import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from collections import defaultdict
from controllers import importData


class AdmixGraph(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.subjects = []
        self.groups = []
        # This is the data that will be plotted
        self.ancestries = defaultdict(list)
        # List of labels
        self.labelsList = []
        # List of locations the labels appear
        self.xtickPos = []
        self.importer = importData.ImportAdmixData()
        # Create Figure and Axes instances
        self.fig = plt.figure()
        # self.fig.tight_layout(pad=0, w_pad=0)
        self.ax = self.fig.subplots(1)
        self.ax.yaxis.set_major_locator(plt.NullLocator())
        self.ax.xaxis.set_major_formatter(plt.NullFormatter())

        # User Interface settings
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.RIGHT | wx.TOP | wx.GROW)

        self.SetSizer(self.sizer)
        self.Fit()

        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    def import_data(self, fam_file_path, Q_file_path, pheno_file_path, column):
        self.importer.import_admix_fam(fam_file_path)
        self.subjects = self.importer.import_admix_Q(Q_file_path)
        self.groups = self.importer.import_admix_pheno(pheno_file_path, column)

    def organise_ancestries(self):
        self.ancestries = defaultdict(list)

        for group in self.groups:
            for key in group.ancestries:
                self.ancestries[key].extend(group.ancestries[key])

    def plot_admix(self):
        # a dummy list
        placeToStart = []

        self.organise_ancestries()

        # populate the list of labels and where they appear
        for eachGroup in range(0, len(self.groups)):
            self.labelsList.append(str(self.groups[eachGroup].name))
            placeToStart.append(len(self.groups[eachGroup].subjects))

        x_shift = 0  # Variable to shift where the x tick appears
        for index in range(0, len(self.groups)):
            x_shift += placeToStart[index]
            self.xtickPos.append(x_shift-placeToStart[index]/2)

        # Specify where each column appears
        ind = np.arange(0, len(self.subjects))

        for key in self.ancestries:
            self.ax.bar(ind, self.ancestries[key], width=1.0)

        self.ax.set_xticks(self.xtickPos)
        self.ax.set_xticklabels(self.labelsList)
