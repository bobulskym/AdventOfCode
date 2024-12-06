with open('../data/d6.txt', 'r') as file:
    map = [[character for character in line.strip()] for line in file]
    
m = len(map)
n = len(map[0])

for i in range(m):
    for j in range(n):
        if map[i][j] in ['^', '>', 'v', '<']:
            pos = (i, j)

dir = map[pos[0]][pos[1]]
            

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
path = []
loop = [0]

def move(pos, dir, part_one = True):
    
    if part_one and pos not in path:
        path.append(pos)

    new_pos = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
    
    while new_pos[0] >= 0 and new_pos[0] < m and new_pos[1] >= 0 and new_pos[1] < n and map[new_pos[0]][new_pos[1]] not in ['#', 'O']:
        if part_one and new_pos not in path:
            path.append(new_pos)

        new_pos = (new_pos[0] + directions[dir][0], new_pos[1] + directions[dir][1])
    
    if new_pos[0] >= 0 and new_pos[0] < m and new_pos[1] >= 0 and new_pos[1] < n:
        curr_pos = (new_pos[0] - directions[dir][0], new_pos[1] - directions[dir][1])
        curr_pos_full = (new_pos[0] - directions[dir][0], new_pos[1] - directions[dir][1], dir)
        
        if curr_pos_full not in visited:
            visited.append(curr_pos_full)
            move(curr_pos, next_dir[dir], part_one)
        else:
            loop[0] += 1


# Part 1
move(pos, dir)
print("Part 1: " + str(len(path)))


# Part 2
path.pop(0)
for i, j in path:
    visited = []
    map[i][j] = 'O'
    move(pos, dir, part_one = False)    
    map[i][j] = '.'

print("Part 2: " + str(loop[0]))



