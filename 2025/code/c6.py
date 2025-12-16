# Part 1
with open('../data/d6.txt', 'r') as file:
    data = [line.strip().split(" ") for line in file]

a = []
for item in data[0]:
    if item != "":
        a.append(int(item))

b = []
for item in data[1]:
    if item != "":
        b.append(int(item))

c = []
for item in data[2]:
    if item != "":
        c.append(int(item))

d = []
for item in data[3]:
    if item != "":
        d.append(int(item))

operators = []
for item in data[4]:
    if item != "":
        operators.append(item)


result = 0

for i in range(len(operators)):

    if operators[i] == "+":
        result += a[i] + b[i] + c[i] + d[i]
    if operators[i] == "*":
        result += a[i] * b[i] * c[i] * d[i]


print("Part 1: " + str(result))


# Part 2
with open('../data/d6.txt', 'r') as file:
    data = [line.strip() for line in file]


opindex = []

for i in range(len(data[4])):
    if data[4][i] == "+" or data[4][i] == "*":
        opindex.append(i)

n = len(opindex)
opindex.append(len(data[0]))


def get_digit(strnum, k):
    
    n = len(strnum)
    
    if k > n:
        return " "
    else:
        return strnum[k - 1]


result = 0

for i in range(n):

    mat = []

    for line in data[:4]:
        mat.append(line[opindex[i]:opindex[i + 1]])
    
    a = get_digit(mat[0], 4) + get_digit(mat[1], 4) + get_digit(mat[2], 4) + get_digit(mat[3], 4)
    b = get_digit(mat[0], 3) + get_digit(mat[1], 3) + get_digit(mat[2], 3) + get_digit(mat[3], 3)
    c = get_digit(mat[0], 2) + get_digit(mat[1], 2) + get_digit(mat[2], 2) + get_digit(mat[3], 2)
    d = get_digit(mat[0], 1) + get_digit(mat[1], 1) + get_digit(mat[2], 1) + get_digit(mat[3], 1)

    if a.strip() == "":
        a = 0
    else:
        a = int(a)
    
    if b.strip() == "":
        b = 0
    else:
        b = int(b)
    
    if c.strip() == "":
        c = 0
    else:
        c = int(c)
    
    if d.strip() == "":
        d = 0
    else:
        d = int(d)

    obj = [a, b, c, d]
    partial = 1
    for o in obj:
        if o != 0:
            partial *= o
    
    op = data[4][opindex[i]]

    if op == "+":
        result += a + b + c + d
    if op == "*":
        result += partial


print("Part 2: " + str(result))