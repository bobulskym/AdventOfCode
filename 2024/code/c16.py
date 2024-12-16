with open('../data/d16.txt', 'r') as file:
    maze = [[item for item in line.strip()] for line in file]

m = len(maze)
n = len(maze[0])

turns = {
    '^' : ['<', '>'],
    '>' : ['^', 'v'],
    'v' : ['>', '<'],
    '<' : ['v', '^']
}

dirs = {
    '^' : (-1, 0),
    '>' : (0, 1),
    'v' : (1, 0),
    '<' : (0, -1) 
}

def check_if_straight(r, c):
    if maze[r][c] != '.':
        return False
    if maze[r - 1][c] == '.' and maze[r + 1][c] == '.' and maze[r][c - 1] != '.' and maze[r][c + 1] != '.':
        return True
    if maze[r - 1][c] != '.' and maze[r + 1][c] != '.' and maze[r][c - 1] == '.' and maze[r][c + 1] == '.':
        return True
    return False

def find_position(item):
    for i in range(m):
        for j in range(n):
            if maze[i][j] == item:
                maze[i][j] = '.'
                return (i, j)
    return (-1, -1)

def set_node_value(r, c, d, key, value):
    for node in nodes:
        if node['r'] == r and node['c'] == c and node['d'] == d:
            node[key] = value

def get_node_value(r, c, d, key):
    for node in nodes:
        if node['r'] == r and node['c'] == c and node['d'] == d:
            return node[key]
    return "Node doesn't exist!"

def get_tiles(pos1, pos2):
    dr = pos2[0] - pos1[0]
    dc = pos2[1] - pos1[1]

    if dr != 0 and dc != 0:
        return 'Diagonal movement not allowed!'
    
    tiles = [pos1]

    if dr > 0:
        shift_r = 1
        shift_c = 0
    elif dr < 0:
        shift_r = -1
        shift_c = 0
    elif dc > 0:
        shift_r = 0
        shift_c = 1
    elif dc < 0:
        shift_r = 0
        shift_c = -1

    pos = pos1
    while pos != pos2:
        pos = (pos[0] + shift_r, pos[1] + shift_c)
        tiles.append(pos)

    return tiles

def move_back(r, c, d):
    if (r, c, d) != (start[0], start[1], '>'):

        curr_dist = get_node_value(r, c, d, 'dist')
        neighbors = get_node_value(r, c, d, 'neighbors')

        for neighbor in neighbors:
            past_dist = get_node_value(neighbor[0], neighbor[1], neighbor[2], 'dist')
            tiles = get_tiles((r, c), (neighbor[0], neighbor[1]))
            
            if len(tiles) == 1:
                diff = 1000
            else:
                diff = len(tiles) - 1
            
            if past_dist + diff == curr_dist:
                for tile in tiles:
                    all_tiles.add(tile)
                move_back(neighbor[0], neighbor[1], neighbor[2])
            

start = find_position('S')
end = find_position('E')

nodes = []
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if maze[i][j] == '.' and not check_if_straight(i, j):
            for dir in dirs:
                
                node = {
                    'r' : i,
                    'c' : j,
                    'd' : dir,
                    'dist' : float('inf'),
                    'visited' : False,
                    'neighbors' : []
                }
                nodes.append(node)

set_node_value(start[0], start[1], '>', 'dist', 0)

# Dijkstra algorithm
for _ in range(len(nodes)):

    min_dist = float('inf')
    min_r = -1
    min_c = -1
    min_d = ''

    for node in nodes:
        if node['visited'] == False and node['dist'] < min_dist:
            min_dist = node['dist']
            min_r = node['r']
            min_c = node['c']
            min_d = node['d']

    set_node_value(min_r, min_c, min_d, 'visited', True)

    curr = get_node_value(min_r, min_c, min_d, 'dist')

    for dir in turns[min_d]:
        if curr + 1000 < get_node_value(min_r, min_c, dir, 'dist'):
            set_node_value(min_r, min_c, dir, 'dist', curr + 1000)
        set_node_value(min_r, min_c, dir, 'neighbors', get_node_value(min_r, min_c, dir, 'neighbors') + [(min_r, min_c, min_d)])

    dr, dc = dirs[min_d]
    if maze[min_r + dr][min_c + dc] == '.':
        pos = (min_r, min_c)
        dist = 0
        while True:
            dist += 1
            pos = (pos[0] + dr, pos[1] + dc)
            if not check_if_straight(pos[0], pos[1]):

                if curr + dist < get_node_value(pos[0], pos[1], min_d, 'dist'):
                    set_node_value(pos[0], pos[1], min_d, 'dist', curr + dist)
                set_node_value(pos[0], pos[1], min_d, 'neighbors', get_node_value(pos[0], pos[1], min_d, 'neighbors') + [(min_r, min_c, min_d)])

                break


# Part 1
result = float('inf')
for dir in dirs:
    result = min(result, get_node_value(end[0], end[1], dir, 'dist'))

print("Part 1: " + str(result))


# Part 2
check = []
for node in nodes:
    if node['r'] == end[0] and node['c'] == end[1] and node['dist'] == result:
        check.append((node['r'], node['c'], node['d']))

all_tiles = set()
for item in check:
    move_back(item[0], item[1], item[2])

print("Part 2: " + str(len(all_tiles)))
    




                




