import mesa
import statistics
import random
import csv
import os
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
        date = "July6/"
        if not os.path.exists("CSVResultFiles/" + date):
            os.makedirs("CSVResultFiles/" + date)
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
        self.mutationSigma = mutationSigma * matingLength
        self.selection = selection
        self.fitfile = open("CSVResultFiles/" + date + filename + ".csv", "w+")
        self.fitwriter = csv.writer(self.fitfile)
        self.genefile = open("CSVResultFiles/" + date + 'geno_' +filename + ".csv", "w+")
        self.genowriter = csv.writer(self.genefile)
        # self.writeToFile(self.fitwriter,["Generation", "Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"])
        self.writeToFile(self.fitwriter,["Generation", "Ave_Fitness", "All_Mate"])
        title = ['Generation']
        genotitle =''
        genotitle+= 'best'
        for x in range(matingLength):
            title.append(genotitle + "_mate_"+str(x+1))
        genotitle = 'worst'
        for x in range(matingLength):
            title.append(genotitle + "_mate_"+str(x+1))
        self.writeToFile(self.genowriter, title)

    def step(self):
        if(self.generation <= self.maxGen):
            self.evolve(self.ran)
            self.generation += 1
            # self.schedule.step()
        else:
            print("End of simulation")
            self.fitfile.close()
            self.genefile.close()

    def evolve(self, ran):
        for female in self.females:
            for i in range(self.matingLength):
                # sample a random male from the distribution
                male = ran.ranMale(self.maleDiv)
                female.setCurrentMale(male)
                # for test without mesa
                female.step()
        # self.writeToFile(self.fitwriter, self.calDataThre())
        self.writeToFile(self.fitwriter, self.calDataNoThre())
        # self.writeToFile(self.genowriter, self.colData())
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
        # print(self.females[0].genome)
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
        self.writeToFile(self.genowriter, self.bestWorstIndi())

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

    def colData(self):
        result = [self.generation]
        for x in range(self.matingLength):
            all1 = 0
            # all0 = 0
            for female in self.females:
                if(female.genome[x] == 1):
                    all1+=1
            result.append(all1/len(self.females))
        return result

    def bestWorstIndi(self):
        result = [self.generation]
        best = self.females[0]
        worst = self.females[len(self.females) - 1]
        for x in range(len(best.genome)):
            result.append(best.genome[x])
        for y in range(len(worst.genome)):
            result.append(worst.genome[y])
        return result

    def calDataThre(self):
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

    def calDataNoThre(self):
        result = [self.generation]
        fitnesses = []
        all1 = 0
        for female in self.females:
            fitnesses.append(female.fitness)
            for x in range(self.matingLength):
                if female.genome[x] == 1:
                    all1+=1
        # Average fitness
        result.append(sum(fitnesses) / len(self.females))
        # Standard deviation of fitness
        # result.append(statistics.pstdev(fitnesses))
        # All mate
        result.append(all1)
        return result

    """
    Write a row into csv file
    """
    def writeToFile(self,writer, row):
        writer.writerow(row)

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
