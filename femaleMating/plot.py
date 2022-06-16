from fileinput import filename
import os
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as ln

# get help from https://stackoverflow.com/a/48126960
class Plot():
    def __init__(
        self,
        plot50,
        plotTour
        ):
        path = "/Users/andrea/Documents/GitHub/Female-Choosing-Project/CSV result files"
        paths = [path + "/top50", path + "/tournament"]
        if(plot50):
            self.plot(paths[0])
        if(plotTour):
            self.plot(paths[1])
    
    def plot(self, path):
        fileNames = os.listdir(path)
        fileNames = [file for file in fileNames if '.csv' in file]
        for file in fileNames:
            gen = pd.read_csv(path + "/" + file, index_col=0)
            af = pd.read_csv(path + "/" + file, index_col=1)
            at = pd.read_csv(path + "/" + file, index_col=3)
            plt.plot(af, 'b.')
            # plt.plot(at, 'r.')
        plt.title("Female's Fitness Eveolved over Generations")
        plt.xlabel("Female's Fitness")
        plt.ylabel("Generation")
        plt.show()