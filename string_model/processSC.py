import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import re

parser = argparse.ArgumentParser(description='Process CSV for sperm competition')
# parser.add_argument('-nf', '--filename', type=str) # no sperm competition filename
parser.add_argument('-fn', '--filenames', type=str, nargs="*") # files with sperm competition
parser.add_argument('-o', '--outputFile', type=str)
args = parser.parse_args()

annotate_points = ["[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]",
                   "[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]",
                #    "[1, 0, 0, 0, 0, 0, 1, 1, 1, 1]",
                #    "[1, 0, 0, 0, 0, 1, 1, 1, 1, 0]",
                   "[1, 1, 1, 0, 0, 0, 0, 0, 0, 1]",
                   "[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]",
                   "[1, 1, 1, 0, 0, 0, 0, 0, 0, 0]",
                #    "[1, 1, 0, 0, 0, 0, 0, 0, 0, 1]",
                   "[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]",
                   "[1, 0, 0, 0, 0, 0, 0, 0, 0, 1]",
                   "[1, 0, 0, 0, 0, 0, 1, 0, 0, 0]",
                   "[1, 0, 1, 1, 1, 1, 1, 1, 1, 1]",
                   "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]",
                   "[1, 1, 0, 1, 1, 1, 0, 1, 1, 0]",
                #    "[1, 0, 1, 1, 0, 0, 1, 1, 1, 0]",
                   "[1, 1, 1, 1, 1, 1, 1, 0, 0, 0]",
                   "[1, 1, 1, 1, 1, 1, 0, 0, 0, 0]",
                   "[1, 0, 0, 0, 1, 1, 1, 1, 0, 0]",
                   "[1, 0, 0, 0, 0, 0, 1, 1, 1, 0]",
                   "[1, 0, 0, 0, 0, 0, 0, 0, 1, 1]",
                #    "[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]"
                   ]

percent = 0.05
# scaled_no_sc_df = pd.read_csv(args.filename)

fig, ax = plt.subplots(1, figsize=(10, 8))

for filename in args.filenames:
    fitbase = re.search('fb_(.+?)_', filename).group(1)
    name = "fitbase = " + fitbase
    df_scaled = pd.read_csv(filename)
    plt.scatter(color='green',x=df_scaled["Ave_fit_y"], y=df_scaled["Ave_fit_x"], label = name, marker=".", s=13**2)
    # df_scaled = df_scaled.sort_values("Ave_fit_x", ascending = False).head(n = int(len(df_scaled.index)*percent))
    xvalue = df_scaled["Ave_fit_y"]
    yvalue=df_scaled["Ave_fit_x"]
    # plt.scatter(x=xvalue, y=yvalue, label = name, marker=".")
    for i, txt in enumerate(df_scaled["Genome"]):
        if(txt in annotate_points):
            genome = txt.replace(", ", "").replace("[", "", 1).replace("]", "", 1)
            plt.annotate(genome, (xvalue.values[i], yvalue.values[i]), fontsize=15)
    
# plt.scatter(x=scaled_no_sc_df["Ave_fit"], y=scaled_no_sc_df["Ave_fit"], label = "no SC", marker=".")

# plt.legend()
plt.xlabel('Normalized Fitness with Last Male Sperm Precedence', fontsize=15)
plt.ylabel('Normalized Fitness without Last Male Sperm Precedence', fontsize=15)
# plt.box(on=False)
for axis in ['bottom','left']:
    ax.spines[axis].set_linewidth(3)
for axis in ['top','right']:
    ax.spines[axis].set_linewidth(0)
# ax.tick_params(width=4)
ax.tick_params('both', length=8, width=3, which='major', labelsize=15)
# plt.show()
# plt.savefig("poster/fb_"+str(fitbase)+"_first.png")
# plt.savefig("poster/fb_"+str(fitbase)+"_second.png")
# plt.savefig("poster/fb_"+str(fitbase)+"_third.png")
plt.savefig("poster/fb_"+str(fitbase)+"_fourth.png")