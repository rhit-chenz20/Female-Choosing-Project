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
        self.ran = Randomizer(maleMu, maleSigma, startingRange)
        self.schedule = mesa.time.RandomActivation(self)
        self.females = []
        self.males = []
        self.matingLength = matingLength
        self.generateFemale(femaleSize)
        # self.generateMale(maleMu, maleSigma, maleSize)
        self.maleMu = maleMu
        self.maleDiv = maleSigma
        self.generation = 0
        self.maxGen = generations
        file = open("/Users/andrea/Documents/GitHub/Female-Choosing-Project/db.csv", "w")
        self.writer = csv.writer(file)
        self.writeToFile(["Generation", "Average Fitness", "Stddev Fitness", "Average Threshold", "Stdev Threhold"])
        

    def step(self):
        if(self.generation < self.maxGen):
            self.evolve()
            self.generation += 1
            print(self.generation)
            print(self.calMeanThres())
            self.schedule.step()
        else:
            print("End of simulation")
            self.file.close()

    def evolve(self):

        for female in self.females:
            for i in range(self.matingLength):
                # choose a male from a predetermined male group
                # male = self.males[self.ran.ranInt(len(self.males))]
                # sample a random male from the distribution
                male = np.random.normal(self.maleMu, self.maleDiv)
                female.setCurrentMale(male)
        self.writeToFile([self.generation, self.calMeanFit(), self.calDivFit(), self.calMeanThres(), self.calDivThres()])         
        # self.reproduce()

    """
    
    """
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
    def generateFemale(self, size):
        for x in range(size):
            female = Female(self.ran.threVal(), x, self)
            self.females.append(female)
            self.schedule.add(female)
            # generate bitstring
            # random.randbytes(n)

    """
    Generate certain number of males from a normal distribution
    """
    def generateMale(self, mu, sigma, size):
        self.males = np.random.normal(mu, sigma, size)
    
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
        self.writer.writerow(row)
        # print(self.generation)

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
        # return 10
        return random.randrange(self.mu - self.range * self.sigma,self.mu + self.range * self.sigma)

    def ranInt(self, size):
        return 2
        # return random.randint(size)
# def main():
#     model = FemaleMatingModel(10)

# if __name__ == "__main__":
#     main()

