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
        filenames,
        output
        ):
        date = "June28/"
        self.names = ['Average Fitness', "Stddev Fitness", "Average Threshold", "Stdev Threhold"]
        self.labels = ['Average Fitness', 'Standard Deviation Fitness', 'Average Threshold', 'Standard Deviation Threshold']
        self.fignames = ['ave_fit', 'sta_fit', 'ave_the', 'sta_the']
        self.filenames = filenames
        self.output = 'ResultPlot/' + date + output
        
        self.plot()
    
    def plot(self):
        data1 = []

        for file in self.filenames:
            df = pd.read_csv(file, index_col=False)
            data1.append(df)

        data1_cancat = pd.concat(objs=data1)
        foo = data1_cancat.groupby(level=0).mean()

        self.plotFig(data1, foo)

    def plotFig(self, data1, foo):
        for y in range(len(self.names)):
            color = iter(plt.cm.rainbow(np.linspace(0, 1, len(data1))))
            fig, ax = plt.subplots()
            
            for x in range(len(data1)):
                c=next(color)
                data1[x].plot(x='Generation', y=self.names[y], ax=ax, kind='scatter', label=x, c=c)
        
            sns.regplot(x=foo['Generation'],y=foo[self.names[y]], lowess=True, scatter=False)
            ax.set(xlabel='Generation', ylabel=self.labels[y])
            plt.savefig(self.output + "_" + self.fignames[y] + ".png")
            plt.clf()
