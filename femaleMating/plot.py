import os
import pandas as pd
import matplotlib.pyplot as plt

# get help from https://stackoverflow.com/a/48126960
class Plot():
    def __init__(
        self,
        filename
        ):
        self.date = "June20/"
        self.filename = filename
        self.inputpath = "/Users/andrea/Documents/GitHub/Female-Choosing-Project/CSVResultFiles/" + self.date
        self.outputPath = "/Users/andrea/Documents/GitHub/Female-Choosing-Project/ResultPlot/"
        self.plot()
    
    def plot(self):
        fileNames = os.listdir(self.inputpath)
        fileNames = [file for file in fileNames if '.csv' in file]
        data1 = []

        for file in fileNames:
            df = pd.read_csv(self.inputpath + "/" + file, index_col=False)
            data1.append(df)

        # print(data) concat
        data1_cancat = pd.concat(objs=data1)
        # print(data1_cancat)
        foo = data1_cancat.groupby(level=0).mean()
        foo.plot(kind='scatter', x='Generation', y='Average Threshold')
        plt.savefig(self.outputPath + self.date + self.filename + ".png")
        # plt.show()
        # data2 = pd.DataFrame(data = data1)
        
        # for df in data1:

        #     print(df.get("Average Fitness"))

            # df.plot(kind='scatter', x='Generation', y='Average Fitness')
            # fig.savefig(self.outputPath + self.date + self.filename)