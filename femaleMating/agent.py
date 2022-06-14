import copy

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
    ):
        """
        Create a new Female.
        """
        super().__init__()
        self.threshold = copy.deepcopy(val)
        self.fitness = 0
        self.mates = []

    # def look(self):
    #     """
    #     Look at the male's fitness
    #     """

    """
    Check to see if mate with the male or not
    """
    def step(self, male):
        if(male >= self.threshold):
            self.mate(male)

    """
    Mate with current male
    """
    def mate(self, male):
        self.mates.append(male)
        self.calFitness()

    """
    Calculate the female's fitness by averaging her mated males' fitness
    """
    def calFitness(self):
        self.fitness = sum(self.mates) / len(self.mates)

    """
    Mutate current threshold
    """
    def mutate(self):
        ""
        
    def getFitness(self):
        return self.fitness
    
    def getThreshold(self):
        return self.threshold

class Randomizer():
    def val(self):
        return 1
        # return random.randint(0,100)