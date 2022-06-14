import mesa
import statistics
import random
import csv

from agent import Female


class FemaleMatingModel(mesa.Model):
#class FemaleMatingModel():
    """

    """

    def __init__(
        self,
        size,

    ):
        super().__init__()
        ran = Randomizer()
        self.females = []
        self.generateFemale(size, ran)
        self.path = "/Users/andrea/Documents/GitHub/Female-Choosing-Project/db.csv"
        self.mean = 0
        self.sdv = 0

    def generateFemale(self, size, ran):
        """
        Randomly generate females
        """
        for x in range(size):
            print(x)
            # self.females[x] = Female(ran.val())
            
            # print(self.females[x].threshold)


        


        # mean = sum(test_list) / len(test_list)
        # standard deviation of a list
        # statistics.pstdev(test_list)
       
    def calMeanThres(self):
        total = 0
        for x in range(len(self.females)):
            total += self.females[x].getThreshold()
        self.mean = total/ len(self.females)

    def calDivThres(self):
        thresholds = []
        for x in range(len(self.females)):
            thresholds.append(self.females[x].getThreshold())
        self.sdv = statistics.pstdev(thresholds)

    def writeToFile(self, row):
        file = open(self.path, "w")
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()

class Randomizer():
    def val(self):
        return 20
        # return random.randint(0,100)

def main():
    model = FemaleMatingModel(10)

if __name__ == "__main__":
    main()

