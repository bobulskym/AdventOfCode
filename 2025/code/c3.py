with open('../data/d3.txt', 'r') as file:
    data = [[int(digit) for digit in line.strip()] for line in file]


def find(seq, length, num = 0):

    global result

    if length == 0:

        result += num

    else:

        n = len(seq)
        max_val = max(seq[:(n + 1 - length)])
        max_index = seq.index(max_val)

        num = num * 10 + max_val
        seq = seq[(max_index + 1):]
        length += -1

        find(seq, length, num)


result = 0
for seq in data:
    find(seq, 2)

print("Part 1: " + str(result))


result = 0
for seq in data:
    find(seq, 12)

print("Part 2: " + str(result))
