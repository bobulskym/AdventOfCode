with open('../data/d10.txt', 'r') as file:
    data = [[int(character) for character in line.strip()] for line in file]

m = len(data)
n = len(data[0])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
trailheads_part_one = set()
trailheads_part_two = []
count_part_one = 0
count_part_two = 0

def find_paths(pos, step = 0):
    for dir in directions:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos[0] >= 0 and new_pos[0] < m and new_pos[1] >= 0 and new_pos[1] < n:
            if data[new_pos[0]][new_pos[1]] == step + 1:
                if step + 1 == 9:
                    trailheads_part_one.add(new_pos)
                    trailheads_part_two.append(new_pos)
                else:
                    find_paths(new_pos, step + 1)

for i in range(m):
    for j in range(n):
        if data[i][j] == 0:
            find_paths((i, j))
            count_part_one += len(trailheads_part_one)
            count_part_two += len(trailheads_part_two)
            trailheads_part_one = set()
            trailheads_part_two = []

print("Part 1: " + str(count_part_one))
print("Part 2: " + str(count_part_two))