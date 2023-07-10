import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('-fn', '--filenames', type=str, nargs="*")
parser.add_argument('-o', '--outputFile', type=str)
parser.add_argument('-t', '--topPercent', type=float, required= False, default=1.0)
parser.add_argument('-c', '--cross_file', type=int, required= False, default=0)
args = parser.parse_args()

fig, ax = plt.subplots(1, figsize = (14,7))
op_i=0
width=0.2
N=10
ind = np.arange(N)

def plot_bar(df, op_i, label_name, color=None):
    if(len(df["Genome"])>0):
        su = [0] * len(df["Genome"].values[0].split(","))
        # x_label = range(len(df["Genome"][0].split(",")))
        for g in df["Genome"]:
            genome = [int(x) for x in g.split("[", 1)[1].split("]", 1)[0].split(",")]
            for i in range(len(genome)):
                su[i] += genome[i]
        
        su = list(map(lambda x: 100*x/int(len(df.index)*args.topPercent),su))
        # creating the bar plot
        if(color):
            plt.bar(ind+op_i*width, su, width, label = label_name, color = color)
        else:
            plt.bar(ind+op_i*width, su, width, label = label_name)


if(args.cross_file == 0):
    # df = df.sort_values(args.column, ascending = False).head(n = int(len(df.index)*args.topPercent))
    # data_series = []
    for filename in args.filenames:
        df = pd.read_csv(filename)
        plot_bar(df, op_i, re.search('fb_(.+?)_', filename).group(1))
        op_i+=1
elif(args.cross_file == 1):
    filenames = [
        "result/June11/CSV/processed/lowest_base_fb_0.75_bge_1.0_sle_1.0.csv",
        "result/June11/CSV/processed/lowest_base_fb_0.75_bge_1.0_sge_1.0.csv",
        "result/June11/CSV/processed/lowest_base_fb_0.75_ble_1.0_sle_1.0.csv",
        "result/June11/CSV/processed/lowest_base_fb_0.75_ble_1.0_sge_1.0.csv",
    ]
    colors = ['#5C7ED1', '#D15CB8', '#D1745C', '#755CD1']
    for filename in filenames:
        df = pd.read_csv(filename)
        name = re.search('fb_*_(.+?).csv', filename).group(1)
        name = name.split("_")
        if(name[1]=='bge'):
            if(name[3]=='sge'):
                name = "B"
            elif(name[3]=='sle'):
                name = "A"
        elif(name[1]=='ble'):
            if(name[3]=='sge'):
                name = "D"
            elif(name[3]=='sle'):    
                name = "C"        
        plot_bar(df, op_i, name, colors[op_i])
        
        op_i+=1
elif(args.cross_file == 2):
    filenames = [
        "result/May12/CSV/ml_10_ms_10_fit_1_1_models.csv",
        "result/May12/CSV/ml_10_ms_5_fit_1_1_models.csv",
        "result/May12/CSV/ml_10_ms_1_fit_1_1_models.csv",
    ]
    percent = 0.25
    column = "Sum_fit"
    colors = ['#D15C5C','#D1D15C', '#5CD197']
    for filename in filenames:
        df = pd.read_csv(filename)
        df = df.sort_values(column, ascending = False).head(n = int(len(df.index)*percent))
        name = re.search('ms_(.+?)_', filename).group(1)
        name = "male variance = "+name
        plot_bar(df, op_i, name, colors[op_i])
        op_i+=1

plt.xlabel("Female Genome Position", fontsize=25)
plt.ylabel("% of Females Who Learn", fontsize=25)
plt.xticks(ind + width / 2, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), fontsize=10)
for axis in ['bottom','left']:
    ax.spines[axis].set_linewidth(3)
for axis in ['top','right']:
    ax.spines[axis].set_linewidth(0)
# ax.tick_params(width=4)
ax.tick_params('both', length=8, width=3, which='major', labelsize=15)
# plt.legend()
plt.savefig(args.outputFile)
# plt.show()
