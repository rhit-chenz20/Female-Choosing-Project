import mesa
import statistics
import random
import csv
import numpy as np

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
        mutationSigma,
        generations,
        startingRange,
        selection,
        fitness,
        filename
    ):
        super().__init__()
        date = "June22"
        self.ran = Randomizer(maleMu, maleSigma, startingRange)
        self.schedule = mesa.time.RandomActivation(self)
        self.females = []
        self.males = []
        self.matingLength = matingLength
        self.generateFemale(femaleSize, fitness)
        # self.generateMale(maleMu, maleSigma, maleSize)
        self.maleMu = maleMu
        self.maleDiv = maleSigma
        self.generation = 0
        self.maxGen = generations
        self.mutationSigma = mutationSigma
        self.selection = selection
        self.file = open("/Users/andrea/Documents/GitHub/Female-Choosing-Project/CSVResultFiles/" + date + "/" + filename + ".csv", "w+")
        self.writer = csv.writer(self.file)
        self.writeToFile(["Generation", "Average Fitness", "Stddev Fitness", "Average Threshold", "Stdev Threhold"])

    def step(self):
        if(self.generation <= self.maxGen):
            self.evolve(self.ran)
            self.generation += 1
            self.schedule.step()
        else:
            print("End of simulation")
            self.file.close()

    def evolve(self, ran):
        for female in self.females:
            for i in range(self.matingLength):
                # sample a random male from the distribution
                male = ran.ranMale(self.maleMu, self.maleDiv)
                female.setCurrentMale(male)
                # for test without mesa
                female.step()
        self.writeToFile([self.generation, self.calMeanFit(), self.calDivFit(), self.calMeanThres(), self.calDivThres()])         
        self.reproduce()

    """
    
    """
    def reproduce(self):
        parent = self.chooseParent()
        for x in range(len(self.females)):
            index = self.ran.ranInt(len(parent))
            child = Female(parent[index].getThreshold(), x, self, parent[index].getFit())
            child.mutate(self.mutationSigma, self.ran)
            self.females[x] = child

    """
    Choose females to be the parent
    """
    def chooseParent(self):
        self.sortFemale()
        if self.selection == 0 :
            return self.top50()
        elif self.selection == 1:
            return self.tournament()

    """
    Choose the top 50% of females as the parent
    """
    def top50(self):
        parent = []
        for x in range(int(len(self.females)/2)):
            parent.append(self.females[x])
        return parent
    
    """
    Use the tournament selection to choose parent
    """
    def tournament(self):
        parent = []
        # Select two random females from the population
        # Choose the one with higher fitness
        for x in range(int(len(self.females)/2)):
            index1 = self.ran.ranInt(len(self.females))
            index2 = self.ran.ranInt(len(self.females))
            if(index1 == index2):
                index2 = self.ran.ranInt(len(self.females))
            if(self.females[index1].getFitness() >= self.females[index2].getFitness()):
                parent.append(self.females[index1])
            else:
                parent.append(self.females[index2])
        return parent

    """
    Sort the females using fitness
    """
    def sortFemale(self):
        self.females.sort(reverse=True)

    """
    Generate females with random threshold within range
    """
    def generateFemale(self, size, fitness):
        for x in range(size):
            female = Female(self.ran.threVal(), x, self, fit = fitness)
            self.females.append(female)
            self.schedule.add(female)
            # generate bitstring
            # random.randbytes(n)

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
        return total / len(self.females)

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
        return random.uniform(self.mu - self.range * self.sigma,self.mu + self.range * self.sigma)

    def ranInt(self, size):
        return random.randint(0, size - 1)

    def valmu(self, sigma):
        return np.random.normal(0,sigma)

    def ranMale(self, mu, sigma):
        return np.random.normal(mu, sigma)