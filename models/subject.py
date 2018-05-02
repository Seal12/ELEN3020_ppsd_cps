class Subject:

    def __init__(self, id_num, values):
        # Subject ID
        self.id_num = id_num

        # List of ancestry ratios(Admix) or list of PC values(PCA)
        self.values = values

        self.marker = None

        self.group = None

    def set_marker(self, marker):
        self.marker = marker

    def set_group(self, group):
        self.group = group
