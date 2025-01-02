keys = []
locks = []

with open('../data/d25.txt', 'r') as file:

    for i, line in enumerate(file):
        k = i % 8
        
        if k == 0:
            item_list = []
        
        if k != 7:
            item_list.append(line.strip())

        if k == 6:
            item = [0, 0, 0, 0, 0]

            for i in range(len(item_list)):
                for j in range(len(item_list[0])):
                    if item_list[i][j] == '#':
                        item[j] += 1

            if all(map(lambda l: l == '#', item_list[0])):
                locks.append(tuple(item))
            else:
                keys.append(tuple(item))


matching = 0

for key in keys:
    for lock in locks:
        if all(map(lambda t: t[0] + t[1] <= 7, zip(key, lock))):
            matching += 1

print("Part 1: " + str(matching))
