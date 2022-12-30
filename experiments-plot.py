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
parser.add_argument("--method", help="Either rejection method or penalty method")

args = parser.parse_args()

print(f"Given data: {vars(args)}")

file = args.file
function = args.function
to_plot = args.toPlot
method = args.method

file = path + '/' + file
filename = os.fsdecode(file)
data = pd.read_csv(filename, header=6)

df = pd.DataFrame(data)

sns.barplot(data=df, y=list(df['global-best-val']), x=list(df[to_plot]), errorbar=None)
plt.title("Global best value depending on " + to_plot + "for function " + function)
plt.xlabel(to_plot)
plt.ylabel("Global best value")

plt.show()

