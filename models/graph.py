#!/usr/bin/env python

"""graph.py: Description"""

__author__ = "Seale Rapolai"
__credits__ = ["Seale Rapolai"]
__email__ = "1098005@students.wits.ac.za"
__status__ = "Development"


class Graph:
    def __init__(self, id, type, graphPanel):
        self.id = id
        self.graphPanel = graphPanel
        self.type = type


    def set_GraphPanel(self, graphPanel):
        self.graphPanel = graphPanel

    def get_GraphPanel(self):
        return self.graphPanel

    def get_Type(self):
        return self.type
