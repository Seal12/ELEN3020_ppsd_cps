import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from controllers import importData


class PCAGraph:

    def __init__(self):
        self.groups = []
        self.importer = importData.ImportPCAData()
        # Default PC to plot
        self.x = 0
        self.y = 1
        # Create Figure and Axes instances
        self.fig = plt.figure()
        self.ax = self.fig.subplots(1)
        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    def import_data(self, evec_file_path, pheno_file_path, column):
        self.importer.import_pca_evec(file_path=evec_file_path)
        self.groups = self.importer.import_pca_pheno(file_path=pheno_file_path, column=column)

    def plot_pca(self, x, y):
        self.x = x
        self.y = y

        plt.xlabel('PC{}'.format(x))
        plt.ylabel('PC{}'.format(y))

        # Plot each group individually
        for group in self.groups:
            if group.visible:
                self.ax.scatter(group.pca_dict[x], group.pca_dict[y], label=group.name, marker=group.marker, c=group.colour, s=group.marker_size, zorder=3)

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

        return self.fig

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
        # return self.plot_pca(self.x, self.y)

    def set_group_colour(self,group_name, colour):
        group = self.find_group(group_name)
        group.colour = colour
        # return self.plot_pca(self.x, self.y)

    def set_group_visibility(self, group_name, visible):
        group = self.find_group(group_name)
        group.visible = visible

    def set_graph_title(self, title):
        self.ax.set_title(title)

# Testing functionality
graph = PCAGraph()
evec_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm-SYMCL.pca.evec'
pheno_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm.phe'

graph.import_data(evec_file_path=evec_fp, pheno_file_path=pheno_fp, column=3)

graph.plot_pca(0,2)
graph.set_graph_title('PCA')

print(graph.importer.group_names)
plt.show()

# # graph.set_group_marker(group_name='CEU:EUR', marker='x')
# # graph.set_group_colour(group_name='CEU:EUR', colour='k')
# # graph.set_all_markers(size=1, marker='o')
# # graph.set_group_marker_size(group_name='CHD:ASN', size=10)
# # #graph.plot_pca(0,1)
# #
# # #plt.show()