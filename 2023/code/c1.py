import pandas as pd

data = pd.read_csv("../data/d1.txt", header=None)

data = [line for line in data[0]]

print(data)