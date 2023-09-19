import os
import pandas as pd
import numpy as np
import altair as alt

# os.getcwd()
root = "/Users/cynthiaxu/PycharmProjects/"
github_path = "209-ds-salaries-viz-project/data/"
data_path = os.path.join(root, github_path)
data_files = os.listdir(data_path)


data_dict = {}
for i in data_files:
    if '.csv' in i:
        df = pd.read_csv(os.path.join(data_path, i))
        name = i[:-4]
        data_dict[name] = df

keys = data_dict.keys()

print(keys)


