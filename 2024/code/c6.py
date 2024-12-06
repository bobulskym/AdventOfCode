with open('../data/d6.txt', 'r') as file:
    map = [[character for character in line.strip()] for line in file]
    mapX = [line[:] for line in map]
    
m = len(map)
n = len(map[0])

for i in range(m):
    for j in range(n):
        if map[i][j] in ['^', '>', 'v', '<']:
            pos = (i, j)
            

directions = {
    '^' : (-1, 0),
    '>' : (0, 1),
    'v' : (1, 0),
    '<' : (0, -1)
}

next_dir = {
    '^' : '>',
    '>' : 'v',
    'v' : '<',
    '<' : '^'
}

visited = []

loop = [0]

def move(pos, dir):
    
    mapX[pos[0]][pos[1]] = 'X'
    new_pos = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
    
    while new_pos[0] >= 0 and new_pos[0] < m and new_pos[1] >= 0 and new_pos[1] < n and map[new_pos[0]][new_pos[1]] not in ['#', 'O']:
        mapX[new_pos[0]][new_pos[1]] = 'X'
        new_pos = (new_pos[0] + directions[dir][0], new_pos[1] + directions[dir][1])
    
    if new_pos[0] >= 0 and new_pos[0] < m and new_pos[1] >= 0 and new_pos[1] < n:
        curr_pos = (new_pos[0] - directions[dir][0], new_pos[1] - directions[dir][1])
        curr_pos_full = (new_pos[0] - directions[dir][0], new_pos[1] - directions[dir][1], dir)
        
        if curr_pos_full not in visited:
            visited.append(curr_pos_full)
            move(curr_pos, next_dir[dir])
        else:
            loop[0] += 1

# Part 1
move(pos, map[pos[0]][pos[1]])

count = 0
for i in range(m):
    for j in range(n):
        if mapX[i][j] == 'X':
            count += 1

print("Part 1: " + str(count))


# Part 2
map_backup = [line[:] for line in map]

for i in range(m):
    for j in range(n):
        if map_backup[i][j] not in ['^', '>', 'v', '<', '#']:
            map = [line[:] for line in map_backup]
            visited = []
            map[i][j] = 'O'
            move(pos, map[pos[0]][pos[1]])            

print("Part 2: " + str(loop[0]))



