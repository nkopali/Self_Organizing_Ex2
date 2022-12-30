import matplotlib.pyplot as plt
import pandas as pd
import os
import argparse
import seaborn as sns


path = os.path.abspath('')
parser = argparse.ArgumentParser()

parser.add_argument("--file", help="csv file to be used")
parser.add_argument("--function", help="Function which have been used")
parser.add_argument("--toPlot", help="The property to plot")

args = parser.parse_args()

print(f"Given data: {vars(args)}")

file = args.file
function = args.function
to_plot = args.toPlot

filename = os.fsdecode(path + '/' + file)
data = pd.read_csv(filename, header=6)

df = pd.DataFrame(data)

has_constraints = list(df['Constraints'])[0]
constraint_method = list(df['constraint_handling_method'])[0]

df['has-global-best'] = df['iterations'] != 600
df_global_best = df.copy()[df['has-global-best']].groupby(to_plot).agg({'iterations': ['mean','std']})
df_global_best.columns = df_global_best.columns.droplevel()
df_global_best =  df.drop(['iterations'], axis=1).join(df_global_best,on=to_plot).groupby(to_plot).agg({'mean': 'mean','std': 'mean','has-global-best' : 'sum'}).reset_index()
runs = df.shape[0]/df_global_best.shape[0]
df_global_best.loc[:,'has-global-best'] = df_global_best['has-global-best'] / runs

sns.barplot(data=df, y='has-global-best', x=list(df[to_plot]), errorbar=None)
plt.title("% Global best value " + to_plot + " " + function + " " + (constraint_method if has_constraints else 'without constraints'))
plt.xlabel(to_plot)
plt.ylabel("% Global best value")

plt.savefig(filename.replace('csv','png'))

