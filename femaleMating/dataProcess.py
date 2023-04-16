import statistics
import csv
import random

class DataProcessor():
    def __init__(self, seed, filename, matingLength, femaleType):
        if(seed==-1):
            seed = random.randint(10000000)
        
        self.matingL = matingLength
        self.fitfile = open(filename + "_" + str(seed)+ ".csv", "w+")
        self.fitwriter = csv.writer(self.fitfile)

        lastfile_name=filename.split("/")
        lastfile_name[len(lastfile_name)-1] = "last_" + lastfile_name[len(lastfile_name) - 1]
        name = lastfile_name[0]
        for x in range(1,len(lastfile_name)):
            name += "/"+lastfile_name[x]
        self.lastfile = open(name + ".csv", "w+")
        self.lastwriter = csv.writer(self.lastfile)
        self.femaleType = femaleType
        if(femaleType == 1):
            last_title = ["Mating_Steps", "Fitness_Mating", "Num_Look_Before_1_Mating"]
            title = ["Generation", "Ave_Fitness", "All_Mate","Fit_Mate_First","Fit_Others"]
            genotitle =''
            genotitle+= 'best'
            for x in range(matingLength):
                title.append(genotitle + "_mate_"+str(x+1))
            genotitle = 'worst'
            for x in range(matingLength):
                title.append(genotitle + "_mate_"+str(x+1))
        elif(femaleType == 0):
            last_title=["Num_Mating"]
            title = ["Generation","Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]

        writeToFile(self.lastwriter, last_title)
        writeToFile(self.fitwriter, title)

    def close(self, females):
        self.writeLastGen(females)
        self.lastfile.close() 
        self.fitfile.close()

    def writeDataLearning(self, generation, females):
        data = [generation]
        data += self.calDataNoThre(females) + self.bestWorstIndi(females)
        writeToFile(self.fitwriter, data)

    def writeDataThreshold(self, generation, females):
        data = [generation]
        data += self.calDataThre(females)
        writeToFile(self.fitwriter, data)

    def bestWorstIndi(self, females):
        result = []
        females.sort(reverse=True)
        best = females[0]
        worst = females[len(females) - 1]
        for x in range(len(best.genome)):
            result.append(best.genome[x])
        for y in range(len(worst.genome)):
            result.append(worst.genome[y])
        return result

    def calDataThre(self, females):
        result = []
        fitnesses = []
        thresholds = []
        for x in range(len(females)):
            fitnesses.append(females[x].fitness)
            thresholds.append(females[x].threshold)
        
        # Average fitness
        result.append(sum(fitnesses) / len(self.females))
        # Standard deviation of fitness
        result.append(statistics.pstdev(fitnesses))
        # Average threshold
        result.append(sum(thresholds) / len(self.females)) 
        # Standard deviation of threshold
        result.append(statistics.pstdev(thresholds))
        return result

    def calDataNoThre(self, females):
        result = []
        fitnesses = []
        all1 = 0
        for female in females:
            fitnesses.append(female.fitness)
            all1+=female.mating_steps
        # Average fitness
        result.append(sum(fitnesses) / len(females))
        # Standard deviation of fitness
        # result.append(statistics.pstdev(fitnesses))
        # All mate
        result.append(all1)
        mate_first = self.mateFirstData(females)
        return result + mate_first

    def mateFirstData(self, females):
        result = []
        mate_first = []
        others = []
        for female in females:
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

    def writeLastGen(self, females):
        if(self.femaleType == 1):
            for female in females:
                result = []
                result.append(female.mating_steps)
                result.append(female.fitness)

                for x in range(len(female.genome)):
                    if female.genome[x] == 1:
                        result.append(x)
                        break

                    if x == len(female.genome)-1:
                        result.append(len(female.genome))

                writeToFile(self.lastwriter, result)
        elif(self.femaleType == 0):
            for female in females:
                writeToFile(self.lastwriter, [len(female.mates)])


def writeToFile(writer, row):
    """
    Write a row into csv file
    """
    writer.writerow(row)