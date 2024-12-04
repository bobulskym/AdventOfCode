with open('../data/d4.txt', 'r') as file:
    data = [[character for character in line.strip()] for line in file]

m = len(data)
n = len(data[0])

# Part 1
down = [0, 1, 1, 1, 0, -1, -1, -1]
right = [1, 1, 0, -1, -1, -1, 0, 1]

count = 0
for i in range(m):
    for j in range(n):
        for d, r in zip(down, right):

            word = ''
            for k in range(4):
                
                ni = i + k * d
                nj = j + k * r
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    word += data[ni][nj]
            
            count += word == "XMAS"
            

print("Part 1: " + str(count))


# Part 2
opt = ['MAS', 'SAM']
count = 0
for i in range(1, m - 1):
    for j in range(1, n - 1):
        
        if data[i][j] == 'A':
            d1 = data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1]
            d2 = data[i + 1][j - 1] + data[i][j] + data[i - 1][j + 1]
            if d1 in opt and d2 in opt:
                count += 1

print("Part 2: " + str(count))