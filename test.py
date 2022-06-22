import unittest
from femaleMating.agent import Female
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
            maleMu = 5,
            maleSigma = 3,
            mutationSigma = 1,
            generations = 100,
            startingRange = 3,
            selection = 0,
            fitness= 0,
            filename = 'test'
        )
        self.female = Female(
            val = 10, 
            unique_id = 0, 
            model = self.model, 
            fit = 0
        )
        self.ran = Randomizer()

    def test_mutate(self):
        self.female.mutate(1,self.ran)
        self.assertEqual(self.female.getThreshold(), 11)
        self.ran.set_mu(-1)
        self.female.mutate(1,self.ran)
        self.assertEqual(self.female.getThreshold(), 10)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()