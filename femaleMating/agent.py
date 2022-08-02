import copy
from abc import abstractmethod

class Female():
    def __init__(
        self,
        fit,
        flatcost,
        fitBase
    ):
        """
        Create a new Female.
        """
        self.fitness = 0
        self.fit = fit
        self.mates = []
        self.fitbase = fitBase
        self.flatcost = flatcost

    
    """
    Check to see if mate with the male or not
    """
    def step(self):
        self.mate()
        self.calFitness()

    def calFitness(self):
        self.fit.cal_fitness(self)
        self.adjustCost()
    
    def setCurrentMale(self, male):
        self.currentMale = male

    @abstractmethod
    def mate(self):
        pass

    @abstractmethod
    def mutate(self, sigma, ran):
        pass
            
    def adjustCost(self):
        self.flatCost()
        self.varCost()

    def flatCost(self):
        self.fitness = self.fitness - self.flatcost * len(self.mates)

    def varCost(self):
        pass

    def __lt__(self, otherF):
        return self.fitness < otherF.fitness


class FemaleThreshold(Female):
    """
    A female of the general population

    Attributes:
        threshold: the threshold which is used to choose the mate
    """

    def __init__(
        self,
        val,
        fit,
        flatcost,
        fitbase
    ):
        super().__init__(fit, flatcost, fitbase)
        self.threshold = copy.deepcopy(val)

    """
    Mate with current male
    """
    def mate(self):
        if(self.currentMale >= self.threshold):
            self.mates.append(self.currentMale)
            return True
        else:
            return False

    """
    Mutate current threshold
    """
    def mutate(self, sigma, ran):
        self.threshold += ran.valmu(sigma)

class FemaleGenome(Female):
    def __init__(
        self,
        genome,
        fit,
        memoryLength,
        flatcost,
        fitbase,
        ran
    ):
        """
        Create a new Female.
        """
        super().__init__(fit,fitbase, flatcost)
        self.genome = copy.deepcopy(genome)
        self.memory = [None] * memoryLength
        self.threshold = 0
        self.geneindex = 0
        self.flatcost = flatcost
        self.ran = ran
        self.mating_steps = 0

    def step(self):
        self.memorize()
        self.calThreshold(self.ran)
        if(self.genome[self.geneindex] == 1):
            self.mate()
            self.mating_steps += 1
        self.geneindex+=1

    def memorize(self):
        notfull = True
        for y in range(len(self.memory)):
            if(self.memory[y] == None):
                self.memory[y] = self.currentMale
                notfull = False
                break
        
        if(notfull and len(self.memory) > 0):
            for x in range(len(self.memory) - 1):
                self.memory[x] = self.memory[x+1]
            self.memory[len(self.memory) - 1] = self.currentMale

    def mate(self):
        if(self.currentMale >= self.threshold):
            self.mates.append(self.currentMale)
            return True
        else:
            return False
    
    def calThreshold(self, ran):
        filtered = list(filter(lambda male: male != None, self.memory))
        if(len(filtered) != 0):
            self.threshold = sum(filtered) / len(filtered)
            # self.threshold = ran.norran(self.malesigma,sum(filtered) / len(filtered))
        else:
            self.threshold = 0

    def mutate(self, lamda, ran):
        size = ran.poisson(lamda)
        self.selected = []
        if(size > len(self.genome)):
            size = len(self.genome)
        for x in range(size):
            index = ran.ranInt(len(self.genome))
            while(index in self.selected):
                index = ran.ranInt(len(self.genome))
            self.selected.append(index)
            if(self.genome[index] == 1):
                self.genome[index] = 0
            elif(self.genome[index] == 0):
                self.genome[index] = 1

