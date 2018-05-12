#!/usr/bin/env python

"""populationGroup.py: population group model storing the groups subjects and the collective data of all subjects in the group in a dictionary"""

__author__ = "Phatho Pukwana"
__credits__ = ["Phatho Pukwana"]
__email__ = "1388857@students.wits.ac.za"
__status__ = "Development"

from collections import defaultdict


class PopulationGroup:

    def __init__(self, name):
        self.name = name
        self.visible = True
        self.subjects = []
        # Create empty dictionary of lists
        self.data_dict = defaultdict(list)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_visibility(self, visibility):
        self.visible = visibility
