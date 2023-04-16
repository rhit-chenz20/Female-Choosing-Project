from .agent import FemaleGenome, FemaleThreshold
from .selection import Selection
from .fitnessFunction import FitnessFunction
from .dataProcess import DataProcessor
from .randomizer import Randomizer

class FemaleMatingModel():
    """
    args: femaleSize, matingLength, maleSigma, mutationLamda, maxGen, femaleSigma, femaleMu, selection,
    fitnessFunction, filename, femaleType, memoryLength, flatCost, fitbase, topPercent, seed, debug
    """
    def __init__(
        self,
        args
    ):
        self.ran = Randomizer(args.seed)
        seed = self.ran.get_seed()
        self.dataPro = DataProcessor(seed, args.filename, args.matingLength, args.femaleType)
        self.males = []
        self.matingLength = args.matingLength
        self.maleSigma = args.maleSigma
        self.femaleType = args.femaleType
        self.females = self.generateFemale(args.femaleSize, args.fitnessFunction,self.ran, args.femaleSigma, 
        args.femaleMu, args.flatCost, args.fitbase, args.memoryLength, args.mutationLamda * args.matingLength)
        self.generation = 0
        self.maxGen = args.maxGen
        self.sel = Selection.get_sel(args.selection, args.topPercent, self.ran)
        self.topPercent = args.topPercent

    def generateFemale(self, size, fitness, ran, femaleSigma, femaleMu, flatcost, fitbase, memoryLength, mutationLambda):
        """
        Generate females
        """
        ffunction = FitnessFunction.get_fitness_function(fitness)
        pop = []
        if(self.femaleType == 1):
            for x in range(size):
                genome = []
                for y in range(self.matingLength):
                    genome.append(ran.ranInt(2))
                female = FemaleGenome(genome = genome,mlambda = mutationLambda, fitness_function = ffunction, memoryLength= memoryLength, flatcost= flatcost, fitbase=fitbase, ran=self.ran)
                pop.append(female)
        elif (self.femaleType == 0):
            for x in range(size):
                female = FemaleThreshold(self.ran.norran(femaleSigma, femaleMu), mutationLambda,fit = ffunction, fitbase = fitbase,flatcost=flatcost)
                pop.append(female)
        return pop

    def start(self):
        """
        Start the evolution
        """
        for x in range(self.maxGen):
            self.evolve()
        self.end()

    def end(self):
        """
        End the evolution
        """
        print("End of simulation")
        print("Outputing last generation.")
        self.dataPro.close(self.females)

    def evolve(self):
        self.step()
        if(self.femaleType == 1):
            self.dataPro.writeDataLearning(self.generation,self.females)
        elif(self.femaleType == 0):
            self.dataPro.writeDataThreshold(self.generation,self.females)
        
        if self.generation < self.maxGen-1:
            self.reproduce()
            self.generation += 1

    def step(self):
        for female in self.females:
            for i in range(self.matingLength):
                male = self.ran.ranMale(self.maleSigma)
                female.setCurrentMale(male)
                female.step()
            female.calFitness()

    def reproduce(self):
        """
        Generate the next generation
        """
        parent = self.sel.choose_parent(self.females)
        for x in range(len(self.females)):
            index = self.ran.ranInt(len(parent))
            if(isinstance(parent[index], FemaleThreshold)):
                child = FemaleThreshold(
                    threshold = parent[index].threshold, 
                    fitness_function = parent[index].fit, 
                    mlambda=parent[index].mlambda,
                    flatcost=parent[index].flatcost,
                    fitbase=parent[index].fitbase)
                child.mutate(0.1, self.ran)
            elif(isinstance(parent[index], FemaleGenome)):
                child = FemaleGenome(
                    genome = parent[index].genome, 
                    mlambda = parent[index].mlambda,
                    fitness_function = parent[index].fit, 
                    memoryLength = len(parent[index].memory),
                    flatcost = parent[index].flatcost, 
                    fitbase = parent[index].fitbase, 
                    ran = parent[index].ran)
                child.mutate(self.ran)
            self.females[x] = child