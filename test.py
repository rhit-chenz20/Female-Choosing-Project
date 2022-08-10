import unittest
from femaleMating.agent import FemaleGenome, FemaleThreshold
from femaleMating.fitnessFunction import FitnessFunction

class Randomizer():
    def __init__(
        self,
    ):
        self.int = 0
        ints = [0,1,2,3,4]
        self.ite = iter(ints)

    def norran(self, sigma, mu):
        return self.int

    def ranInt(self, size):
        return next(self.ite)

    def valmu(self, sigma):
        return self.int

    def ranMale(self, sigma):
        return self.int

    def poisson(self, lam):
        return self.int

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.ran = Randomizer()
        self.femaleThre = FemaleThreshold(
            val = 10, 
            fit = FitnessFunction.get_fitness_function(0),
            fitbase=0.5,
            flatcost=0
        )
        self.femaleGeno = FemaleGenome(
            genome=[0,1,0,1,0,1],
            fit=FitnessFunction.get_fitness_function(0),
            memoryLength=3,
            flatcost=2,
            fitbase=0.5,
            ran=self.ran
        )

    def test_mutate(self):
        self.ran.int = 1
        self.femaleThre.mutate(1,self.ran)
        self.assertEqual(self.femaleThre.threshold, 11)
        self.ran.int = -1
        self.femaleThre.mutate(1,self.ran)
        self.assertEqual(self.femaleThre.threshold, 10)
        self.ran.int = 0
        self.femaleThre.mutate(1,self.ran)
        self.assertEqual(self.femaleThre.threshold, 10)

    def test_currentMate(self):
        self.femaleThre.setCurrentMale(11)
        self.assertEqual(self.femaleThre.mate(), True)
        self.assertEqual(len(self.femaleThre.mates), 1)
        self.femaleThre.setCurrentMale(10)
        self.assertEqual(self.femaleThre.mate(), True)
        self.assertEqual(len(self.femaleThre.mates), 2)
        self.femaleThre.setCurrentMale(9)
        self.assertEqual(self.femaleThre.mate(), False)
        self.assertEqual(len(self.femaleThre.mates), 2)
        self.femaleThre.mates.clear()

    def test_aveFitness(self):
        sets = [[0,1,5,10,15,20],
            [0, 1, 2, 4, 8],
            [10, 10, 10]]
        self.femaleThre.fit = FitnessFunction.get_fitness_function(0)
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.femaleThre.setCurrentMale(sets[y][x])
                self.femaleThre.step()
            filtered = list(filter(lambda male: male >= self.femaleThre.threshold, sets[y]))
            self.assertEqual(len(self.femaleThre.mates), len(filtered))
            if(len(filtered) != 0):
                self.assertEqual(self.femaleThre.fitness, sum(filtered) / len(filtered))
            else:
                self.assertEqual(self.femaleThre.fitness, 0)
            self.femaleThre.mates.clear()

    def test_lowFitness(self):
        sets = [[0,1,5,10,15,20],
            [-10, 0, 1, 2, 4, 8],
            [10, 10, 10]]
        self.femaleThre.fit = FitnessFunction.get_fitness_function(1)
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.femaleThre.setCurrentMale(sets[y][x])
                self.femaleThre.step()
            filtered = list(filter(lambda male: male >= self.femaleThre.threshold, sets[y]))
            self.assertEqual(len(self.femaleThre.mates), len(filtered))
            if(len(filtered) != 0):
                self.assertEqual(self.femaleThre.fitness, min(filtered))
            else:
                self.assertEqual(self.femaleThre.fitness, 0)
            self.femaleThre.mates.clear()

    def test_flatcost(self):
        sets = [[0,1,5,10,15,20],
            [0, 1, 2, 4, 8],
            [10, 10, 10]]
        cost = 2
        self.femaleThre.flatcost = cost
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.femaleThre.setCurrentMale(sets[y][x])
                self.femaleThre.step()
            filtered = list(filter(lambda male: male >= self.femaleThre.threshold, sets[y]))
            self.assertEqual(len(self.femaleThre.mates), len(filtered))
            if(len(filtered) != 0):
                self.assertEqual(self.femaleThre.fitness, (sum(filtered) / len(filtered)) -  cost * len(filtered))
            else:
                self.assertEqual(self.femaleThre.fitness, 0)
            self.femaleThre.mates.clear()

    def test_memory(self):
        sets = [[0,1,5,10,15,20],
            [0, 1, 2, 4, 8],
            [10, 10, 10]]
        
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.femaleGeno.setCurrentMale(sets[y][x])
                self.femaleGeno.step()
            
            self.assertEqual(len(self.femaleGeno.memory), 3)
            if(x == 0):
                self.assertEqual(self.femaleGeno.memory, [sets[y][0], None, None])
            elif(x==1):
                self.assertEqual(self.femaleGeno.memory, [sets[y][0], sets[y][1], None])
            else:
                self.assertEqual(self.femaleGeno.memory, [sets[y][x-2], sets[y][x-1], sets[y][x]])
            self.femaleGeno.mates.clear()
            self.femaleGeno.geneindex = 0

    def test_mutation(self):
        self.ran.int = 2
        self.femaleGeno.genome = [0,1,0,1,0,1]
        self.ran.ite = iter([0,1,2,3])
        self.femaleGeno.mutate(1,self.ran)
        self.assertEqual(self.femaleGeno.selected, [0,1])
        self.assertEqual(self.femaleGeno.genome, [1,0,0,1,0,1])
        self.ran.int = 10
        self.femaleGeno.genome = [0,1,0,1,0,1]
        self.ran.ite = iter([0,1,2,3,4,5])
        self.femaleGeno.mutate(1,self.ran)
        self.assertEqual(self.femaleGeno.selected, [0,1,2,3,4,5])
        self.assertEqual(self.femaleGeno.genome, [1,0,1,0,1,0])
        self.ran.int = 3
        self.femaleGeno.genome = [0,1,0,1,0,1]
        self.ran.ite = iter([0,0,0,3,4,5])        
        self.femaleGeno.mutate(1,self.ran)
        self.assertEqual(self.femaleGeno.selected, [0,3,4])
        self.assertEqual(self.femaleGeno.genome, [1,1,0,0,1,1])

    def test_weightedFitness(self):
        sets = [[0,1,5,10,15,20],
            [-10, 0, 1, 2, 4, 8],
            [10, 10, 10]]
        answers = [15,0,8.75]
        self.femaleThre.fit = FitnessFunction.get_fitness_function(2)
        self.femaleThre.fitbase = 0.5
        self.femaleThre.fitness = 0
        self.femaleThre.flatcost = 0
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.femaleThre.setCurrentMale(sets[y][x])
                self.femaleThre.step()
            filtered = list(filter(lambda male: male >= self.femaleThre.threshold, sets[y]))
            
            self.assertEqual(len(self.femaleThre.mates), len(filtered))
            self.assertEqual(self.femaleThre.fitness, answers[y])
            self.femaleThre.mates.clear()
            self.femaleThre.fitness = 0

    def test_weightedFitness_negative(self):
        sets = [[-10, -10, -10],
        [-30, -20, -10, -10, -10],
        [-100, -100, -20, -200, -150]]
        self.femaleThre.fit = FitnessFunction.get_fitness_function(2)
        self.femaleThre.fitbase = 0.5
        self.femaleThre.fitness = 0
        self.femaleThre.flatcost = 0
        thresholds = [-10, -20, -30, -150]
        answers=[[-8.75, -8.75, -8.75, -8.75],
        [-8.75, -10, -10.9375, -10.9375],
        [0,-10, -10, -98.75]]
        for y in range(len(sets)):
            for i in range(len(thresholds)):
                self.femaleThre.threshold = thresholds[i]
                for x in range(len(sets[y])):
                    self.femaleThre.setCurrentMale(sets[y][x])
                    self.femaleThre.step()
                filtered = list(filter(lambda male: male >= self.femaleThre.threshold, sets[y]))         
                self.assertEqual(len(self.femaleThre.mates), len(filtered))
                self.assertEqual(self.femaleThre.fitness, answers[y][i])

                self.femaleThre.mates.clear()
                self.femaleThre.fitness = 0


if __name__ == '__main__':
    unittest.main()