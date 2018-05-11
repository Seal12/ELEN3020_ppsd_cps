import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from collections import defaultdict
from controllers import importData


class AdmixGraph:
    def __init__(self):
        self.subjects = []
        self.groups = []
        self.ancestries = defaultdict(list)
        self.importer = importData.ImportAdmixData()
        # Create Figure and Axes instances
        self.fig = plt.figure()
       # self.fig.tight_layout(pad=0, w_pad=0)
        self.ax = self.fig.subplots(1)
        # self.axes = plt.axes()
        # self.axes.yaxis.set_major_locator(plt.NullLocator())
        # self.axes.xaxis.set_major_formatter(plt.NullFormatter())
        # Set Font
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Tahoma']

    def import_ratios(self,fam_file_path,Q_file_path,Phen_file_path, column):
        self.importer.import_admix_fam(fam_file_path)
        self.subjects = self.importer.import_admix_Q(Q_file_path)
        self.groups = self.importer.import_admix_pheno(Phen_file_path, column)

    def organise_ancestries(self):
        self.ancestries = defaultdict(list)

        for group in self.groups:
            for key in group.ancestries:
                self.ancestries[key].extend(group.ancestries[key])

    def plot_admix(self):
        # Swapping the order of group 0 and group 3
        # temp = self.groups[3]
        # self.groups[3] = self.groups[0]
        # self.groups[0] = temp

        self.organise_ancestries()

        ind = np.arange(0, len(self.subjects))

        for key in self.ancestries:
            self.ax.bar(ind, self.ancestries[key], width=1.0)

        # self.ax = self.fig.subplots(ncols=len(self.groups))

        # for each in self.groups:
        #     self.ax.axes[each].xticks([])

        # print(len(self.groups))
        #
        #     # Loop through the dictionary plot each ancestry
        #     for key in self.ancestries:
        #         axes.bar(ind, height=self.ancestries[key], width=1.0)
        #         axes.set_frame_on(False)
        #
        #         axes.set_xticks([])
        #         axes.set_yticks([])
        #         # axes.set_yticks([])
        #
        #         if i > 1:
        #             axes.get_shared_y_axes().join(self.ax[i],self.ax[i-1])
        #
        #     axes.set_xlabel(str(group.name))
        #
        #     i  += 1
        #     if i >= len(self.groups):
        #         break


# Test functionality
graph = AdmixGraph()
fam_fp = 'C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.fam'
Q_fp = 'C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.Q.4'
phen_fp = 'C:\\Users\\Phatho\\Desktop\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.phe'
graph.import_ratios(fam_file_path=fam_fp,Q_file_path=Q_fp,Phen_file_path=phen_fp, column=3)

graph.plot_admix()
plt.show()
