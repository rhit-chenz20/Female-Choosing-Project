from fileinput import filename
import numpy as np
import seaborn as sns
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
        fileNames = [file for file in fileNames if ('.csv' in file) & (self.filename in file)]
        data1 = []

        for file in fileNames:
            df = pd.read_csv(self.inputpath + "/" + file, index_col=False)
            data1.append(df)
            # df.plot(kind='scatter', x='Generation', y='Stddev Fitness')
        # plt.show()

        color = iter(plt.cm.rainbow(np.linspace(0, 1, len(data1))))
        fig, ax = plt.subplots()  # creates one figure with one axes
        for x in range(len(data1)):  # Looping over the GroupBy objects
            c=next(color)
            data1[x].plot(x='Generation', y='Stddev Fitness', ax=ax, kind='scatter', label=x, c=c)
        # plt.show()

        data1_cancat = pd.concat(objs=data1)
        foo = data1_cancat.groupby(level=0).mean()
        # foo.plot(kind='scatter', x='Generation', y='Average Fitness')
        sns.regplot(x=foo['Generation'],y=foo['Stddev Fitness'], lowess=True, scatter=False)
        # plt.savefig(self.outputPath + self.date + self.filename + "_aveFit.png")
        # plt.clf()
        # foo.plot(kind='scatter', x='Generation', y='Average Threshold')
        # sns.regplot(x=foo['Generation'],y=foo['Average Threshold'])
        # plt.savefig(self.outputPath + self.date + self.filename + "_aveThr.png")

        
        # foo.plot(kind='scatter', x='Generation', y='Stddev Fitness')
        # plt.savefig(self.outputPath + self.date + self.filename + "_staFit.png")

        # foo.plot(kind='scatter', x='Generation', y='Stdev Threhold')
        # plt.savefig(self.outputPath + self.date + self.filename + "_staThr.png")
        plt.show()