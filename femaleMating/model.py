import mesa
import statistics
import random
import csv
import numpy as np

from .agent import FemaleGenome, FemaleThreshold

class FemaleMatingModel():
    """

    """
    def __init__(
        self,
        femaleSize,
        matingLength,
        maleSigma,
        mutationSigma,
        generations,
        femaleSigma,
        femaleMu,
        selection,
        fitness,
        filename,
        femaleType,
        memoryLength,
        flatcost,
        fitbase
    ):
        super().__init__()
        date = "June28/"
        self.ran = Randomizer()
        # self.schedule = mesa.time.RandomActivation(self)
        self.females = []
        self.males = []
        self.matingLength = matingLength
        self.flatcost = flatcost
        self.fitbase = fitbase 
        self.memoryLength = memoryLength
        self.generateFemale(femaleSize, fitness, femaleType, self.ran, femaleSigma, femaleMu)
        self.maleDiv = maleSigma
        self.generation = 0
        self.maxGen = generations
        self.mutationSigma = mutationSigma
        self.selection = selection
        self.file = open("CSVResultFiles/" + date + filename + ".csv", "w+")
        self.writer = csv.writer(self.file)
        self.writeToFile(["Generation", "Average Fitness", "Stddev Fitness", "Average Threshold", "Stdev Threhold"])

    def step(self):
        if(self.generation <= self.maxGen):
            self.evolve(self.ran)
            self.generation += 1
            # self.schedule.step()
        else:
            print("End of simulation")
            self.file.close()

    def evolve(self, ran):
        for female in self.females:
            for i in range(self.matingLength):
                # sample a random male from the distribution
                male = ran.ranMale(self.maleDiv)
                female.setCurrentMale(male)
                # for test without mesa
                female.step()
        self.writeToFile(self.calData())
        self.reproduce()

    """
    
    """
    def reproduce(self):
        parent = self.chooseParent()
        for x in range(len(self.females)):
            index = self.ran.ranInt(len(parent))
            if(isinstance(parent[index], FemaleThreshold)):
                child = FemaleThreshold(parent[index].threshold, parent[index].fit)
                child.mutate(0.1, self.ran)
            elif(isinstance(parent[index], FemaleGenome)):
                child = FemaleGenome(parent[index].genome, parent[index].fit, len(parent[index].memory),
                parent[index].flatcost, parent[index].fitbase)
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
        for x in range(int(len(self.females)/2)):
            index1 = self.ran.ranInt(len(self.females))
            index2 = self.ran.ranInt(len(self.females))
            if(index1 == index2):
                index2 = self.ran.ranInt(len(self.females))
            if(self.females[index1].fitness >= self.females[index2].fitness):
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
    def generateFemale(self, size, fitness, type, ran, femaleSigma, femaleMu):
        if(type == 1):
            for x in range(size):
                genome = []
                for y in range(self.matingLength):
                    genome.append(ran.ranInt(2))
                female = FemaleGenome(genome, fit = fitness, memoryLength= self.memoryLength, flatcost= self.flatcost, fitbase=self.fitbase)
                self.females.append(female)
        elif (type == 0):
            for x in range(size):
                female = FemaleThreshold(self.ran.threVal(femaleSigma, femaleMu), fit = fitness, fitbase = self.fitbase)
                self.females.append(female)
            # self.schedule.add(female)

    def calData(self):
        result = [self.generation]
        fitnesses = []
        thresholds = []
        for x in range(len(self.females)):
            fitnesses.append(self.females[x].fitness)
            thresholds.append(self.females[x].threshold)
        
        # Average fitness
        result.append(sum(fitnesses) / len(self.females))
        # Standard deviation of fitness
        result.append(statistics.pstdev(fitnesses))
        # Average threshold
        result.append(sum(thresholds) / len(self.females))
        # Standard deviation of threshold
        result.append(statistics.pstdev(thresholds))
        return result

    """
    Write a row into csv file
    """
    def writeToFile(self, row):
        self.writer.writerow(row)

class Randomizer():

    def threVal(self, sigma, mu):
        return np.random.normal(mu, sigma)

    def ranInt(self, size):
        return random.randint(0, size - 1)

    def valmu(self, sigma):
        return np.random.normal(0,sigma)

    def ranMale(self, sigma):
        return np.random.normal(5, sigma)

    def poisson(self, lam):
        return np.random.poisson(lam)
