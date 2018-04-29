import matplotlib.pyplot as plt
from controllers import importData


class PCAGraph:
   # fig = plt.figure()

    def __init__(self, heading):
        self.heading = heading
        self.groups = []
        self.importer = importData.ImportData()

    def import_fam_file(self, file_path):
        self.importer.import_values(file_path)

    def import_pheno_file(self, file_path):
        self.groups = self.importer.import_pca_pheno(file_path)

    def plot_pca(self, x, y):
        for group in self.groups:
            pc_x = []
            pc_y = []
            for subject in group.subjects:
                pc_x.append(subject.values[x])
                pc_y.append(subject.values[y])

            plt.scatter(pc_x, pc_y, marker=group.marker, c=group.colour)

        plt.show()


 # testing functionality
graph = PCAGraph(heading='Random')
graph.import_fam_file('C:/Users/Phatho/Desktop/ELEN3020_ppsd_cps/exampleData/PCA/comm-SYMCL.pca.evec')
graph.import_pheno_file('C:/Users/Phatho/Desktop/ELEN3020_ppsd_cps/exampleData/PCA/comm.phe')
graph.plot_pca(3,1)