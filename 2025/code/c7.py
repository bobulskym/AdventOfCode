with open('../data/d7.txt', 'r') as file:
    data = [[item for item in line.strip()] for line in file]


r = 0
c = data[0].index("S")

m = len(data)
n = len(data[0])


splitters = []
def move(r, c):

    global splitters

    while data[r][c] == "S" or data[r][c] == ".":
        r += 1
        if r == m:
            break

    if r < m:
        if (r, c) not in splitters:

            splitters.append((r, c))

            if c > 0:
                move(r, c - 1)

            if c < (n - 1):
                move(r, c + 1)


memory = {}
def move2(r, c):

    global memory
    count = 0

    while data[r][c] == "S" or data[r][c] == ".":
        r += 1
        if r == m:
            break

    if r < m:
        if (r, c) not in memory:
            memory[(r, c)] = move2(r, c - 1)
            memory[(r, c)] += move2(r, c + 1)
        count += memory[(r, c)]
    else:
        count = 1

    return count


move(r, c)
count = move2(r, c)


print("Part 1: " + str(len(splitters)))
print("Part 2: " + str(count))