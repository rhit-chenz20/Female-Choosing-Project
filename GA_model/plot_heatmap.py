import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load all files ending with 'test.csv'
file_list = glob.glob("../result/Oct28_24/CSV/Learning/*test.csv")
data_frames = [pd.read_csv(file) for file in file_list]

# Step 2: Stack and take the average for each cell position
# Concatenate along a new axis and take the mean
stacked_data = np.stack([df.values for df in data_frames])
mean_data = np.mean(stacked_data, axis=0)

# Convert to DataFrame for easy plotting, transpose, and reverse rows
mean_df = pd.DataFrame(mean_data, columns=data_frames[0].columns).T.iloc[::-1]

# Set font scale for larger text
sns.set_theme(font_scale=2)

# Step 3: Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(mean_df, cmap="YlGnBu")
plt.xlabel("Generation")
plt.ylabel("Genome")
# plt.title("Heatmap of Averaged Values Across CSV Files")
plt.show()