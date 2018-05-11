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
        # A list of labels
        self.labelsList = []
        # a list of locations the labels appear
        self.xtickPos = []
        self.importer = importData.ImportAdmixData()
        # Create Figure and Axes instances
        self.fig = plt.figure()
       # self.fig.tight_layout(pad=0, w_pad=0)
        self.ax = self.fig.subplots(1)
        self.ax.yaxis.set_major_locator(plt.NullLocator())
        self.ax.xaxis.set_major_formatter(plt.NullFormatter())
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

        # a dummy list
        placeToStart = []

        self.organise_ancestries()

        # populate the list of labels and where they appear
        for eachGroup in range(0, len(self.groups)):
            self.labelsList.append(str(self.groups[eachGroup].name))
            #print(str(self.groups[eachGroup].name))
            placeToStart.append(len(self.groups[eachGroup].subjects))

        print (placeToStart)
        # variable to shift where the x tick appears
        xshift = 0
        for index in range(0, len(self.groups)):
            xshift += placeToStart[index]
            self.xtickPos.append(xshift-placeToStart[index]/2)


        # where each column appears
        ind = np.arange(0, len(self.subjects))

        for key in self.ancestries:
            self.ax.bar(ind, self.ancestries[key], width=1.0)

        self.ax.set_xticks(self.xtickPos)
        self.ax.set_xticklabels(self.labelsList)


# Test functionality
graph = AdmixGraph()
fam_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.fam'
Q_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.Q.4'
phen_fp = 'C:\\Users\\Cedrick\\PycharmProjects\\ELEN3020_ppsd_cps\\exampleData\\Admix\\small.phe'
graph.import_ratios(fam_file_path=fam_fp,Q_file_path=Q_fp,Phen_file_path=phen_fp, column=3)

graph.plot_admix()
plt.show()
