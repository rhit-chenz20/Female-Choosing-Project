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
        date = "July6/"
        # self.names = ["Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        self.names = ["Ave_Fitness", "All_Mate",]
        self.genonames = ['best_mate_', 'worst_mate_']
        self.labels = ['Average Fitness', 'Sta Dev Fitness', 'Average Threshold', 'Sta Dev Threshold']
        self.fignames = ['ave_fit', 'sta_fit', 'ave_the', 'sta_the']
        self.output = 'ResultPlot/' + date
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        self.output += output

        self.fitfilenames = []
        self.genofilenames = []
        dictionary = {}  
        for x in fitfilenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = dictionary.get(key,[])
            group.append(x)  
            dictionary[key] = group
        self.fitfilenames = dictionary.values()

        gdictionary = {}  
        for x in genofilenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = gdictionary.get(key,[])
            group.append(x)  
            gdictionary[key] = group
        self.genofilenames = gdictionary.values()

        sample1 = list(gdictionary.keys())[0].split('_')
        sample2 = list(gdictionary.keys())[1].split('_')
        diIndex = 0
        for x in range(len(sample1)):
            if(sample1[x] != sample2[x]):
                diIndex = x-1
                break

        self.legends = []
        for key in gdictionary.keys():
            li = key.split('_')
            self.legends.append(self.processwords(li[diIndex]) + ' ' + li[diIndex+1])
            self.legends.append(self.processwords(li[diIndex]) + ' ' + li[diIndex+1] + ' CI')

        self.plot()

    def processwords(self, word):
        if(word == "ms"):
            return 'Male Sigma'
        elif (word == 'me'):
            return 'Memory Length'
    
    def plot(self):
        fit_datas = []
        bests=[]
        worsts=[]

        for stack1 in self.fitfilenames:
            fit_data = []
            for file1 in stack1:
                df1 = pd.read_csv(file1, index_col=False).reset_index()
                fit_data.append(df1)
            fit_datas.append(fit_data) 
            
        for stack2 in self.genofilenames:
            best_data = []
            worst_data = []
            for file2 in stack2:
                df2 = pd.read_csv(file2, index_col=False)
                best_data.append(df2.loc[:, df2.columns!='Generation'].filter(regex="^best_mate"))
                worst_data.append(df2.loc[:, df2.columns!='Generation'].filter(regex="^worst_mate"))
            bests.append(best_data)
            worsts.append(worst_data)

        for x in range(len(fit_datas)):
            fit_datas[x] = pd.concat(objs=fit_datas[x], ignore_index=True)
            bests[x] = pd.concat(objs=bests[x]).groupby(level=0).mean().T
            worsts[x] = pd.concat(objs = worsts[x]).groupby(level=0).mean().T

        self.plotFigWOThre(fit_datas, bests, worsts)

    def plotFig(self, data1, foo, geno):
        axd = plt.figure(figsize=(14,10)).subplot_mosaic(
        """
        AB
        CC
        DD
        """,
        )
        for y in range(len(self.names)):
            
            color = iter(plt.cm.rainbow(np.linspace(0, 1, len(data1))))
            
            for x in range(len(data1)):
                c=next(color)
                data1[x].plot(x='Generation', y=self.names[y], ax=list(axd.values())[y], kind='scatter', label=x, c=c,)
        
            sns.regplot(x=foo['Generation'],y=foo[self.names[y]], lowess=True, scatter=False, ax = list(axd.values())[y])
            list(axd.values())[y].set(xlabel='Generation', ylabel=self.labels[y])

        axd['C'] = sns.heatmap(geno)
        axd['C'].invert_yaxis()
        axd['C'].set(xlabel='Generation', ylabel='Steps', title='Mate Percentage for each step')

        axd['D'] = sns.heatmap(geno)
        axd['D'].invert_yaxis()
        axd['D'].set(xlabel='Generation', ylabel='Steps', title='Mate Percentage for each step')

        
        identify_axes(axd)
        # plt.show()
        plt.savefig(self.output + ".png")

    def plotFigWOThre(self, fitdatas, best, worst):
        axd = plt.figure(figsize=(14,8)).subplot_mosaic(
        """
        AB
        CC
        DD
        """,
        )
        colo = iter(plt.cm.rainbow(np.linspace(0, 1, len(fitdatas))))
        for fit_cancat in fitdatas:
            c = next(colo)

            self.lineplot(axd['A'],fit_cancat,'Ave_Fitness',"Average Fitness",c)
            self.lineplot(axd['B'],fit_cancat,'All_Mate',"All Mating Steps",c)
            
        axd['A'].legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))
        axd['B'].legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))

        self.plotHeatmap(axd['C'], pd.concat(objs=best).to_numpy(), 'Best Female', 'Steps')
        self.plotHeatmap(axd['D'], pd.concat(objs=worst).to_numpy(), 'Worst Female', 'Steps')
        
        identify_axes(axd)
        plt.tight_layout()
        plt.show()
        # plt.savefig(self.output + ".png")

    def lineplot(self, ax, li,y, ylabel, c):
        sns.lineplot(
            data=li,
            ax=ax,
            x=li["Generation"], y=li[y],
            marker='', color = c
        )
        ax.set(xlabel='Generation', ylabel=ylabel)

    def plotHeatmap(self, ax, li, title, ylabel):
        sns.heatmap(li, ax =ax)
        ax.invert_yaxis()
        ax.set(xlabel='Generation', ylabel=ylabel, title=title)

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