import mesa
import statistics
import random
import csv
import os
import numpy as np

from .agent import FemaleGenome, FemaleThreshold
from .selection import Selection
from .fitnessFunction import FitnessFunction

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
        fitbase,
        topPercent,
        date
    ):
        super().__init__()
        out = "CSVResultFiles/" + date
        if not os.path.exists(out):
            os.makedirs(out)
        self.ran = Randomizer()
        self.females = []
        self.males = []
        self.matingLength = matingLength
        self.flatcost = flatcost
        self.fitbase = fitbase 
        self.memoryLength = memoryLength
        self.maleSigma = maleSigma
        self.generateFemale(femaleSize, fitness, femaleType, self.ran, femaleSigma, femaleMu)
        self.generation = 0
        self.maxGen = generations
        self.mutationSigma = mutationSigma * matingLength
        self.selection = selection
        self.topPercent = topPercent
        self.fitfile = open(out+'/' + filename + ".csv", "w+")
        self.fitwriter = csv.writer(self.fitfile)
        self.lastfile = open(out+'/' + 'last_' +filename + ".csv", "w+")
        self.lastwriter = csv.writer(self.lastfile)
        self.writeToFile(self.lastwriter, ["Mating_Steps", "Fitness_Mating", "Num_Look_Before_1_Mating"])
        # self.genefile = open(out+'/' + 'geno_' +filename + ".csv", "w+")
        # self.genowriter = csv.writer(self.genefile)
        # self.writeToFile(self.fitwriter,["Generation", "Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"])
        # self.writeToFile(self.fitwriter,["Generation", "Ave_Fitness", "All_Mate"])
        title = ["Generation", "Ave_Fitness", "All_Mate","Fit_Mate_First","Fit_Others"]
        genotitle =''
        genotitle+= 'best'
        for x in range(matingLength):
            title.append(genotitle + "_mate_"+str(x+1))
        genotitle = 'worst'
        for x in range(matingLength):
            title.append(genotitle + "_mate_"+str(x+1))
        # title += ["Fit_Mate_First","Fit_Others"]
        self.writeToFile(self.fitwriter, title)
        self.start()

    def generateFemale(self, size, fitness, type, ran, femaleSigma, femaleMu):
        """
        Generate females
        """
        function = FitnessFunction.get_fitness_function(fitness)
        if(type == 1):
            for x in range(size):
                genome = []
                for y in range(self.matingLength):
                    genome.append(ran.ranInt(2))
                female = FemaleGenome(genome, fit = function, memoryLength= self.memoryLength, flatcost= self.flatcost, fitbase=self.fitbase, ran=self.ran, malesigma=self.maleSigma)
                self.females.append(female)
        elif (type == 0):
            for x in range(size):
                female = FemaleThreshold(self.ran.norran(femaleSigma, femaleMu), fit = function, fitbase = self.fitbase)
                self.females.append(female)

    def colData(self):
        result = [self.generation]
        for x in range(self.matingLength):
            all1 = 0
            for female in self.females:
                if(female.genome[x] == 1):
                    all1+=1
            result.append(all1/len(self.females))
        return result

    def bestWorstIndi(self):
        result = []
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
        result = []
        fitnesses = []
        all1 = 0
        for female in self.females:
            fitnesses.append(female.fitness)
            all1+=female.mating_steps
        # Average fitness
        result.append(sum(fitnesses) / len(self.females))
        # Standard deviation of fitness
        # result.append(statistics.pstdev(fitnesses))
        # All mate
        result.append(all1)
        mate_first = self.mateFirstData()
        # print(mate_first)
        return result + mate_first

    def mateFirstData(self):
        result = []
        mate_first = []
        others = []
        for female in self.females:
            if female.genome[0] == 1:
                mate_first.append(female.fitness)
            else:
                others.append(female.fitness)
        # print("gen "+str(self.generation)+" ")
        # print(len(mate_first))
        # print("gen "+str(self.generation)+" ")
        # print(len(others))
        if len(mate_first) == 0:
            mate1 = 0
        else: mate1 = sum(mate_first)/len(mate_first)
        result.append(mate1)

        if len(others) == 0:
            mate2 = 0
        else: mate2 = sum(others)/len(others)
        result.append(mate2)
        # print(mate2)
        return result

    def writeLastGen(self):
        for female in self.females:
            result = []
            result.append(female.mating_steps)
            result.append(female.fitness)

            for x in range(len(female.genome)):
                if female.genome[x] == 1:
                    result.append(x)
                    break

                if x == len(female.genome)-1:
                    result.append(len(female.genome))

            self.writeToFile(self.lastwriter, result)

    def writeToFile(self,writer, row):
        """
        Write a row into csv file
        """
        writer.writerow(row)

    def start(self):
        """
        Start the evolution
        """
        for x in range(self.maxGen+1):
            self.evolve(self.ran)

        self.end()

    def end(self):
        """
        End the evolution
        """
        print("End of simulation. Outputing last generation.")
        self.writeLastGen()
        self.fitfile.close()
        self.lastfile.close() 

    def evolve(self, ran):
        for female in self.females:
            for i in range(self.matingLength):
                # sample a random male from the distribution
                male = ran.ranMale(self.maleSigma)
                female.setCurrentMale(male)
                # for test without mesa
                female.step()
        self.females.sort(reverse=True)
        data = [self.generation]
        data += self.calDataNoThre() + self.bestWorstIndi()

        self.writeToFile(self.fitwriter, data)
        if self.generation < self.maxGen:
            self.reproduce()
            self.generation += 1

    def reproduce(self):
        """
        Generate the next generation
        """
        parent = self.chooseParent()
        for x in range(len(self.females)):
            index = self.ran.ranInt(len(parent))
            if(isinstance(parent[index], FemaleThreshold)):
                child = FemaleThreshold(parent[index].threshold, parent[index].fit)
                child.mutate(0.1, self.ran)
            elif(isinstance(parent[index], FemaleGenome)):
                child = FemaleGenome(parent[index].genome, parent[index].fit, len(parent[index].memory),
                parent[index].flatcost, parent[index].fitbase, parent[index].ran, parent[index].malesigma)
                child.mutate(self.mutationSigma, self.ran)
            self.females[x] = child

    def chooseParent(self):
        """
        Choose females to be the parent
        """
        self.sortFemale()
        sel = Selection.get_sel(self.selection, self.topPercent, self.ran)
        return sel.choose_parent(self.females)
        # if self.selection == 0 :
        #     return self.top50(self.topPercent)
        # elif self.selection == 1:
        #     return self.tournament()

    def sortFemale(self):
        """
        Sort the females using fitness
        """
        self.females.sort(reverse=True)
        # self.writeToFile(self.genowriter, self.bestWorstIndi())

    



















class Randomizer():
    def norran(self, sigma, mu):
        return np.random.normal(mu, sigma)

    def ranInt(self, size):
        return random.randint(0, size - 1)

    def valmu(self, sigma):
        return np.random.normal(0,sigma)

    def ranMale(self, sigma):
        return np.random.normal(5, sigma)

    def poisson(self, lam):
        return np.random.poisson(lam)
