#!/usr/bin/env python

"""
pcaGraph.py: This file is responsible for generating and customising a PCA plot
"""

__author__ = "Phatho Pukwana"
__credits__ = ["Phatho Pukwana, Seale Rapolai"]
__email__ = "1388857@students.wits.ac.za"
__status__ = "Development"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
import wx

from controllers import importData
from views import graphPopupMenu


class PCAGraph(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.groups = []
        self.importer = importData.ImportPCAData()
        # Default PC to plot
        self.pc_x = 0
        self.pc_y = 1
        # Create Figure and Axes instances
        self.figure = plt.figure()
        self.ax = self.figure.subplots(1)
        # User Interface settings
        self.canvas = FigureCanvas(self, -1, self.figure)
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

    def import_data(self, evec_file_path, pheno_file_path, column=0):
        """
        Imports the data files required for PCA plot

        :Note: none of the data files are optional and both evec and pheno files are required to generate a plot

        Keyword arguments:
            evec_file_path -- the file path of the evec file
            pheno_file_path -- the file path of the phenotype file
            column -- column where the relevant phenotype data is
        """

        self.importer.import_pca_evec(file_path=evec_file_path)
        self.groups = self.importer.import_pca_pheno(file_path=pheno_file_path, column=column)

    # </editor-fold>

    # <editor-fold desc="Plotting">

    def plot_pca(self, pc_x=0, pc_y=1, title=None):
        """
        Generates a scatter plot of PCA data

        Keyword arguments:
            pc_x -- the principle component to be plotted on the x axis(default 0)
            pc_y -- the principle component to be plotted on the y axis(default 1)

        Each groups data is plotted as an individual scatter plot onto the same subplot
        """
        max_pc = len(self.importer.subject_list[0].values)

        if pc_x > max_pc:
            pc_x = max_pc

        if pc_y > max_pc:
            pc_y = max_pc

        self.pc_x = pc_x
        self.pc_y = pc_y

        plt.xlabel('PC{}'.format(pc_x))
        plt.ylabel('PC{}'.format(pc_y))

        # Plot each group individually
        for group in self.groups:
            if group.visible:
                self.ax.scatter(group.data_dict[pc_x], group.data_dict[pc_y], label=group.name, marker=group.marker, c=group.colour, s=group.marker_size, zorder=3)

        # Create legend
        self.ax.legend(loc='best', frameon=False, prop={'size': 7})

        self.set_up_grid(grid_division=10)

        if title is None:
            self.ax.set_title("PC{} vs. PC{}".format(pc_x, pc_y))
        else:
            self.ax.set_title(title)

        self.cid = self.figure.canvas.mpl_connect('button_press_event', self.OnPlotClick)

        return self.figure

    # </editor-fold>

    def OnPlotClick(self, event):
        if event.button == 3:
            x, y = self.GetSize()
            x = event.x
            y = y - event.y - 30
            self.PopupMenu(graphPopupMenu.GraphPopupMenu(self, "PCA"), (x, y))

    def set_up_grid(self, grid_division):
        """
        Creates a grid for the scatter plot

        Keyword arguments:
            grid_division: -- How many times the grid should be subdivided
        """

        # Get the min and max values of the plot
        v = plt.axis()
        x_min = v[0]
        x_max = v[1]
        y_min = v[2]
        y_max = v[3]

        # Calculate major ticks
        major_x_step = (x_max - x_min)/2
        major_y_step = (y_max - y_min)/2
        x_major_ticks = np.arange(x_min, x_max, major_x_step)
        y_major_ticks = np.arange(y_min, y_max, major_y_step)

        # Calculate minor ticks
        minor_x_step = (x_max - x_min)/grid_division
        minor_y_step = (y_max - y_min)/grid_division
        x_minor_ticks = np.arange(x_min, x_max, minor_x_step)
        y_minor_ticks = np.arange(y_min, y_max, minor_y_step)

        # Set the grid spacing to the calculated ticks
        self.ax.set_xticks(x_major_ticks)
        self.ax.set_xticks(x_minor_ticks, minor=True)
        self.ax.set_yticks(y_major_ticks)
        self.ax.set_yticks(y_minor_ticks, minor=True)

        # Turn off tick labels
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])

        # Set the grid
        self.ax.grid(which='major', alpha=0.5, zorder=0)
        self.ax.grid(which='minor', alpha=0.5, ls='dotted', zorder=0)

    # <editor-fold desc="Searching Functionality">
    def find_subject(self, subject_id):
        """
        Finds a subject based of subjects identification number

        Keyword arguments:
            subject_id -- subjects identification number (String)

        :returns:
            subject

            if subject is not found returns a string message
        """
        for group in self.groups:
            for subject in group.subjects:
                if subject.id_num == subject_id:
                    return subject

        return 'No subject with id {}'.format(subject_id)

    def find_group(self, group_name):
        """
        Finds a group based of groups name

        Keyword arguments:
            group_name: -- subjects identification number (String)

        :returns:
            group

            if group is not found returns a string message
        """
        for group in self.groups:
            if group.name == group_name:
                return group

        return 'No group by the name {}'.format(group_name)

    # </editor-fold>

    # <editor-fold desc="Customization Functionality">
    def set_all_markers(self, marker, size):
        for group in self.groups:
            group.marker = marker
            group.marker_size = size

    def set_group_marker_size(self, group_name, size):
        group = self.find_group(group_name)
        group.marker_size = size

    def set_group_marker(self,group_name, marker):
        print("change {} with {}".format(group_name, marker))
        group = self.find_group(group_name)
        group.marker = marker
        self.refresh_graph()

    def set_group_colour(self,group_name, colour):
        group = self.find_group(group_name)
        group.colour = colour

    def set_group_visibility(self, group_name, visible):
        group = self.find_group(group_name)
        group.visible = visible

    def set_graph_title(self, title):
        self.ax.set_title(title)

    def get_groups(self):
        return self.groups

    def refresh_graph(self):
        self.figure.canvas.draw()

    def change_labling(self, title=None, ylabel=None, xlabel=None):
        self.ax.set_title(title)

        self.figure.canvas.draw()
    # </editor-fold>

