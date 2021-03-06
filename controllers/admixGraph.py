#!/usr/bin/env python

"""
admixGraph.py: This file is responsible for creating the admixture plot
"""

__author__ = "Phatho Pukwana, Cedrick Platt"
__credits__ = ["Phatho Pukwana", "Cedrick Platt", "Seale Rapolai"]
__email__ = "1388857@students.wits.ac.za, 1500728@students.wits.ac.za"
__status__ = "Development"

import numpy as np
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib import rcParams

from controllers import importData
from views import graphPopupMenu


class AdmixGraph(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.groups = []
        # This is the data that will be plotted
        self.ancestries = defaultdict(list)
        # List of labels
        self.labelsList = []
        # List of locations the labels appear
        self.x_tickPos = []
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

        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()

        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    # <editor-fold desc="Importing data methods">

    def import_data(self, fam_file_path, Q_file_path, pheno_file_path, column):
        """Imports the data files for admixture plot

        Keyword arguments:
            fam_file_path: -- the file path of the fam file
            Q_file_path: -- the file path of the Q file
            pheno_file_path: -- the file path of the phenotype file
            column: -- column where the relevant phenotype data is
        """

        self.importer.import_admix_fam(fam_file_path)
        self.importer.import_admix_Q(Q_file_path)
        self.groups = self.importer.import_admix_pheno(pheno_file_path, column)

    # </editor-fold>

    # <editor-fold desc="Plotting">

    def organise_plotting_data(self):
        """Ensure that the data is in the correct format to be plotted

            :functionality:
                1:Ensures that subjects in the same group are plotted together
                2:Ensures groups will be plotted in the order in which they are stored
                3:Ensures that groups which are hidden are not plotted

        """

        self.ancestries = defaultdict(list)

        for group in self.groups:
            if group.visible:
                for key in group.data_dict:
                    self.ancestries[key].extend(group.data_dict[key])

    def plot_admix(self, title=None):
        """Creates the admixture plot

            This method plots a set of bar graphs per ancestry,
            the bar graph of each ancestry are plotted on top of each other,
            the ancestry at the very top is always a height of 100,
            subsequent ancestries heights are the sum of all ancestries below
        """

        # a dummy list
        place_to_start = []

        # Organise the data by group
        self.organise_plotting_data()

        # populate the list of labels and where they appear
        for eachGroup in range(0, len(self.groups)):
            self.labelsList.append(str(self.groups[eachGroup].name))
            place_to_start.append(len(self.groups[eachGroup].subjects))

        x_shift = 0  # Variable to shift where the x tick appears
        for index in range(0, len(self.groups)):
            x_shift += place_to_start[index]
            self.x_tickPos.append(x_shift - place_to_start[index] / 2)

        # Specify where each column appears
        ind = np.arange(0, len(self.importer.subject_list))

        # Plot the data
        for key in self.ancestries:
            self.ax.bar(ind, self.ancestries[key], width=1.0)

        # Set the ticks
        self.ax.set_xticks(self.x_tickPos)
        self.ax.set_xticklabels(self.labelsList)

        self.ax.set_title(title)

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.OnPlotClick)

    def OnPlotClick(self, event):
        if event.button == 3:
            x, y = self.GetSize()
            x = event.x
            y = y - event.y - 30
            self.PopupMenu(graphPopupMenu.GraphPopupMenu(self, "Admix"), (x, y))

    def refresh_graph(self):
        self.fig.canvas.draw()

    def change_labling(self, title=None, ylabel=None, xlabel=None):
        self.ax.set_title(title)

        self.fig.canvas.draw()

    # </editor-fold>
