import mesa
import statistics
import random
import csv
import numpy as np
from queue import PriorityQueue

from .agent import Female

class FemaleMatingModel(mesa.Model):
    """

    """
    def __init__(
        self,
        femaleSize,
        matingLength,
        maleMu,
        maleSigma,
        maleSize,
        mutationMu,
        generations,
        startingRange
    ):
        super().__init__()
        ran = Randomizer(maleMu, maleSigma, startingRange)
        self.females = []
        self.males = []
        self.matingLength = matingLength
        self.generateFemale(femaleSize, ran)
        self.generateMale(maleMu, maleSigma, maleSize)
        self.path = "/Users/andrea/Documents/GitHub/Female-Choosing-Project/db.csv"
        self.writeToFile(["Generation", "Average Fitness", "Stddev Fitness", "Average Threshold", "Stdev Threhold"]) 
        self.generation = 0
        self.maxGen = generations
        self.evolve(ran)
        s = PriorityQueue()

    def evolve(self, ran):
        while(self.generation < self.maxGen):
            for female in self.females:
                for i in range(self.matingLength):
                    male = self.males[ran.ranInt(len(self.males))]
                    female.step(male)
            self.writeToFile([self.generation, self.calMeanFit(), self.calDivFit(), self.calMeanThres(), self.calDivThres()])
            self.generation += 1
            self.reproduce()

    def reproduce(self):
        parent = self.chooseParent()
        p = parent.pop()

    """
    
    """
    def chooseParent(self):
        parent = PriorityQueue(maxsize=(len(self.females) / 2))
        for female in self.females:
            parent.put((-female.getFitness(),female))
        return parent

    """
    Generate females with random threshold within range
    """
    def generateFemale(self, size, ran):
        for x in range(size):
            self.females[x] = Female(ran.threVal())
            # generate bitstring
            # random.randbytes(n)

    """
    Generate certain number of males from a normal distribution
    """
    def generateMale(self, mu, sigma, size):
        self.male = np.random.normal(mu, sigma, size)
    
    """
    Calculate the fitness' mean of current generation
    """
    def calMeanFit(self):
        total = 0
        for x in range(len(self.females)):
            total += self.females[x].getFitness()
        return total / len(self.females)

    """
    Calculate the fitness' standard deviation of current generation
    """
    def calDivFit(self):
        fitnesses = []
        for x in range(len(self.females)):
            fitnesses.append(self.females[x].getFitness())
        return statistics.pstdev(fitnesses)

    """
    Calculate the thresholds' mean of current generation
    """
    def calMeanThres(self):
        total = 0
        for x in range(len(self.females)):
            total += self.females[x].getThreshold()
        return total/ len(self.females)

    """
    Calculate the thresholds' standard deviation of current generation
    """
    def calDivThres(self):
        thresholds = []
        for x in range(len(self.females)):
            thresholds.append(self.females[x].getThreshold())
        return statistics.pstdev(thresholds)

    """
    Write a row into csv file
    """
    def writeToFile(self, row):
        file = open(self.path, "w")
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()

class Randomizer():
    def __init__(
        self,
        maleMu,
        maleSigma,
        startingRange
    ):
        super().__init__()
        self.mu = maleMu
        self.sigma = maleSigma
        self.range = startingRange

    def threVal(self):
        return 20
        # return random.randrange(self.mu - self.range * self.sigma,self.mu + self.range * self.sigma)

    def ranInt(self, size):
        return 2
        # return random.randint(size)
# def main():
#     model = FemaleMatingModel(10)

# if __name__ == "__main__":
#     main()

