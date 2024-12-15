robots = {}
id = 0
m = 101
n = 103

with open('../data/d14.txt', 'r') as file:

        for line in file:
            id += 1
            robot = [robot.split('=')[1] for robot in line.split()]
            robots[id] = {}
            robots[id]['pos'] = (int(robot[0].split(',')[0]), int(robot[0].split(',')[1]))
            robots[id]['dir'] = (int(robot[1].split(',')[0]), int(robot[1].split(',')[1]))

tree_template = [[0 for c in range(m)] for r in range(n)]
for i in range(n):
    for j in range(m):
        if i > int(n/3) and j > int(m/3) and j < int(m/3 * 2):
            tree_template[i][j] = 1


min_distance = [m * n]
result_part_two = [0]

def find_tree(robots, k):
    map = [[0 for c in range(m)] for r in range(n)]
    for id in robots:
        pos = robots[id]['pos']
        map[pos[1]][pos[0]] = 1

    distance = 0
    for i in range(n):
        for j in range(m):
            distance += abs(map[i][j] - tree_template[i][j])

    if distance < min_distance[0]:
        min_distance[0] = distance
        result_part_two[0] = k
        global final_map
        final_map = [line[:] for line in map]


for k in range(101 * 103):

    for id, robot in robots.items():
        pos = robots[id]['pos']
        dir = robots[id]['dir']
        robots[id]['pos'] = ((pos[0] + dir[0]) % m, (pos[1] + dir[1]) % n)

    find_tree(robots, k + 1)

    if k + 1 == 100:
        quadrants = [0, 0, 0, 0]
        mid_m = int(m / 2)
        mid_n = int(n / 2)
        for id, robot in robots.items():
            if (robot['pos'][0] < mid_m and robot['pos'][1] < mid_n):
                quadrants[0] += 1
            elif (robot['pos'][0] > mid_m and robot['pos'][1] < mid_n):
                quadrants[1] += 1
            elif (robot['pos'][0] < mid_m and robot['pos'][1] > mid_n):
                quadrants[2] += 1
            elif (robot['pos'][0] > mid_m and robot['pos'][1] > mid_n):
                quadrants[3] += 1

        result_part_one = 1
        for q in quadrants:
            result_part_one *= q


for line in final_map:
    str_line = ''
    for item in line:
        if item != 0:
            str_line += str(item)
        else:
            str_line += '.'
    print(str_line)

print("Part 1: " + str(result_part_one))
print("Part 2: " + str(result_part_two[0]))

    



            
