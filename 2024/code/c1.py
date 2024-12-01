import numpy as np

data =np.loadtxt("../data/d1.txt")

# Part 1
x = np.sort(data[:, 0])
y = np.sort(data[:, 1])

print(sum(abs(x - y)))

# Part2
x = data[:, 0]
y = data[:, 1]

s = 0
for num in x:
    s += num * sum(y == num)

print(s)


