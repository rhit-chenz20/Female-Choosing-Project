import unittest
from femaleMating.agent import FemaleThreshold
from femaleMating.model import FemaleMatingModel

class Randomizer():
    def __init__(
        self,
    ):
        self.mu = 1
        self.thre = 10
        self.male = 1
        self.int = 1

    def threVal(self):
        return self.thre

    def ranInt(self, size):
        return self.int

    def valmu(self, sigma):
        return self.mu

    def ranMale(self, mu, sigma):
        return self.male

    def set_mu(self, newnum):
        self.mu = newnum

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.model = FemaleMatingModel(
            femaleSize = 10,
            matingLength = 10,
            maleSigma = 3,
            mutationSigma = 1,
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
        self.female = FemaleThreshold(
            val = 10, 
            fit = 0,
        )
        self.ran = Randomizer()

    def test_mutate(self):
        self.female.mutate(1,self.ran)
        self.assertEqual(self.female.threshold, 11)
        self.ran.set_mu(-1)
        self.female.mutate(1,self.ran)
        self.assertEqual(self.female.threshold, 10)
        self.ran.set_mu(0)
        self.female.mutate(1,self.ran)
        self.assertEqual(self.female.threshold, 10)

    def test_currentMate(self):
        self.female.setCurrentMale(11)
        self.assertEqual(self.female.mate(), True)
        self.assertEqual(len(self.female.mates), 1)
        self.female.setCurrentMale(10)
        self.assertEqual(self.female.mate(), True)
        self.assertEqual(len(self.female.mates), 2)
        self.female.setCurrentMale(9)
        self.assertEqual(self.female.mate(), False)
        self.assertEqual(len(self.female.mates), 2)
        self.female.mates.clear()

    def test_aveFitness(self):
        sets = [[0,1,5,10,15,20],
            [0, 1, 2, 4, 8],
            [10, 10, 10]]
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.female.setCurrentMale(sets[y][x])
                self.female.step()
            filtered = list(filter(lambda male: male >= self.female.threshold, sets[y]))
            self.assertEqual(len(self.female.mates), len(filtered))
            if(len(filtered) != 0):
                self.assertEqual(self.female.fitness, sum(filtered) / len(filtered))
            else:
                self.assertEqual(self.female.fitness, 0)
            self.female.mates.clear()

    def test_lowFitness(self):
        sets = [[0,1,5,10,15,20],
            [-10, 0, 1, 2, 4, 8],
            [10, 10, 10]]
        self.female.fit = 1
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.female.setCurrentMale(sets[y][x])
                self.female.step()
            filtered = list(filter(lambda male: male >= self.female.threshold, sets[y]))
            self.assertEqual(len(self.female.mates), len(filtered))
            if(len(filtered) != 0):
                self.assertEqual(self.female.fitness, min(filtered))
            else:
                self.assertEqual(self.female.fitness, 0)
            self.female.mates.clear()
        self.female.fit = 0

    def test_flatcost(self):
        sets = [[0,1,5,10,15,20],
            [0, 1, 2, 4, 8],
            [10, 10, 10]]
        cost = 2
        self.female.flatcost = cost
        for y in range(len(sets)):
            for x in range(len(sets[y])):
                self.female.setCurrentMale(sets[y][x])
                self.female.step()
            filtered = list(filter(lambda male: male >= self.female.threshold, sets[y]))
            self.assertEqual(len(self.female.mates), len(filtered))
            if(len(filtered) != 0):
                self.assertEqual(self.female.fitness, (sum(filtered) / len(filtered)) -  cost * len(filtered))
            else:
                self.assertEqual(self.female.fitness, 0)
            self.female.mates.clear()

    

if __name__ == '__main__':
    unittest.main()