import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from collections import defaultdict
from controllers import importData


class AdmixGraph:
    def __init__(self):
        self.subjects = []
        self.groups = []
        # Create empty dictionary of lists
        self.ancestries = defaultdict(list)
        self.importer = importData.ImportAdmixData()
        # Create Figure and Axes instances
        self.fig = plt.figure()
        self.ax = self.fig.subplots(1)
        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    def import_ratios(self,fam_file_path,Q_file_path,Phen_file_path, column):
        self.importer.import_admix_fam(fam_file_path)
        self.subjects = self.importer.import_admix_Q(Q_file_path)
        self.groups = self.importer.import_admix_pheno(Phen_file_path, column)

    def plot_admix(self):
        self.ax = self.fig.subplots(nrows=1, ncols=len(self.groups))
        # I actually don't know what ths value does
        #ind = np.arange(len(self.subjects))
        i = 0
        for group in self.groups:
            ind = np.arange(len(group.subjects))
            self.ancestries = defaultdict(list)
            # Populate the dictionary with ancestry values
            for subject in group.subjects:
                # Calculate the height of the ancestry bar graphs
                for key in range(0, len(subject.values)):
                    value = 0
                    for j in range(key, len(subject.values)):
                        value += subject.values[j]
                    # Store the heights in a dictionary of lists
                    self.ancestries[key].append(value)
            # Loop through the dictionary plot each ancestry
            axes = self.ax[i]
            for key in self.ancestries:
                axes.bar(ind, height=self.ancestries[key], width=1.0)
                #self.fig.suptitle(str(index[group]))
            print((self.ancestries[3]))


            i  += 1
            if i >= len(self.groups):
                break
        #self.fig.set_label('admix')






# Test functionality
graph = AdmixGraph()
fam_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.fam'
Q_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.Q.4'
phen_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.phe'
graph.import_ratios(fam_file_path=fam_fp,Q_file_path=Q_fp,Phen_file_path=phen_fp, column=5)

graph.plot_admix()
# print(str(graph.subjects;;''))
plt.show()
