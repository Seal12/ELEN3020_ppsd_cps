from models.populationGroup import PopulationGroup


class PCAGroup(PopulationGroup):

    def __init__(self, name):
        # Icon for the group
        self.marker = None
        self.colour = None
        super(PCAGroup, self).__init__(name)

    def add_subject(self, subject):
        super(PCAGroup, self).add_subject(subject)
