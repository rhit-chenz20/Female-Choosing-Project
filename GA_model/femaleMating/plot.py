import numpy as np
import seaborn as sns
import sys
import pandas as pd
import matplotlib.pyplot as plt

# get help from https://stackoverflow.com/a/48126960
class Plot():
    def __init__(
        self,
        fitfilenames,
        lastfilenames,
        output,
        type,
        debug,
        gap
        ):
        self.genoNames = ["Generation","Ave_Fitness", "All_Mate",]
        # self.genonames = ['best_mate', 'worst_mate']
        self.lastnames = ["Mating_Steps", "Fitness_Mating", "Num_Look_Before_1_Mating"]
        # self.fignames = ["Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        self.output = output
        self.debug = debug
        self.gap = gap
        self._setup_filename(fitfilenames,lastfilenames, type)
        sys.argv

    def _setup_filename(self,ffilenames,lfilenames, type):
        fitfilenames = []
        lastfilenames = []
        dictionary = {}  
        for x in ffilenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = dictionary.get(key,[])
            group.append(x)  
            dictionary[key] = group
        fitfilenames = dictionary.values()

        gdictionary = {}  
        for x in lfilenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = gdictionary.get(key,[])
            group.append(x)  
            gdictionary[key] = group

        lastfilenames = gdictionary.values()

        samples = []
        for key in dictionary.keys():
            sample1 = key.split('/')
            samples.append(sample1[len(sample1)-1].split('_'))

        diIndex = 0
        for x in range(len(samples[1])):
            if samples[1][x] != samples[0][x]:
                diIndex = x-1

        self.legends = []
        for sample in samples:
            label = self._processwords(diIndex, sample)
            self.legends.append(label) 
            self.legends.append(label+" CI") 

        if(type == 1):
            self._dataProcessGeno(fitfilenames, lastfilenames)    
        elif(type ==0):
            self._dataProcessThre(fitfilenames, lastfilenames)        

    def _processwords(self, index, li:list):
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
            elif(li[index+1] == '2'):
                spe = 'Last Sperm Precedence'
            return spe
        elif(li[index] == 'fsigma'):
            return 'Female Sigma ' + li[index+1]
        elif(li[index] == 'cost'):
            return 'Flat Cost ' + li[index+1]
        elif(li[index] == 'sel'):
            spe=''
            if(li[index+1] == '0'):
                spe = 'Top 50% Selection'
            elif(li[index+1] == '1'):
                spe = 'Tournament Selection'
            return spe            
    
    def _dataProcessGeno(self, fitfilenames, lastfilenames):
        fit_datas = []
        bests=[]
        worsts=[]
        lasts = []

        for stack1 in fitfilenames:
            fit_data = []
            best_data = []
            worst_data = []
            for file1 in stack1:
                df1 = pd.read_csv(file1, index_col=False).reset_index()
                fit_data.append(df1.filter(items=self.genoNames))
                best_data.append(df1.loc[:, df1.columns!='Generation'].filter(regex="^best_mate"))
                worst_data.append(df1.loc[:, (df1.columns!='Generation') & (df1.index %self.gap == 0)].filter(regex="^worst_mate"))
            fit_datas.append(fit_data) 
            bests.append(best_data)
            worsts.append(worst_data)
            
        for stack2 in lastfilenames:
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

    def _dataProcessThre(self, filenames,lastfilenames):
        thre_datas = []
        datas = []
        lasts = []
        for stack1 in filenames:
            thre_data = []
            for file1 in stack1:
                df1 = pd.read_csv(file1, index_col=False).reset_index()
                thre_data.append(df1)
            thre_datas.append(thre_data) 

        for stack2 in lastfilenames:
            last = []
            for file2 in stack2:
                df2 = pd.read_csv(file2, index_col=False)
                last.append(df2)
            lasts.append(last)
        for x in range(len(thre_datas)):
            datas.append(pd.concat(objs=thre_datas[x], ignore_index=True))
            lasts[x] = pd.concat(objs = lasts[x]).groupby(level=0).mean()
        self.plotFigWTher(thre_datas, datas, lasts)

    def plotFigWTher(self, thre, thre_conc, lasts):
        labels = ['Average Fitness', 'Sta Dev Fitness', 'Average Threshold', 'Sta Dev Threshold']
        threNames = ["Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        letters = ['A','B','C','D']

        axd = plt.figure(figsize=(18,8)).subplot_mosaic(
        """
        AB
        CD
        EE
        """,
        )

        color_lines = iter(plt.cm.rainbow(np.linspace(0, 1, len(self.legends))))

        # n sets of data (same length as legends)
        for x in range(len(thre_conc)):
            c_line=next(color_lines)
            
            # four graph

            for y in range(len(threNames)):
                self.lineplot(axd[letters[y]],thre_conc[x],'Generation',threNames[y],"Generation",labels[y],c_line)
                # for z in range(len(thre[0])):
                #     thre[x][z].plot(x='Generation', y=threNames[y], ax=axd[letters[y]], kind='line', c=c_line,label='_nolegend_')
            axd["E"].hist(lasts[x], color=c_line, alpha=0.5)
                
        #         sns.regplot(x=thre_conc[x]['index'],y=thre_conc[x][threNames[y]], lowess=True, 
        #             scatter=False, ax = list(axd.values())[y], color = c_line, ci=95)
                        #     list(axd.values())[y].set(xlabel='Generation', ylabel=self.labels[y])
        #     
        
        list(axd.values())[1].legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))
        axd["E"].set(xlabel='Number of Matings', ylabel="Number of Females")

        identify_axes(axd)
        plt.tight_layout()
        # plt.show() 
        plt.savefig(self.output + ".pdf")

    def plotFigWOThre(self, fitdatas, best, worst, lasts):
        mosaic = "AB\nCD"

        letters = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O','P','Q','R','S','T', 'U','V']

        for x in range(2*len(best)):
            mosaic+="\n"+letters[x]+letters[x]

        mosaic = """{}""".format(mosaic)

        axd = plt.figure(figsize=(18,len(best)*10)).subplot_mosaic(mosaic)
        colo = iter(plt.cm.rainbow(np.linspace(0, 1, len(fitdatas))))
        for x in range(len(fitdatas)):
            c = next(colo)
            # print(fitdatas[x])
            self.lineplot(axd['A'],fitdatas[x],'Generation','Ave_Fitness',"Generation","Average Fitness",c)
            self.lineplot(axd['B'],fitdatas[x],'Generation','All_Mate',"Generation","All Mating Steps",c)
            sns.regplot(x=lasts[x]['Mating_Steps'],y=lasts[x]['Fitness_Mating'], lowess=True, scatter=True, ax = axd['C'], color = c)
            sns.regplot(x=lasts[x]['Num_Look_Before_1_Mating'],y=lasts[x]['Fitness_Mating'], lowess=True, scatter=True, ax = axd['D'], color = c)
            # self.lineplot(axd['C'],lasts[x],'Mating_Steps','Fitness_Mating',"Mating Steps","Female's Fitness",c)
            # self.lineplot(axd['D'],lasts[x],'Num_Look_Before_1_Mating','Fitness_Mating',"Look Steps before First Mate","Female's Fitness",c)

        for x in range(len(best)):
            self.plotHeatmap(axd[letters[2*x]], best[x].to_numpy(), 'Best Female of '+self.legends[2*x], 'Steps')
            
            self.plotHeatmap(axd[letters[2*x+1]], worst[x].to_numpy(), 'Worst Female of '+self.legends[2*x], 'Steps')
            # self.plotHeatmap(axd[letters[2*x]], best[x].to_numpy(), 'Best Female of ', 'Steps')
            # self.plotHeatmap(axd[letters[2*x+1]], worst[x].to_numpy(), 'Worst Female of ', 'Steps')
        axd["B"].legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))

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
        # ax.legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))

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