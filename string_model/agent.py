
class Female():
    def __init__(
        self,
        genome,
        fitbase
    ):
        """
        Create a new Female.
        """
        self.fitness = 0
        self.mates = []
        self.mem = []
        self.threshold = 0
        self.genome = genome
        self.mate_i = 0
        self.fitbase = fitbase
        self.done = self.mate_i >= len(self.genome)

    def step(self, male):
        if(self.genome[self.mate_i] == 0):
            self.mate(male)
        self.memorize(male)
        self.mate_i += 1
        self.done = self.mate_i >= len(self.genome)
        

    def calFitness(self, fit_func):
        fit_func.cal_fitness(self)
        #self.adjustCost()
    
    def memorize(self, male_fit):
        self.mem.append(male_fit)
        self.update_threshold()
    
    def update_threshold(self):
        self.threshold = sum(self.mem)/len(self.mem)
    
    def mate(self, male_fit):
        if(male_fit >= self.threshold):
            self.mates.append(male_fit)

    def __lt__(self, otherF):
        return self.fitness < otherF.fitness

    def __str__(self):
        return str(self.genome)