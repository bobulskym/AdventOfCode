with open('../data/d1.txt', 'r') as file:
    data = [[line[0], int(line.strip()[1:])] for line in file]


pos = 50
result1 = 0
result2 = 0

for rot in data:
    
    if rot[0] == "L":
        dir = -1
    if rot[0] == "R":
        dir = 1 
    
    move = pos + dir * rot[1]

    result2 += abs(move) // 100
    if move <= 0 and pos > 0:
        result2 += 1
    
    pos = move % 100

    if pos == 0:
        result1 += 1


print("Part 1: " + str(result1))
print("Part 2: " + str(result2))