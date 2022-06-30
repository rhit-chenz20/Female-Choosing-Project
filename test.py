import unittest
from femaleMating.agent import FemaleGenome, FemaleThreshold
from femaleMating.model import FemaleMatingModel
import numpy as np

class Randomizer():
    def __init__(
        self,
    ):
        self.mu = 1
        self.thre = 10
        self.male = 1
        self.int = [1]
        self.size = 1

    def threVal(self):
        return self.thre

    def ranInt(self, size):
        result = self.int[0]
        self.int.remove(self.int[0])
        return result

    def valmu(self, sigma):
        return self.mu

    def ranMale(self, mu, sigma):
        return self.male

    def poisson(self, lam):
        return self.size

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.model = FemaleMatingModel(
            femaleSize = 10,
            matingLength = 10,
            maleSigma = 3,
            # mutationSigma = 1,
            generations = 100,
            femaleSigma = 3,
            femaleMu = 1,
            selection = 0,
            fitness= 0,
            filename = 'test',
            femaleType = 0,
            memoryLength = 0,
            flatcost = 0,
            fitbase = 0
        )
        self.femaleThre = FemaleThreshold(
            val = 10, 
            fit = 0,
        )
        self.femaleGeno = FemaleGenome(
            [0,1,0,1,0,1],
            0,3,2,0.5
        )
        self.ran = Randomizer()

    def test_mutate(self):
        self.femaleThre.mutate(1,self.ran)
        self.assertEqual(self.femaleThre.threshold, 11)
        self.ran.mu = -1
        self.femaleThre.mutate(1,self.ran)
        self.assertEqual(self.femaleThre.threshold, 10)
        self.ran.mu = 0
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
        self.femaleThre.fit = 1
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
        self.femaleThre.fit = 0

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

    def test_mutation(self):
        self.ran.size = 2
        self.ran.int = [1,3]
        self.femaleGeno.mutate(1,self.ran)
        self.assertEqual(self.femaleGeno.selected, [1,3])
        self.assertEqual(self.femaleGeno.genome, [0,0,0,0,0,1])
        self.ran.int = [0,1,2,3,4,5,6,7,8]
        self.ran.size = 10
        self.femaleGeno.mutate(1,self.ran)
        self.assertEqual(self.femaleGeno.selected, [0,1,2,3,4,5])
        self.assertEqual(self.femaleGeno.genome, [1,1,1,1,1,0])
        self.ran.int = [0,1,1,1,1,5,4,3,2]
        self.ran.size = 3
        self.femaleGeno.mutate(1,self.ran)
        self.assertEqual(self.femaleGeno.selected, [0,1,5])
        self.assertEqual(self.femaleGeno.genome, [0,0,1,1,1,1])

if __name__ == '__main__':
    unittest.main()