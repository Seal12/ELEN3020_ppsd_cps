class Subject:

    def __init__(self, id, values, group):
        # Subject ID
        self.id = id

        # List of ancestry ratios(Admix) or list of PC values(PCA)
        self.values = values

        self.group = group

        self.marker = None

    def set_Marker(self, marker):
        self.marker = marker