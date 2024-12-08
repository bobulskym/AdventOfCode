with open('../data/d8.txt', 'r') as file:
    map = [[character for character in line.strip()] for line in file]

m = len(map)
n = len(map[0])

antennas = {}
antinodes_part_one = {}
antinodes_part_two = {}

for i in range(m):
    for j in range(n):
        if map[i][j] != '.':
            if map[i][j] not in antennas:
                antennas[map[i][j]] = [(i, j)]
            else:
                antennas[map[i][j]].append((i, j))

def calc_antinodes_part_one(ant_type, a, b, m, n):
    d = (b[0] - a[0], b[1] - a[1])
    antinode_one = (b[0] + d[0], b[1] + d[1])
    antinode_two = (a[0] - d[0], a[1] - d[1])
    
    if antinode_one[0] >= 0 and antinode_one[0] < m and antinode_one[1] >= 0 and antinode_one[1] < n:
        if ant_type not in antinodes_part_one:
            antinodes_part_one[ant_type] = [antinode_one]
        elif antinode_one not in antinodes_part_one[ant_type]:
            antinodes_part_one[ant_type].append(antinode_one)

    if antinode_two[0] >= 0 and antinode_two[0] < m and antinode_two[1] >= 0 and antinode_two[1] < n:
        if ant_type not in antinodes_part_one:
            antinodes_part_one[ant_type] = [antinode_two]
        elif antinode_two not in antinodes_part_one[ant_type]:
            antinodes_part_one[ant_type].append(antinode_two)

def calc_antinodes_part_two(ant_type, a, b, m, n):
    d = (b[0] - a[0], b[1] - a[1])
    
    antinode = b
    while antinode[0] >= 0 and antinode[0] < m and antinode[1] >= 0 and antinode[1] < n:
        if ant_type not in antinodes_part_two:
            antinodes_part_two[ant_type] = [antinode]
        elif antinode not in antinodes_part_two[ant_type]:
            antinodes_part_two[ant_type].append(antinode)
        
        antinode = (antinode[0] + d[0], antinode[1] + d[1])

    antinode = a
    while antinode[0] >= 0 and antinode[0] < m and antinode[1] >= 0 and antinode[1] < n:
        if ant_type not in antinodes_part_two:
            antinodes_part_two[ant_type] = [antinode]
        elif antinode not in antinodes_part_two[ant_type]:
            antinodes_part_two[ant_type].append(antinode)
        
        antinode = (antinode[0] - d[0], antinode[1] - d[1])


for antenna_type in antennas:
    for antenna_one in antennas[antenna_type]:
        for antenna_two in antennas[antenna_type]:
            if antenna_one != antenna_two:
                calc_antinodes_part_one(antenna_type, antenna_one, antenna_two, m, n)
                calc_antinodes_part_two(antenna_type, antenna_one, antenna_two, m, n)

all_antinodes_part_one = set()
for antenna_type in antinodes_part_one:
    for node in antinodes_part_one[antenna_type]:
        all_antinodes_part_one.add(node)

all_antinodes_part_two = set()
for antenna_type in antinodes_part_two:
    for node in antinodes_part_two[antenna_type]:
        all_antinodes_part_two.add(node)

print("Part 1: " + str(len(all_antinodes_part_one)))
print("Part 2: " + str(len(all_antinodes_part_two)))


