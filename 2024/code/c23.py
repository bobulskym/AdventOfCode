from collections import defaultdict

data = defaultdict(list)
groups = []
pcs = set()

with open('../data/d23.txt', 'r') as file:
    for line in file:
        pc1, pc2 = map(str.strip, line.split('-'))

        groups.append((pc1, pc2))
        pcs.add(pc1)
        pcs.add(pc2)

        if pc2 not in data[pc1]:
            data[pc1].append(pc2)
        if pc1 not in data[pc2]:
            data[pc2].append(pc1)


# Part 1
result = set()
for key, value in data.items():
    for i in range(len(value) - 1):
        for j in range(i + 1, len(value)):
            pc1 = data[key][i]
            pc2 = data[key][j]
            if pc2 in data[pc1]:
                three = [key, pc1, pc2]
                three.sort()
                if any(map(lambda item: item[0] == 't', three)):
                    result.add(tuple(three))

print("Part 1: " + str(len(result)))


# Part 2
for i in range(len(groups)):
    group = list(groups[i])
    for pc in pcs:
        if pc not in group:
            if all(map(lambda p: p in data[pc], group)):
                group.append(pc)
    group.sort()
    groups[i] = tuple(group)


groups.sort(key = lambda g: len(g), reverse = True)
longest = groups[0]
result = ','.join(longest)

print("Part 2: " + result)





