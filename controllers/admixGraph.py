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
        self.ax = self.fig.subplots(ncols=len(self.groups))

        # for each in self.groups:
        #     self.ax.axes[each].xticks([])

        print(len(self.groups))


        i = 0
        for group in self.groups:
            # calculates where each column appears
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



            if len(self.groups) > 1:
                axes = self.ax[i]
            else:
                axes = self.ax

            # Remove white horizontal space between subplots
            # self.fig.tight_layout(pad=0.0,w_pad=0.0)
            # self.fig.subplots_adjust(wspace=0.0)

            


            # Loop through the dictionary plot each ancestry
            for key in self.ancestries:
                axes.bar(ind, height=self.ancestries[key], width=1.0)
                axes.set_frame_on(False)

                axes.set_xticks([])
                axes.set_yticks([])
                # axes.set_yticks([])

                if i > 1:
                    axes.get_shared_y_axes().join(self.ax[i],self.ax[i-1])

            axes.set_xlabel(str(group.name))

            i  += 1
            if i >= len(self.groups):
                break


# Test functionality
graph = AdmixGraph()
fam_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.fam'
Q_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.Q.4'
phen_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.phe'
graph.import_ratios(fam_file_path=fam_fp,Q_file_path=Q_fp,Phen_file_path=phen_fp, column=3)

graph.plot_admix()
plt.show()
