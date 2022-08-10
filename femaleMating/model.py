import statistics
import random
import csv
import numpy as np

from .agent import FemaleGenome, FemaleThreshold
from .selection import Selection
from .fitnessFunction import FitnessFunction

class FemaleMatingModel():
    """

    """
    def __init__(
        self,
        args
    ):
        self.ran = Randomizer()
        self.females = []
        self.males = []
        self.matingLength = args.matingLength
        self.memoryLength = args.memoryLength
        self.maleSigma = args.maleSigma
        self.femaleType = args.femaleType
        self.generateFemale(args.femaleSize, args.fitnessFunction, self.femaleType, self.ran, args.femaleSigma, 
        args.femaleMu, args.flatCost, args.fitbase)
        self.generation = 0
        self.maxGen = args.maxGen
        self.mutationSigma = args.mutationLamda * args.matingLength
        self.selection = args.selection
        self.topPercent = args.topPercent
        self.fitfile = open(args.filename + ".csv", "w+")
        self.fitwriter = csv.writer(self.fitfile)
        self.lastfile = open("last_" + args.filename + ".csv", "w+")
        self.lastwriter = csv.writer(self.lastfile)

        if(self.femaleType == 1):
            last_title = ["Mating_Steps", "Fitness_Mating", "Num_Look_Before_1_Mating"]
        
            title = ["Generation", "Ave_Fitness", "All_Mate","Fit_Mate_First","Fit_Others"]
            genotitle =''
            genotitle+= 'best'
            for x in range(args.matingLength):
                title.append(genotitle + "_mate_"+str(x+1))
            genotitle = 'worst'
            for x in range(args.matingLength):
                title.append(genotitle + "_mate_"+str(x+1))
        elif(self.femaleType == 0):
            last_title=["Num_Mating"]
            title = ["Generation","Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]

        self.writeToFile(self.lastwriter, last_title)
        self.writeToFile(self.fitwriter, title)

    def generateFemale(self, size, fitness, type, ran, femaleSigma, femaleMu, flatcost, fitbase):
        """
        Generate females
        """
        function = FitnessFunction.get_fitness_function(fitness)
        if(type == 1):
            for x in range(size):
                genome = []
                for y in range(self.matingLength):
                    genome.append(ran.ranInt(2))
                female = FemaleGenome(genome, fit = function, memoryLength= self.memoryLength, flatcost= flatcost, fitbase=fitbase, ran=self.ran)
                self.females.append(female)
        elif (type == 0):
            for x in range(size):
                female = FemaleThreshold(self.ran.norran(femaleSigma, femaleMu), fit = function, fitbase = fitbase,flatcost=flatcost)
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
        result = []
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
        if len(mate_first) == 0:
            mate1 = 0
        else: mate1 = sum(mate_first)/len(mate_first)
        result.append(mate1)

        if len(others) == 0:
            mate2 = 0
        else: mate2 = sum(others)/len(others)
        result.append(mate2)
        return result

    def writeLastGen(self):
        if(self.femaleType == 1):
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
        elif(self.femaleType == 0):
            for female in self.females:
                self.writeToFile(self.lastwriter, [len(female.mates)])

        

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
        print("End of simulation")

        print("Outputing last generation.")
        self.writeLastGen()
        self.lastfile.close() 
        self.fitfile.close()

    def evolve(self, ran):
        self.step(ran)
        data = [self.generation]
        if(self.femaleType == 1):
            data += self.calDataNoThre() + self.bestWorstIndi()
        elif(self.femaleType == 0):
            data += self.calDataThre()
        self.writeToFile(self.fitwriter, data)
        if self.generation < self.maxGen:
            self.reproduce()
            self.generation += 1

    def step(self, ran):
        for female in self.females:
            for i in range(self.matingLength):
                # sample a random male from the distribution
                male = ran.ranMale(self.maleSigma)
                female.setCurrentMale(male)
                # for test without mesa
                female.step()
            female.calFitness()
        self.females.sort(reverse=True)

    def reproduce(self):
        """
        Generate the next generation
        """
        parent = self.chooseParent()
        for x in range(len(self.females)):
            index = self.ran.ranInt(len(parent))
            if(isinstance(parent[index], FemaleThreshold)):
                child = FemaleThreshold(parent[index].threshold, parent[index].fit, 
                flatcost=parent[index].flatcost,fitbase=parent[index].fitbase)
                child.mutate(0.1, self.ran)
            elif(isinstance(parent[index], FemaleGenome)):
                child = FemaleGenome(parent[index].genome, parent[index].fit, len(parent[index].memory),
                parent[index].flatcost, parent[index].fitbase, parent[index].ran)
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
