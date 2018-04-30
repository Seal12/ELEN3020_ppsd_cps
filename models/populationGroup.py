class PopulationGroup:

    def __init__(self, name):
        self.name = name
        self.visible = True
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_visibility(self, visibility):
        self.visible = visibility
