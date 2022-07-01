# from fileinput import filename
from turtle import title
import numpy as np
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt

# get help from https://stackoverflow.com/a/48126960
class Plot():
    def __init__(
        self,
        fitfilenames,
        genofilenames,
        output
        ):
        date = "June29/"
        self.names = ["Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        self.labels = ['Average Fitness', 'Sta Dev Fitness', 'Average Threshold', 'Sta Dev Threshold']
        self.fignames = ['ave_fit', 'sta_fit', 'ave_the', 'sta_the']
        self.fitfilenames = fitfilenames
        self.genofilename = genofilenames
        self.output = 'ResultPlot/' + date
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        self.output += output
        self.plot()
    
    def plot(self):
        data1 = []
        data2 = []

        for file1 in self.fitfilenames:
            df1 = pd.read_csv(file1, index_col=False)
            # print(df1.columns.tolist())
            data1.append(df1)

        for file2 in self.genofilename:
            df2 = pd.read_csv(file2, index_col=False)
            data2.append(df2.loc[:, df2.columns!='Generation'])

        data1_cancat = pd.concat(objs=data1)
        data2_cancat = pd.concat(objs=data2)
        foo = data1_cancat.groupby(level=0).mean()
        foo2 = data2_cancat.groupby(level=0).mean()
        
        self.plotFig(data1, foo, foo2.to_numpy().T)


    def plotFig(self, data1, foo, geno):
        axd = plt.figure(figsize=(14,10)).subplot_mosaic(
        """
        AB
        CD
        EE
        """,
        )
        for y in range(len(self.names)):
            
            color = iter(plt.cm.rainbow(np.linspace(0, 1, len(data1))))
            
            for x in range(len(data1)):
                c=next(color)
                data1[x].plot(x='Generation', y=self.names[y], ax=list(axd.values())[y], kind='scatter', label=x, c=c,)
        
            sns.regplot(x=foo['Generation'],y=foo[self.names[y]], lowess=True, scatter=False, ax = list(axd.values())[y])
            list(axd.values())[y].set(xlabel='Generation', ylabel=self.labels[y], title=self.labels[y])

        axd['E'] = sns.heatmap(geno)
        axd['E'].invert_yaxis()
        axd['E'].set(xlabel='Generation', ylabel='Steps', title='Look Percentage for each step')
        
        identify_axes(axd)
        # plt.show()
        plt.savefig(self.output + ".png")

# https://matplotlib.org/stable/tutorials/provisional/mosaic.html
# Helper function used for visualization in the following examples
def identify_axes(ax_dict, fontsize=48):
    """
    Helper to identify the Axes in the examples below.

    Draws the label in a large font in the center of the Axes.

    Parameters
    ----------
    ax_dict : dict[str, Axes]
        Mapping between the title / label and the Axes.
    fontsize : int, optional
        How big the label should be.
    """
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")