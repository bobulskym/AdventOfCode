with open('../data/d12.txt', 'r') as file:
    data = [[character for character in line.strip()] for line in file]

m = len(data)
n = len(data[0])

corner_check_map = [[item for item in line] for line in data]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

perimeter = []
area = []
corners = []

def exists(pos):
    return 0 <= pos[0] < m and 0 <= pos[1] < n

def neighbor(pos, type):
    if exists(pos):
        if corner_check_map[pos[0]][pos[1]] == type:
            return type
        else:
            return '.'
    else:
        return '.'

def check_garden(type, pos):
    garden.append(pos)
    data[pos[0]][pos[1]] = '.'
    area[-1] += 1

    UR = [
        [neighbor((pos[0] - 1, pos[1]), type), neighbor((pos[0] - 1, pos[1] + 1), type)],
        [neighbor((pos[0], pos[1]), type), neighbor((pos[0], pos[1] + 1), type)]
    ]

    DR = [
        [neighbor((pos[0], pos[1]), type), neighbor((pos[0], pos[1] + 1), type)],
        [neighbor((pos[0] + 1, pos[1]), type), neighbor((pos[0] + 1, pos[1] + 1), type)]
    ]

    DL = [
        [neighbor((pos[0], pos[1] - 1), type), neighbor((pos[0], pos[1]), type)],
        [neighbor((pos[0] + 1, pos[1] - 1), type), neighbor((pos[0] + 1, pos[1]), type)]
    ]

    UL = [
        [neighbor((pos[0] - 1, pos[1] - 1), type), neighbor((pos[0] - 1, pos[1]), type)],
        [neighbor((pos[0], pos[1] - 1), type), neighbor((pos[0], pos[1]), type)]
    ]
    
    if UR[0][0] == UR[1][1]:
        if UR[0][0] == '.' or (UR[0][0] != '.' and UR[0][1] == '.'):
            corners[-1] += 1

    if DR[1][0] == DR[0][1]:
        if DR[1][0] == '.' or (DR[1][0] != '.' and DR[1][1] == '.'):
            corners[-1] += 1

    if DL[0][0] == DL[1][1]:
        if DL[0][0] == '.' or (DL[0][0] != '.' and DL[1][0] == '.'):
            corners[-1] += 1

    if UL[1][0] == UL[0][1]:
        if UL[1][0] == '.' or (UL[1][0] != '.' and UL[0][0] == '.'):
            corners[-1] += 1

    for d in directions:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if exists(next_pos) and data[next_pos[0]][next_pos[1]] == type:
            check_garden(type, next_pos)
        elif next_pos not in garden:
            perimeter[-1] += 1


for i in range(m):
    for j in range(n):
        if data[i][j] != '.':
            type = data[i][j]
            garden = []
            area.append(0)
            perimeter.append(0)
            corners.append(0)
            check_garden(type, (i, j))

# Part 1
result = 0
for k in range(len(area)):
    result += area[k] * perimeter[k]

print("Part 1: " + str(result))


# Part 2
result = 0
for k in range(len(area)):
    result += area[k] * corners[k]

print("Part 2: " + str(result))
