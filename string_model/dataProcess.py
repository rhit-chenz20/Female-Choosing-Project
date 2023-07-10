import statistics
import csv
from copy import deepcopy
from agent import Female

def calDataThre(females):
    result = []
    fitnesses = []
    thresholds = []
    for x in range(len(females)):
        fitnesses.append(females[x].fitness)
        thresholds.append(females[x].threshold)
    
    # Average fitness
    ave = sum(fitnesses) / len(females)
    # Standard deviation of fitness
    std = statistics.pstdev(fitnesses)

    result.extend([ave, std, ave-std])
    # Average threshold
    result.append(sum(thresholds) / len(females)) 
    # Standard deviation of threshold
    result.append(statistics.pstdev(thresholds))
    return result
    
def writeToFile(writer, row):
    """
    Write a row into csv file
    """
    writer.writerow(row)
    
def close(file):
    file.close()
    
def cal_data(models: list, filename):
    file = open(filename + "_models.csv", "w+")
    writer = csv.writer(file)
    title = ["Genome", "Ave_fit", "Std_fit", "Sum_fit", "Ave_thr", "Std_thr", "Seed", "Num_Learning", "Num_Mating"]
    writeToFile(writer, title)
    
    for m in models:
        genome = m.genome
        num_mating = 0
        for l in genome:
            if(l==0): num_mating+=1
        data = [str(genome)]
        data.extend(calDataThre(m.females))
        data.extend([m.seed, len(genome) - num_mating, num_mating])
        writeToFile(writer, data)
        
        