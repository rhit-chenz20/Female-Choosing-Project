import copy
import numpy as np
from mesa import Agent


class Female(Agent):
    """
    A female of the general population

    Attributes:
        threshold: the threshold which is used to choose the mate
    """

    def __init__(
        self,
        val, #threshold
        # length of genome
        unique_id,
        model,
        fit
    ):
        """
        Create a new Female.
        """
        super().__init__(unique_id,
        model)
        self.threshold = copy.deepcopy(val)
        self.fitness = 0
        self.fit = fit
        self.mates = []

    # def look(self):
    #     """
    #     Look at the male's fitness
    #     """

    """
    Check to see if mate with the male or not
    """
    def step(self):
        if(self.currentMale >= self.threshold):
            self.mate(self.currentMale)

    def setCurrentMale(self, male):
        self.currentMale = male

    """
    Mate with current male
    """
    def mate(self, male):
        self.mates.append(male)
        if(self.fit == 0):
            self.calFitnessAve()
        elif (self.fit == 1):
            self.calFitnessLow()

    """
    Calculate the female's fitness by averaging her mated males' fitness
    """
    def calFitnessAve(self):
        self.fitness = sum(self.mates) / len(self.mates)

    def calFitnessLow(self):
        self.fitness = min(self.mates)

    """
    Mutate current threshold
    """
    def mutate(self, sigma):
        self.threshold += np.random.normal(0,sigma)

    def getFitness(self):
        return self.fitness
    
    def getThreshold(self):
        return self.threshold

    def getFit(self):
        return self.fit     
    
    def __lt__(self, otherF):
        return self.fitness < otherF.fitness


# class Randomizer():
#     def val(self):
#         return 1
#         # return random.randint(0,100)