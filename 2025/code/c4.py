with open('../data/d4.txt', 'r') as file:
    data = [[item for item in line.strip()] for line in file]


m = len(data)
n = len(data[0])


def exists(r, c):

    if 0 <= r < m and 0 <= c < n:
        return True
    
    return False

def forklift(r, c):

    count = 0
    dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for dir in dirs:
        nr = r + dir[0]
        nc = c + dir[1]
        if exists(nr, nc):
            if data[nr][nc] == "@":
                count += 1

    return count < 4

def findrolls():

    tbr = []

    for i in range(m):
        for j in range(n):
            if data[i][j] == "@" and forklift(i, j):
                tbr.append((i, j))

    return tbr

def removerolls(tbr):

    for pos in tbr:
        data[pos[0]][pos[1]] = "."


k = 1
result1 = 0
result2 = 0

while True:

    tbr = findrolls()

    if len(tbr) == 0:
        break
    
    if k == 1:
        result1 += len(tbr)

    result2 += len(tbr)

    removerolls(tbr)

    k += 1


print("Part 1: " + str(result1))
print("Part 2: " + str(result2))