import os
import pandas as pd

path = os.path.abspath('')

directory = path + '/experiments/new-experiments'
files = os.listdir(directory)
count = 0
for file in files:
    filename = os.fsdecode(file)
    if (filename.endswith ('.csv')):
        df = pd.read_csv(os.path.join(directory, filename), header=6)
        count += len(df)

print (count)
