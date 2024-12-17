with open('../data/d17.txt', 'r') as file:
    for k, line in enumerate(file):
        if k != 3:
            line = line.strip().split(':')[1]
            if k == 0:
                A = int(line)
            elif k == 1:
                B = int(line)
            elif k == 2:
                C = int(line)
            elif k == 4:
                instructions = tuple(map(int, line.split(',')))

n = len(instructions)

def combo_operand(operand):
    global A, B, C

    if operand == 4:
        output_operand = A
    elif operand == 5:
        output_operand = B
    elif operand == 6:
        output_operand = B
    else:
        output_operand = operand
    
    return output_operand

def compute(opcode, operand):
    global A, B, C, out
    
    if opcode == 0:
        operand = combo_operand(operand)
        binA = bin(A)
        if len(binA) - 3 < operand:
            A = 0
        elif operand == 0:
            pass
        else:
            A = int(binA[:-operand], 2)

    elif opcode == 1:
        B = B ^ operand

    elif opcode == 2:
        operand = combo_operand(operand)
        if operand > 7:
            B = int(bin(operand)[-3:], 2)
        else:
            B = operand

    elif opcode == 3:
        if A != 0:
            global i
            i = instructions[i + 1] - 2

    elif opcode == 4:
        B = B ^ C

    elif opcode == 5:
        operand = combo_operand(operand)
        if operand > 7:
            out.append(int(bin(operand)[-3:], 2))
        else:
            out.append(operand)

    elif opcode == 6:
        operand = combo_operand(operand)
        binA = bin(A)
        if len(binA) - 3 < operand:
            B = 0
        elif operand == 0:
            B = A
        else:
            B = int(binA[:-operand], 2)

    elif opcode == 7:
        operand = combo_operand(operand)
        binA = bin(A)
        if len(binA) - 3 < operand:
            C = 0
        elif operand == 0:
            C = A
        else:
            C = int(binA[:-operand], 2)

def find(start, diff, goal, nod):
    
    global i, out, A, B, C
    iter = start

    while True:

        A = iter
        B = 0
        C = 0

        out = []

        i = 0
        while True:
            compute(instructions[i], instructions[i + 1])
            i += 2
            if i > n - 2:
                break
        
        if goal == 'length':
            if len(out) >= nod:
                break
            else:
                iter += diff
        
        elif goal == 'digits':
            if instructions[-nod:] == tuple(out)[-nod:]:
                break
            else:
                iter += diff

    return iter

def find_exact(start, diff, goal, nod):
    iter = start
    
    while diff >= 1:
        iter = find(iter, diff, goal, nod)
        iter = iter - 2 * diff
        diff = int(diff / 10)

    iter += 2

    return iter


# Part 1
out = []

i = 0
while True:
    compute(instructions[i], instructions[i + 1])
    i += 2
    if i > n - 2:
        break

result = ''
for item in out:
    result += str(item) + ','
result = result[:-1]

print("Part 1: " + result)


# Part 2
iter = 0
iter = find_exact(iter, 1000000000000, 'length', 16)
iter = find_exact(iter, 1000000000, 'digits', 4)
iter = find_exact(iter, 1000000, 'digits', 8)
iter = find_exact(iter, 1000, 'digits', 12)
iter = find_exact(iter, 1, 'digits', 16)

print("Part 2: " + str(iter))


