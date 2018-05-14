#!/usr/bin/env python

"""pcaGroup.py: Model for PCA group inherits from populationGroup
    the main difference between a PCA group and a normal population group is marker information(group icon)
"""

__author__ = "Phatho Pukwana"
__credits__ = ["Phatho Pukwana"]
__email__ = "1388857@students.wits.ac.za"
__status__ = "Development"

from models.populationGroup import PopulationGroup


class PCAGroup(PopulationGroup):

    def __init__(self, name):
        # Icon for the group
        self.name = name
        self.marker = None
        self.marker_size= None
        self.colour = None
        super(PCAGroup, self).__init__(name)

    def add_subject(self, subject):
        """Adds a subject to group(in base class) and adds subjects pc data to collective data dictionary

        Keyword arguments:
            subject -- individual subject that'll be added to the group
        """
        super(PCAGroup, self).add_subject(subject)

        # Adds subjects pc data to group data dictionary
        for i in range(0, len(subject.values)):
            self.data_dict[i].append(subject.values[i])

