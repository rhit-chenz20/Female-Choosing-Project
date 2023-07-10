import random
import numpy as np
from fitness_function import FitnessFunction
from agent import Female
from copy import deepcopy

class FemaleMatingModel():
    """
    args: femaleSize, maleSigma,fitnessFunction, filename, seed, fitbase
    """
    def __init__(
        self,
        args,
        genome
    ):
        if args.seed!=-1:
            self.seed = args.seed
        else:
            self.seed = np.random.randint(0,100000)
        self.ran = np.random.seed(self.seed) 
        self.maleSigma = args.maleSigma
        self.genome = genome
        self.females = self.generateFemale(args.femaleSize, genome, args.fitbase)
        self.fitness_function = FitnessFunction.get_fitness_function(args.fitnessFunction)
        
    def generateFemale(self, size, genome, fitbase):
        """
        Generate females
        """
        pop = []
        for x in range(size):
            pop.append(Female(genome = deepcopy(genome), fitbase = fitbase))
        return pop
    
    def ranMale(self):
        male = np.random.normal(5, self.maleSigma)
        while(male<0):
            male = np.random.normal(5, self.maleSigma)
        return male
    
    def det_fitness(self):
        for f in self.females:
            while(not f.done):
                f.step(self.ranMale())
            self.fitness_function.cal_fitness(f)