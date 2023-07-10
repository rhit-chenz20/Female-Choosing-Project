import argparse
import pandas as pd
import re

parser = argparse.ArgumentParser(description='filter csv')
parser.add_argument('-nf', '--filename', type=str) # no sperm competition filename
parser.add_argument('-fn', '--filenames', type=str, nargs="*") # files with sperm competition
parser.add_argument('-bv', '--baseValue', type=float)
parser.add_argument('-be', '--baseEqulity', type=int, required=False, default=1)
parser.add_argument('-sv', '--scVlue', type=float)
parser.add_argument('-se', '--scEqulity', type=int, required=False, default=1)
parser.add_argument('-o', '--outputFile', type=str)
args = parser.parse_args()

def mean_normalize_column(df: pd.DataFrame, col:str):
    mean = df[col].mean()
    df[col] = df[col]/mean

def process_csv(filename, filter_value, equlity):
    df_scaled = pd.read_csv(filename)
    df_scaled.set_index('Genome')
    mean_normalize_column(df_scaled, "Ave_fit")
    if(equlity==0):
        df_scaled = df_scaled[df_scaled['Ave_fit'] <= filter_value]
    elif(equlity==1):
        df_scaled = df_scaled[df_scaled['Ave_fit'] >= filter_value]
    return df_scaled


# for non_sc csv
no_sc_df = process_csv(args.filename, args.baseValue, args.baseEqulity)

# for sc csv
for filename in args.filenames:
    if(re.search(".csv", filename)):
        fitbase = re.search('fitbase_(.+?)_', filename).group(1)
        sc_df = process_csv(filename, args.scVlue, args.scEqulity)
        df_joined = no_sc_df.merge(sc_df, on='Genome', how='inner').set_index('Genome')
        
        if(args.baseEqulity==0):
            fn = args.outputFile+"_fb_"+fitbase+"_ble_" + str(args.baseValue)
        elif(args.baseEqulity==1):
            fn = args.outputFile+"_fb_"+fitbase+"_bge_" + str(args.baseValue)
        
        if(args.scEqulity==0):
            fn += "_sle_"+ str(args.scVlue)
        elif(args.scEqulity==1):
            fn += "_sge_"+ str(args.scVlue)
        
        
        df_joined.to_csv(fn +".csv")
