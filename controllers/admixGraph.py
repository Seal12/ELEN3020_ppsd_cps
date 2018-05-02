import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from collections import defaultdict
from controllers import importData


class AdmixGraph:
    def __init__(self):
        self.subjects = []
        # Create empty dictionary of lists
        self.ancestries = defaultdict(list)
        self.importer = importData.ImportAdmixData()
        # Create Figure and Axes instances
        self.fig = plt.figure()
        self.ax = self.fig.subplots(1)
        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    def import_ratios(self,fam_file_path,Q_file_path):
        self.importer.import_admix_fam(fam_file_path)
        self.subjects = self.importer.import_admix_Q(Q_file_path)

    def plot_admix(self):
        # I actually don't know what ths value does
        ind = np.arange(len(self.subjects))

        # Populate the dictionary with ancestry values
        for subject in self.subjects:
            # Calculate the height of the ancestry bar graphs
            for key in range(0, len(subject.values)):
                value = 0
                for j in range(key, len(subject.values)):
                    value += subject.values[j]
                # Store the heights in a dictionary of lists
                self.ancestries[key].append(value)

        # Loop through the dictionary plot each ancestry
        for key in self.ancestries:
            self.ax.bar(ind, height=self.ancestries[key],width=1.0)

# Test functionality
graph = AdmixGraph()
fam_fp = 'C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.fam'
Q_fp = 'C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.Q.4'
graph.import_ratios(fam_file_path=fam_fp,Q_file_path=Q_fp)

graph.plot_admix()

plt.show()
