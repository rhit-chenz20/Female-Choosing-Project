from abc import abstractmethod
import math

class FitnessFunction():
    def get_fitness_function(num):
        if(num == 0):
            return AverageFitness()
        elif (num == 1):
            return LowestFitness()
        elif (num == 2):
            return LastMalePrecedentFitness()

    @abstractmethod
    def cal_fitness(self, female):
        pass

class AverageFitness(FitnessFunction):
    def cal_fitness(self, female):
        if(len(female.mates) != 0):
            female.fitness = sum(female.mates) / len(female.mates)
        else:
            female.fitness = 0

class LowestFitness(FitnessFunction):
    def cal_fitness(self, female):
        if(len(female.mates) == 0):
            female.fitness = 0
        else: 
            female.fitness = min(female.mates)

class LastMalePrecedentFitness(FitnessFunction):
    def cal_fitness(self, female):
        female.fitness = 0
        if(len(female.mates) != 0):
            for x in range(len(female.mates)):
                female.fitness += math.pow(female.fitbase, len(female.mates) - x) * female.mates[x]