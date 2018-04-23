from models import populationGroup


class PCAGroup(populationGroup):

    def __init__(self, marker, colour):
        # Icon for the group
        self.marker = marker

        # Colour of the marker
        self.colour = colour