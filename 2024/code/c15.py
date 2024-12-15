with open('../data/d15.txt', 'r') as file:

    map_part_one = []
    map_part_two = []
    dirs = ''
    load_map = True

    for line in file:
        if line.strip() == '':
            load_map = False
            continue
        if load_map:
            map_part_one.append([item for item in line.strip()])
            map_part_two.append([])
            for item in line.strip():
                if item == '#':
                    map_part_two[-1] += ['#', '#']
                if item == 'O':
                    map_part_two[-1] += ['[', ']']
                if item == '.':
                    map_part_two[-1] += ['.', '.']
                if item == '@':
                    map_part_two[-1] += ['@', '.']
        else:
            dirs += line.strip()


def get_initial_position():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                pos = (i, j)
    return pos

def get_view(pos, dir):

    if dir == '>':
        dy, dx = (0, 1)
    if dir == '<':
        dy, dx = (0, -1)
    if dir == '^':
        dy, dx = (-1, 0)
    if dir == 'v':
        dy, dx = (1, 0)
    
    view = []
    item = map[pos[0]][pos[1]]
    while item != '#':
        view.append(item)
        pos = (pos[0] + dy, pos[1] + dx)
        item = map[pos[0]][pos[1]]

    return view

def place_view(pos, dir, view):

    if dir == '>':
        dy, dx = (0, 1)
    if dir == '<':
        dy, dx = (0, -1)
    if dir == '^':
        dy, dx = (-1, 0)
    if dir == 'v':
        dy, dx = (1, 0)
    
    for item in view:
        map[pos[0]][pos[1]] = item
        pos = (pos[0] + dy, pos[1] + dx)        

def count_empty(view):
    empty = 0
    for item in view:
        if item == '.':
            empty += 1
    return empty

def move_position(pos, dir):
    if dir == '>':
        pos = (pos[0], pos[1] + 1)
    if dir == '<':
        pos = (pos[0], pos[1] - 1)
    if dir == '^':
        pos = (pos[0] - 1, pos[1])
    if dir == 'v':
        pos = (pos[0] + 1, pos[1])
    return pos

def get_stones(pos, dir):
    if dir == '^':
        dy, dx = (-1, 0)
    if dir == 'v':
        dy, dx = (1, 0)
    y, x = pos
    x += dx
    y += dy
    
    if map[y][x] == '[':
        stones.add((y, x))
        stones.add((y, x + 1))
        stone = [(y, x), (y, x + 1)]
    elif map[y][x] == ']':
        stones.add((y, x))
        stones.add((y, x - 1))
        stone = [(y, x), (y, x - 1)]
    
    if map[y][x] in ['[', ']']:
        for s in stone:
            get_stones(s, dir)


def try_to_move(stone, dir):

    if dir == '^' and map_copy[stone[0] - 1][stone[1]] == '.':
        map_copy[stone[0] - 1][stone[1]] = map_copy[stone[0]][stone[1]]
        map_copy[stone[0]][stone[1]] = '.'
        return True
    
    if dir == 'v' and map_copy[stone[0] + 1][stone[1]] == '.':
        map_copy[stone[0] + 1][stone[1]] = map_copy[stone[0]][stone[1]]
        map_copy[stone[0]][stone[1]] = '.'
        return True
    
    return False


def move(pos, dir, part_two = False):
    if part_two == False or dir in ['>', '<']:
        view = get_view(pos, dir)
        empty = count_empty(view)

        if empty > 0:
            new_view = ['.', '@']
            rest = view[1:]
            skip = 0
            for i in range(len(rest)):
                if rest[i] == '.':
                    skip = i
                    break
            rest = rest[:skip] + rest[(skip + 1):]
            new_view += rest
            place_view(pos, dir, new_view)
            pos = move_position(pos, dir)
    
    else:
        if dir == '^' and map[pos[0] - 1][pos[1]] == '.':
            map[pos[0]][pos[1]] = '.'
            map[pos[0] - 1][pos[1]] = '@'
            pos = move_position(pos, dir)
        elif dir == 'v' and map[pos[0] + 1][pos[1]] == '.':
            map[pos[0]][pos[1]] = '.'
            map[pos[0] + 1][pos[1]] = '@'
            pos = move_position(pos, dir)
        else:
            global stones
            stones = set()
            get_stones(pos, dir)
            stones = list(stones)

            if len(stones) > 0:
                
                stones.sort(key = lambda p: p[0])
                if dir == 'v':
                    stones = stones[::-1]
                
                global map_copy
                map_copy = [line[:] for line in map]
                successful = []
                for stone in stones:
                    successful.append(try_to_move(stone, dir))
                
                if all(successful):
                    for i in range(len(map)):
                        for j in range(len(map[0])):
                            map[i][j] = map_copy[i][j]
                    if dir == '^':
                        map[pos[0]][pos[1]] = '.'
                        map[pos[0] - 1][pos[1]] = '@'
                        pos = move_position(pos, dir)
                    elif dir == 'v':
                        map[pos[0]][pos[1]] = '.'
                        map[pos[0] + 1][pos[1]] = '@'
                        pos = move_position(pos, dir)

    return pos


# Part 1
map = [line[:] for line in map_part_one]
pos = get_initial_position()

for dir in dirs:
    pos = move(pos, dir)

result_part_one = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'O':
            result_part_one += i * 100 + j

print("Part 1: " + str(result_part_one))


# Part 2
map = [line[:] for line in map_part_two]
map_copy = [line[:] for line in map]
stones = set()
pos = get_initial_position()

for dir in dirs:
    pos = move(pos, dir, part_two = True)

result_part_two = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '[':
            result_part_two += i * 100 + j

print("Part 2: " + str(result_part_two))
