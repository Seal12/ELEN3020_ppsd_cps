from collections import defaultdict


class PopulationGroup:

    def __init__(self, name):
        self.name = name
        self.visible = True
        self.subjects = []
        # Create empty dictionary of lists
        self.ancestries = defaultdict(list)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_visibility(self, visibility):
        self.visible = visibility
