with open('../data/d5.txt', 'r') as file:
    data = [line.strip() for line in file]

fresh = []
candidates = []

for item in data:
    if "-" in item:
        item = item.split("-")
        item = map(int, item)
        fresh.append(tuple(item))
    elif item != "":
        candidates.append(int(item))


def check_candidate(candidate):
    
    isfresh = False

    for interval in fresh:
        if candidate >= interval[0] and candidate <= interval[1]:
            isfresh = True
            break

    return isfresh


# Part 1
result = 0

for candidate in candidates:
    result += check_candidate(candidate)


print("Part 1: " + str(result))


# Part 2
fresh.sort(key = lambda tup: tup[0])

start = 0
end = -1
result = 0

for interaval in fresh:

    istart = interaval[0]
    iend = interaval[1]

    if istart > end:
        result += end - start + 1
        start = istart
        end = iend
    elif iend > end:
        end = iend

result += end - start + 1


print("Part 2: " + str(result))