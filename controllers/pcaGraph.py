import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
import wx

from controllers import importData


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

    def import_data(self, evec_file_path, pheno_file_path, column):
        self.importer.import_pca_evec(file_path=evec_file_path)
        self.groups = self.importer.import_pca_pheno(file_path=pheno_file_path, column=column)

    def import_pca_file(self, file_path):
        self.importer.import_pca_evec(file_path)

    def import_pheno_file(self, file_path, column):
        self.groups = self.importer.import_pca_pheno(file_path, column)

    def plot_pca(self, pc_x, pc_y):
        self.pc_x = pc_x
        self.pc_y = pc_y

        plt.xlabel('PC{}'.format(pc_x))
        plt.ylabel('PC{}'.format(pc_y))

        # Plot each group individually
        for group in self.groups:
            if group.visible:
                self.ax.scatter(group.pca_dict[pc_x], group.pca_dict[pc_y], label=group.name, marker=group.marker, c=group.colour, s=group.marker_size, zorder=3)

        # Create legend
        self.ax.legend(loc='best', frameon=False, prop={'size': 7})

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
        minor_x_step = (x_max - x_min)/10
        minor_y_step = (y_max - y_min)/10
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

        self.ax.set_title("PC{} vs. PC{}".format(pc_x, pc_y))

        return self.figure

    def find_subject(self, subject_id):
        for group in self.groups:
            for subject in group.subjects:
                if subject.id_num == subject_id:
                    return subject

        return 'No subject with id {}'.format(subject_id)

    def find_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group

        return 'No group by the name {}'.format(group_name)

    def set_all_markers(self, marker, size):
        for group in self.groups:
            group.marker = marker
            group.marker_size = size

    def set_group_marker_size(self, group_name, size):
        group = self.find_group(group_name)
        group.marker_size = size

    def set_group_marker(self,group_name, marker):
        group = self.find_group(group_name)
        group.marker = marker
        # return self.plot_pca(self.pcaX, self.pcaY)

    def set_group_colour(self,group_name, colour):
        group = self.find_group(group_name)
        group.colour = colour
        # return self.plot_pca(self.pcaX, self.pcaY)

    def set_group_visibility(self, group_name, visible):
        group = self.find_group(group_name)
        group.visible = visible

    def set_graph_title(self, title):
        self.ax.set_title(title)