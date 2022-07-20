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
        lastfilenames,
        output,
        outfolder
        ):
        # self.names = ["Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        self.names = ["Generation","Ave_Fitness", "All_Mate",]
        # self.genonames = ['best_mate', 'worst_mate']
        self.lastnames = ["Mating_Steps", "Fitness_Mating", "Num_Look_Before_1_Mating"]
        self.labels = ['Average Fitness', 'Sta Dev Fitness', 'Average Threshold', 'Sta Dev Threshold']
        # self.fignames = ['ave_fit', 'sta_fit', 'ave_the', 'sta_the']
        self.output = 'ResultPlot/' + outfolder
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        self.output += "/" + output

        self.fitfilenames = []
        self.lastfilenames = []
        dictionary = {}  
        for x in fitfilenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = dictionary.get(key,[])
            group.append(x)  
            dictionary[key] = group
        self.fitfilenames = dictionary.values()

        gdictionary = {}  
        for x in lastfilenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = gdictionary.get(key,[])
            group.append(x)  
            gdictionary[key] = group

        self.lastfilenames = gdictionary.values()
        # print(list(gdictionary.keys()))

        sample1 = list(dictionary.keys())[0].split('_')
        sample2 = list(dictionary.keys())[1].split('_')
        diIndex = 0
        for x in range(len(sample1)):
            if(sample1[x] != sample2[x]):
                diIndex = x-1
                break

        self.legends = []
        for key in dictionary.keys():
            li = key.split('_')
            label = self.processwords(diIndex, li)
            self.legends.append(label)
            self.legends.append(label + ' CI')                

        self.plot()

    def processwords(self, index, li:list):
        if(li[index] == "ms"):
            return 'Male Sigma ' + li[index+1]
        elif (li[index] == 'me'):
            return 'Memory Length ' + li[index+1]
        elif(li[index] == "ml"):
            return 'Mating Length ' + li[index+1]
        elif(li[index] == 'fmu'):
            return 'Female Mu ' + li[index+1]
        elif (li[index] == 'selper'):
            return 'Selection Percent ' + li[index+1]
        elif(li[index] == 'fit'):
            spe=''
            if(li[index+1] == '0'):
                spe = 'Average males fitness'
            elif(li[index+1] == '1'):
                spe = 'Lowest male fitness'
            # print(spe)
            return spe
        elif(li[index] == 'fsigma'):
            return 'Female Sigma ' + li[index+1]
        elif(li[index] == 'cost'):
            return 'Flat Cost ' + li[index+1]
    
    def plot(self):
        fit_datas = []
        bests=[]
        worsts=[]
        lasts = []

        for stack1 in self.fitfilenames:
            fit_data = []
            best_data = []
            worst_data = []
            for file1 in stack1:
                df1 = pd.read_csv(file1, index_col=False).reset_index()
                fit_data.append(df1.filter(items=self.names))
                best_data.append(df1.loc[:, df1.columns!='Generation'].filter(regex="^best_mate"))
                worst_data.append(df1.loc[:, df1.columns!='Generation'].filter(regex="^worst_mate"))
            fit_datas.append(fit_data) 
            bests.append(best_data)
            worsts.append(worst_data)
            
        for stack2 in self.lastfilenames:
            last = []
            for file2 in stack2:
                df2 = pd.read_csv(file2, index_col=False)
                last.append(df2)
            lasts.append(last)

        for x in range(len(fit_datas)):
            fit_datas[x] = pd.concat(objs=fit_datas[x], ignore_index=True)
            bests[x] = pd.concat(objs=bests[x]).groupby(level=0).mean().T
            worsts[x] = pd.concat(objs = worsts[x]).groupby(level=0).mean().T
            lasts[x] = pd.concat(objs = lasts[x]).groupby(level=0).mean()
            # print(lasts[x])

        self.plotFigWOThre(fit_datas, bests, worsts, lasts)

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

    def plotFigWOThre(self, fitdatas, best, worst, lasts):
        mosaic = "AB\nCD"

        letters = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

        for x in range(2*len(best)):
            mosaic+="\n"+letters[x]+letters[x]

        mosaic = """{}""".format(mosaic)

        axd = plt.figure(figsize=(18,len(best)*10)).subplot_mosaic(mosaic)
        colo = iter(plt.cm.rainbow(np.linspace(0, 1, len(fitdatas))))
        for x in range(len(fitdatas)):
            c = next(colo)
            self.lineplot(axd['A'],fitdatas[x],'Generation','Ave_Fitness',"Generation","Average Fitness",c)
            self.lineplot(axd['B'],fitdatas[x],'Generation','All_Mate',"Generation","All Mating Steps",c)
            sns.regplot(x=lasts[x]['Mating_Steps'],y=lasts[x]['Fitness_Mating'], lowess=True, scatter=True, ax = axd['C'], color = c, ci=95)
            sns.regplot(x=lasts[x]['Num_Look_Before_1_Mating'],y=lasts[x]['Fitness_Mating'], lowess=True, scatter=True, ax = axd['D'], color = c, ci=95)
            # self.lineplot(axd['C'],lasts[x],'Mating_Steps','Fitness_Mating',"Mating Steps","Female's Fitness",c)
            # self.lineplot(axd['D'],lasts[x],'Num_Look_Before_1_Mating','Fitness_Mating',"Look Steps before First Mate","Female's Fitness",c)

        for x in range(len(best)):
            self.plotHeatmap(axd[letters[2*x]], best[x].to_numpy(), 'Best Female of '+self.legends[2*x], 'Steps')
            self.plotHeatmap(axd[letters[2*x+1]], worst[x].to_numpy(), 'Worst Female of '+self.legends[2*x], 'Steps')
            # self.plotHeatmap(axd[letters[2*x]], best[x].to_numpy(), 'Best Female of ', 'Steps')
            # self.plotHeatmap(axd[letters[2*x+1]], worst[x].to_numpy(), 'Worst Female of ', 'Steps')
        
        identify_axes(axd)
        plt.tight_layout()
        # plt.show()
        plt.savefig(self.output + ".pdf")

    def lineplot(self, ax, li, x,y,xlabel, ylabel, c):
        sns.lineplot(
            data=li,
            ax=ax,
            x=li[x], y=li[y],
            marker='', color = c
        )
        ax.set(xlabel=xlabel, ylabel=ylabel)
        ax.legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))

    def plotHeatmap(self, ax, li, title, ylabel):
        sns.heatmap(li, ax =ax, cmap="Greens",vmin=0, vmax=1)
        ax.invert_yaxis()
        ax.set(xlabel='Generation', ylabel=ylabel, title=title)
        c_bar = ax.collections[0].colorbar
        c_bar.set_ticks([0, 0.25, 0.5, 0.75, 1])
        c_bar.set_ticklabels(["0% Female Mate", "25% Female Mate", "50% Female Mate", "75% Female Mate", "100% Female Mate", ])

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