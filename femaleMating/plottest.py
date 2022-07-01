# libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#------------------3D--------------
file = "CSVResultFiles/June29/test_geno.csv"
df = pd.read_csv(file)
data = df.loc[:, df.columns!='Generation']

df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# # And transform the old column name in something numeric
df['X']=pd.Categorical(df['X'])
df['X']=df['X'].cat.codes
 
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
plt.show()
# plt.savefig("femaleMating/sample/3d.png")


#------------2D-------------

data = data.to_numpy().T
# #--------------seaborn heatmap-------------
# ax = sns.heatmap(data)
# ax.invert_yaxis()
# ax.set(xlabel='Generation', ylabel='Steps')
# plt.show()

#---------------imshow---------------
# fig, ax = plt.subplots(
#     figsize=(18, 2)
#     )
# im = ax.imshow(data,interpolation='nearest', 
# # aspect='auto'
# )

# # Show all ticks and label them with the respective list entries
# ax.set_yticks(np.arange(len(df.columns)))
# ax.set(xlabel='Generation', ylabel='Steps')
# ax.invert_yaxis()
# # Create colorbar
# cbar = ax.figure.colorbar(im, ax=ax)
# cbar.ax.set_ylabel('Percentage', rotation=-90, va="bottom")

# # Rotate the tick labels and set their alignment.
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#          rotation_mode="anchor")

# ax.set_title("Mate step percentage over life time/generation")
# fig.tight_layout()
# plt.show()
# plt.savefig("femaleMating/sample/seaborn.png")