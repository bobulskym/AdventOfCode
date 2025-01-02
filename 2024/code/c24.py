from collections import defaultdict
wires = {}
gates = []

with open('../data/d24.txt', 'r') as file:
    part_one = True

    for line in file:
        if line.strip() == '':
            part_one = False
        elif part_one:
            key, value = tuple(map(str.strip, line.split(':')))
            wires[key] = int(value)
        else:
            gate = tuple(map(str.strip, line.split(' ')))
            gate = (gate[0], gate[1], gate[2], gate[4])
            gates.append(gate)
            
            if gate[0] not in wires:
                wires[gate[0]] = -1
            if gate[2] not in wires:
                wires[gate[2]] = -1
            if gate[3] not in wires:
                wires[gate[3]] = -1


new_loop = True
while new_loop:
    for gate in gates:
        if wires[gate[0]] != -1 and wires[gate[2]] != -1 and wires[gate[3]] == -1:
            if gate[1] == 'AND':
                wires[gate[3]] = wires[gate[0]] and wires[gate[2]]
            if gate[1] == 'OR':
                wires[gate[3]] = wires[gate[0]] or wires[gate[2]]
            if gate[1] == 'XOR':
                wires[gate[3]] = wires[gate[0]] ^ wires[gate[2]]

    z_values = []
    is_filled = True
    for wire in wires:
        if wire[0] == 'z':
            z_values.append((wire, wires[wire]))
            if wires[wire] == -1:
                is_filled = False

    if is_filled:
        new_loop = False



# Part 1
z_values.sort(key = lambda t: t[0], reverse = True)

result = ''
for wire, value in z_values:
    result += str(value)
result = int(result, 2)

print("Part 1: " + str(result))


# Part 2
c = []
c.append(('z12', 'kwb'))
c.append(('z24', 'tgr'))
c.append(('z16', 'qkf'))
c.append(('jqn', 'cph'))

answer = []
for a, b in c:
    answer.append(a)
    answer.append(b)
answer.sort()
answer = ','.join(answer)

print("Part 2: " + str(answer))
