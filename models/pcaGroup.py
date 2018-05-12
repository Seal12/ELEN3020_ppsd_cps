#!/usr/bin/env python

"""pcaGroup.py: Description"""

__author__ = "Phatho Pukwana"
__credits__ = ["Phatho Pukwana"]
__email__ = "1388857@students.wits.ac.za"
__status__ = "Development"

from models.populationGroup import PopulationGroup
from collections import defaultdict


class PCAGroup(PopulationGroup):

    def __init__(self, name):
        # Icon for the group
        self.marker = None
        self.marker_size= None
        self.colour = None
        super(PCAGroup, self).__init__(name)

    def add_subject(self, subject):
        super(PCAGroup, self).add_subject(subject)
        self.add_to_pca_dictionary(subject)

    def add_to_pca_dictionary(self, subject):
        for i in range(0, len(subject.values)):
            self.data_dict[i].append(subject.values[i])
