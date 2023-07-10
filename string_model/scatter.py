import matplotlib.pyplot as plt
import pandas as pd
import re

def mean_normalize_column(df: pd.DataFrame, col:str):
    mean = df[col].mean()
    df[col] = df[col]/mean

filenames = ["result/June11/CSV/ml_10_ms_10_fit_2_fb_0.25_1_models.csv",
             "result/June11/CSV/ml_10_ms_10_fit_2_fb_0.5_1_models.csv",
             "result/June11/CSV/ml_10_ms_10_fit_2_fb_0.75_1_models.csv",
             "result/June11/CSV/ml_10_ms_10_fit_2_fb_1_1_models.csv"]

base_files = [
    "base.csv", 
            #   "base_ave.csv"
              ]

outputFilename = "poster/lowest_base_full.png"

for base in base_files:
    plt.figure(figsize = (10,8))
    plt.plot([1,1],[0.5, 1.2], '--', linewidth=1, color='black', alpha=0.6)
    plt.plot([0.0, 2.1],[1,1], '--', linewidth=1, color='black', alpha=0.6)
    base_df = pd.read_csv(base)
    mean_normalize_column(base_df, "Ave_fit")
    for filename in filenames:
        df = pd.read_csv(filename)
        mean_normalize_column(df, "Ave_fit")
        fitbase = re.search('fb_(.+?)_', filename).group(1)
        name = "s = " + fitbase
        plt.scatter(x=df["Ave_fit"], y=base_df["Ave_fit"], marker= ".", label=name)
    
    plt.xlabel('Normalized Fitness with Last Male Sperm Precedence', fontsize=15)
    plt.ylabel('Normalized Fitness without Last Male Sperm Precedence', fontsize=15)
    plt.ylim([0.5, 1.15])
    plt.xlim([0.1, 2.1])
    legend = plt.legend(title="LMSP Strength", loc=4, fontsize="18")
    plt.setp(legend.get_title(),fontsize='x-large')
    # plt.show()
    plt.savefig(outputFilename)