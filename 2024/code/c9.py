with open('../data/d9.txt', 'r') as file:
    for line in file:
        data = line

# Part 1
blocks = []
for i, item in enumerate(data):
    item = int(item)
    if item != 0:
        for j in range(item):
            if i % 2 == 0:
                blocks.append(int(i / 2))
            else:
                blocks.append(-1)

for i, item in enumerate(blocks):
    if item == -1:
        new_item = blocks.pop()
        while new_item == -1:
            new_item = blocks.pop()
        blocks[i] = new_item

result = 0
for i, item in enumerate(blocks):
    result += i * item

print("Part 1: " + str(result))


# Part 2
blocks = []
for i, item in enumerate(data):
    item = int(item)
    if item != 0:
        for j in range(item):
            if i % 2 == 0:
                blocks.append(int(i / 2))
            else:
                blocks.append(-1)

blocks_grouped = [[blocks[0], 1, 0]]
for i in range(1, len(blocks)):
    if blocks[i] == blocks_grouped[-1][0]:
        blocks_grouped[-1][1] += 1
    else:
        blocks_grouped.append([blocks[i], 1, i])

hanging_blocks = [[item[0], item[1], item[2]] for item in blocks_grouped if item[0] != -1]
hanging_blocks.sort(reverse = True, key = lambda x: x[0])

for block in hanging_blocks:
    for i in range(block[2]):
        if blocks[i] == -1:
            check = blocks[i:(i + block[1])]
            if all([item == -1 for item in check]):
                blocks[i:(i + block[1])] = [block[0] for _ in range(block[1])]
                blocks[block[2]:(block[2] + block[1])] = [-1 for _ in range(block[1])]
                break

result = 0
for i, item in enumerate(blocks):
    if item != -1:
        result += i * item

print("Part 2: " + str(result))





