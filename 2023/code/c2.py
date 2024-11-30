import pandas as pd

data = pd.read_csv("../data/d2.txt", header=None)

data = [[character for character in line] for line in data[0]]

print(data)
