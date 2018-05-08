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
