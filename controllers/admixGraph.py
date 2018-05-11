import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from collections import defaultdict
from controllers import importData


class AdmixGraph:
    def __init__(self):
        self.subjects = []
        self.groups = []
        self.heightsList = []
        # Create empty dictionary of lists
        self.ancestries = defaultdict(list)
        self.importer = importData.ImportAdmixData()
        # Create Figure and Axes instances
        self.fig = plt.figure(frameon=False)
        self.fig.tight_layout(pad=0, w_pad=0)
        self.ax = self.fig.subplots(1)
        self.axes = plt.axes()
        self.axes.yaxis.set_major_locator(plt.NullLocator())
        self.axes.xaxis.set_major_formatter(plt.NullFormatter())
        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    def import_ratios(self,fam_file_path,Q_file_path,Phen_file_path, column):
        self.importer.import_admix_fam(fam_file_path)
        self.subjects = self.importer.import_admix_Q(Q_file_path)
        self.groups = self.importer.import_admix_pheno(Phen_file_path, column)

    def plot_admix(self):
        self.ax = self.fig.subplots()
        # attempted to solve the error related to single shape
        ind = np.arange(len(self.subjects))
        print(len(self.groups))

        # clear height list
        self.heightsList = []
        i = 0
        for group in self.groups:
            # calculates where each column appears

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
                    # attempted to create the heights list
                    self.heightsList.append(self.ancestries[key])
                    #print(self.heightsList)



            # Remove white horizontal space between subplots
            self.fig.subplots_adjust(wspace=0.0)

            # Loop through the dictionary plot each ancestry
            for key in range(len(self.heightsList)):
                self.ax.bar(ind, height=self.heightsList[key], width=1.0)

                self.ax.set_frame_on(False)
                self.ax.set_xticks([])
                self.ax.set_yticks([])

            self.ax.set_xlabel(str(group.name))


# Test functionality
graph = AdmixGraph()
fam_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.fam'
Q_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.Q.4'
phen_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.phe'
graph.import_ratios(fam_file_path=fam_fp,Q_file_path=Q_fp,Phen_file_path=phen_fp, column=3)

graph.plot_admix()
plt.show()
