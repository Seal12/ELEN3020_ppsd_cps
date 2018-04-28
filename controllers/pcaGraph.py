import matplotlib.pyplot as plt
from matplotlib import style
from controllers import importData


class PCAGraph:

    def __init__(self, heading):
        self.heading = heading
        self.groups = []
        self.importer = importData.ImportData()

    def import_fam_file(self, file_path):
        self.importer.import_values(file_path)

    def import_pheno_file(self, file_path):
        self.groups = self.importer.import_pca_pheno(file_path)

    def plot_pca(self, x, y):
        style.use('ggplot')

        # Create Figure and Axes instances
        fig, ax = plt.subplots(1)

        plt.xlabel('PC{}'.format(x))
        plt.ylabel('PC{}'.format(y))

        for group in self.groups:
            if group.visible:
                ax.scatter(group.pca_dict[x], group.pca_dict[y], marker=group.marker, c=group.colour)
                # Turn off tick labels
                ax.set_yticklabels([])
                ax.set_xticklabels([])

        plt.show()

    def search(self, id_num):
        


 # testing functionality
graph = PCAGraph(heading='Random')
graph.import_fam_file('C:\\Users\\Apprentice\\Documents\\GitHub\\ELEN3020_ppsd_cps\\exampleData\PCA\\comm-SYMCL.pca.evec')
graph.import_pheno_file('C:\\Users\\Apprentice\\Documents\\GitHub\\ELEN3020_ppsd_cps\\exampleData\\PCA\\comm.phe')
graph.plot_pca(0,1)