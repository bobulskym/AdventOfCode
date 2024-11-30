import pandas as pd

data = pd.read_csv("../data/template_data.txt", header=None)

data = [[character for character in line] for line in data[0]]

print(data)
