import numpy as np
import random

class Randomizer():
    def __init__(self,seed):
        if(seed==-1):
            self.seed = random.randint(1,10000000)
        else:
            self.seed = seed
        random.seed(self.seed)
        np.random.seed(self.seed)
        print(self.seed)

    def get_seed (self):
        return self.seed

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
