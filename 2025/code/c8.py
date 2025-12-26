with open('../data/d8.txt', 'r') as file:
    data = [tuple(map(lambda x: int(x), line.strip().split(","))) for line in file]


nshortest = 1000


def dist(x, y):
    return sum((z1 - z2) ** 2 for z1, z2 in zip(x, y))


circuits = {item : 0 for item in data}


distances = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        distances.append([data[i], data[j], dist(data[i], data[j])])

distances.sort(key = lambda item: item[2])


name = 1
contin = True
i = 0

while i < len(distances) and contin:
    
    box1 = distances[i][0]
    box2 = distances[i][1]

    if circuits[box1] == 0 and circuits[box2] == 0:
        circuits[box1] = name
        circuits[box2] = name
        name += 1

    elif circuits[box1] == 0:
        circuits[box1] = circuits[box2]

    elif circuits[box2] == 0:
        circuits[box2] = circuits[box1]

    else:

        name1 = circuits[box1]
        name2 = circuits[box2]

        for key, value in circuits.items():
            if circuits[key] in [name1, name2]:
                circuits[key] = name
        
        name += 1


    hist = {}
    for key, value in circuits.items():
        
        if value not in hist:
            hist[value] = 1
        else:
            hist[value] += 1
    

    if len(hist.keys()) == 1:

        result2 = box1[0] * box2[0]
        contin = False


    if i == nshortest - 1:

        lengths = [value for key, value in hist.items() if key != 0]
        lengths.sort(reverse = True)

        result1 = lengths[0] * lengths[1] * lengths[2]
    

    i += 1


print("Part 1: " + str(result1))
print("Part 2: " + str(result2))