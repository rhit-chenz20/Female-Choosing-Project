import copy
import numpy as np
from mesa import Agent
import math

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
        self.adjustCost()

    def calFitness(self):
        if(self.fit == 0):
            self.calFitnessAve()
        elif (self.fit == 1):
            self.calFitnessLow()
        elif(self.fit == 2):
            self.calFitnessWeighted()
    
    def setCurrentMale(self, male):
        self.currentMale = male

    def mate(self):
        pass
    
    """
    Calculate the female's fitness by averaging her mated males' fitness
    """
    def calFitnessAve(self):
        if(len(self.mates) != 0):
            self.fitness = sum(self.mates) / len(self.mates)
        else:
            self.fitness = 0

    def calFitnessLow(self):
        if(len(self.mates) == 0):
            self.fitness = 0
        else: 
            self.fitness = min(self.mates)

    def calFitnessWeighted(self):
        for x in range(len(self.mates)):
            self.fitness += (math.pow(self.fitbase, len(self.mates - x)) * self.mates[x])
    
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
        flatcost = 0,
        fitbase = 0
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
        fitbase
    ):
        """
        Create a new Female.
        """
        super().__init__(fit,fitbase, flatcost)
        #list
        self.genome = copy.deepcopy(genome)
        self.memory = [None] * memoryLength
        self.threshold = 0
        self.geneindex = 0
        self.flatcost = flatcost

    def step(self):
        self.memorize()
        self.calThreshold()
        if(self.genome[self.geneindex] == 1):
            self.mate()
        self.calFitness()
        self.adjustCost()
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
    
    def calThreshold(self):
        filtered = list(filter(lambda male: male != None, self.memory))
        if(len(filtered) != 0):
            self.threshold = sum(filtered) / len(filtered)
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

