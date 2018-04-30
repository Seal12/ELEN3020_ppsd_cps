import matplotlib.pyplot as plt
from matplotlib import style
from controllers import importData


class PCAGraph:

    def __init__(self, heading):
        self.heading = heading
        self.groups = []
        self.importer = importData.ImportData()
        #Default PC to plot
        self.x = 0
        self.y = 1
        # Create Figure and Axes instances
        self.fig, self.ax = plt.subplots(1)

    def import_fam_file(self, file_path):
        self.importer.import_values(file_path)

    def import_pheno_file(self, file_path):
        self.groups = self.importer.import_pca_pheno(file_path)

    def plot_pca(self, x, y):
        self.x = x
        self.y = y

        plt.xlabel('PC{}'.format(x))
        plt.ylabel('PC{}'.format(y))

        for group in self.groups:
            if group.visible:
                self.ax.scatter(group.pca_dict[x], group.pca_dict[y], marker=group.marker, c=group.colour, s=group.marker_size)
                # Turn off tick labels
                self.ax.set_yticklabels([])
                self.ax.set_xticklabels([])

        return self.fig

    def find_subject(self, subject_id):
        for group in self.groups:
            for subject in group.subjects:
                if subject.id_num == subject_id:
                    return subject

        return 'No subject with that ID'

    def find_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group

        return 1

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


 # testing functionality
# graph = PCAGraph(heading='Random')
# graph.import_fam_file('C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\PCA\\comm-SYMCL.pca.evec')
# graph.import_pheno_file('C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm.phe')
# graph.plot_pca(0,1)
# graph.set_graph_title('PCA')
#
# print(graph.importer.group_names)
# plt.show()

# graph.set_group_marker(group_name='CEU:EUR', marker='x')
# graph.set_group_colour(group_name='CEU:EUR', colour='k')
# graph.set_all_markers(size=1, marker='o')
# graph.set_group_marker_size(group_name='CHD:ASN', size=10)
# #graph.plot_pca(0,1)
#
# #plt.show()