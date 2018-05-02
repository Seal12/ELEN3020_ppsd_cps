import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from controllers import importData

class admixGraph:
    def __init__(self):
        self.subjects = []
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
        pass