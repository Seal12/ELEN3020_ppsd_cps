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
        self.pcaX = 0
        self.pcaY = 1
        # Create Figure and Axes instances
        self.figure = plt.figure()
        self.ax = self.figure.subplots(1)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.RIGHT | wx.TOP | wx.GROW)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def import_pca_file(self, file_path):
        self.importer.import_pca_evec(file_path)

    def import_pheno_file(self, file_path, column):
        self.groups = self.importer.import_pca_pheno(file_path, column)

    def plot_pca(self, pcaX, pcaY):
        self.pcaX = pcaX
        self.pcaY = pcaY

        plt.xlabel('PC{}'.format(pcaX))
        plt.ylabel('PC{}'.format(pcaY))

        # Plot each group individually
        for group in self.groups:
            if group.visible:
                self.ax.scatter(group.pca_dict[pcaX], group.pca_dict[pcaY], label=group.name, marker=group.marker, c=group.colour, s=group.marker_size, zorder=3)

        # Create legend
        self.ax.legend(loc='best', frameon=False, prop={'size': 7})

        # Set the ticks
        v = plt.axis()
        x_min = v[0]
        x_max = v[1]
        y_min = v[2]
        y_max = v[3]

        major_x_step = (x_max - x_min)/2
        major_y_step = (y_max - y_min)/2
        x_major_ticks = np.arange(x_min, x_max, major_x_step)
        y_major_ticks = np.arange(y_min, y_max, major_y_step)

        minor_x_step = (x_max - x_min)/10
        minor_y_step = (y_max - y_min)/10
        x_minor_ticks = np.arange(x_min, x_max, minor_x_step)
        y_minor_ticks = np.arange(y_min, y_max, minor_y_step)

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

        self.ax.set_title("Title")

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

        return 'No group with that name'

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

# Testing functionality
# graph = PCAGraph()
# graph.import_fam_file('C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm-SYMCL.pca.evec')
# graph.import_pheno_file('C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm.phe')
#
# graph.plot_pca(0,2)
# graph.set_graph_title('PCA')
#
# print(graph.importer.group_names)
# plt.show()

# # graph.set_group_marker(group_name='CEU:EUR', marker='x')
# # graph.set_group_colour(group_name='CEU:EUR', colour='k')
# # graph.set_all_markers(size=1, marker='o')
# # graph.set_group_marker_size(group_name='CHD:ASN', size=10)
# # #graph.plot_pca(0,1)
# #
# # #plt.show()