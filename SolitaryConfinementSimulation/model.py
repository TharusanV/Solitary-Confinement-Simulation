#pip install mesa==2.4

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner


class PlayerAgent(Agent):
    def __init__(self, unique_id, model, isJackOfHeart):
        super().__init__(unique_id, model)
        
        self.occupation = self.random.choice(["Gambler", "Politician", "Teacher", "Police Officer"])
        self.suit = self.random.choice(["Hearts", "Diamonds", "Clubs", "Spades"])
        self.strategy = self.random.choice(["Truthful", "Deceptive", "Random"])
        self.suitGuess = ""
        self.trustLevelsHashMap = {}
        self.sleepDeprived = 0
        
        self.isJackOfHeart = isJackOfHeart

    def step(self): #Step function holds what the agent does as time passes
        pass


    
class JackOfHeartsModel(Model):
    """ Our Model acts as the home for our agents """
    def __init__(self, numOfAgents, width, height):
        self.numOfAgents = numOfAgents
        
        # A space to place our agents in
        self.grid = mesa.space.MultiGrid(width, height, False) #If we wanted the space to wrap set it to True instead of false e.g. go far left you end up on the right

        """
        In the real world, at the best that we can tell, everything moves at the same time. This is not exactly achievable in a simulation
        e.g. if both agents are telling eachother their card suits at the same time it will cause issues in that mid-transaction point. So we use a turn based schedule.
        This RandomActivation makes it so each step, the order won't be the same so sometimes agent A will communicate first with agent B and sometimes the opposite.
        """
        self.schedule = RandomActivation(self)

        self.running = True
        
        for i in range(self.numOfAgents):
            isJackBoolean = False
            if i == self.numOfAgents - 1:
                isJackBoolean = True
                
            agentObj = PlayerAgent(self, i, isJackBoolean)
            self.schedule.add(agentObj) #Adds agent to the schedule defined earlier

            #Instead of just using random, we add self. as to rerun the same randomness each run of the simulation
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agentObj, (x,y))

        #Metrics used to measure the model
        self.datacollector = DataCollector(
            agent_reporters={"SleepDeprived": "sleepDeprived"}
        )
        
        

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        
