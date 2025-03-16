import mesa

class JackOfHeartsModel(mesa.Model):
    def __init__(self, numOfAgents):
        super().__init__()
        
        self.numOfAgents = numOfAgents
        self.grid = mesa.space.MultiGrid(10, 10, torus=True)
        
        
