from itertools import product

depth_part_one = 2
depth_part_two = 25

# Too lazy to process the first keyboard
inputs = ['^^<<A>A^>AvvvA', '^^A<<^AvvA>>vA', '<^^^A<vA>>AvvA', '<^A^^AvAvv>A', '<A^^^Avv>AvA']
coeffs = [459, 671, 846, 285, 83]


def process(start, end, v):
    if start == 'A':
        if end == '<':
            return ['v<<A', '<v<A'][v[0]]
        if end == 'v':
            return ['<vA', 'v<A'][v[1]]
        if end == '>':
            return 'vA'
        if end == '^':
            return '<A'
        if end == 'A':
            return 'A'
    if start == '^':
        if end == '<':
            return 'v<A'
        if end == 'v':
            return 'vA'
        if end == '>':
            return ['v>A', '>vA'][v[2]]
        if end == '^':
            return 'A'
        if end == 'A':
            return '>A'
    if start == '>':
        if end == '<':
            return '<<A'
        if end == 'v':
            return '<A'
        if end == '>':
            return 'A'
        if end == '^':
            return ['<^A', '^<A'][v[3]]
        if end == 'A':
            return '^A'
    if start == 'v':
        if end == '<':
            return '<A'
        if end == 'v':
            return 'A'
        if end == '>':
            return '>A'
        if end == '^':
            return '^A'
        if end == 'A':
            return ['>^A', '^>A'][v[4]]
    if start == '<':
        if end == '<':
            return 'A'
        if end == 'v':
            return '>A'
        if end == '>':
            return '>>A'
        if end == '^':
            return '>^A'
        if end == 'A':
            return ['>>^A', '>^>A'][v[5]]
        

memory = {depth_part_one: {}, depth_part_two: {}}
def robot(start, end, depth, depth_max, v = (0, 0, 0, 0, 0, 0)):

    if depth == depth_max + 1:
        return 1
    
    result = 0
    next_keyboard = process(start, end, v)

    new_depth = depth + 1
    new_start = 'A'
    for new_end in next_keyboard:

        if (new_start, new_end, new_depth) not in memory[depth_max]:
            memory[depth_max][(new_start, new_end, new_depth)] = robot(new_start, new_end, new_depth, depth_max, v)
            for comb in product((0, 1), repeat = 6):
                temp = robot(new_start, new_end, new_depth, depth_max, comb)
                if temp < memory[depth_max][(new_start, new_end, new_depth)]:
                    memory[depth_max][(new_start, new_end, new_depth)] = temp
        
        result += memory[depth_max][(new_start, new_end, new_depth)]

        new_start = new_end

    return result


result_part_one = 0
result_part_two = 0
for i, input in enumerate(inputs):
    start = 'A'
    for end in input:
        
        min_result_part_one = coeffs[i] * robot(start, end, 1, depth_part_one)
        min_result_part_two = coeffs[i] * robot(start, end, 1, depth_part_two)

        for comb in product((0, 1), repeat = 6):
            
            temp_part_one = coeffs[i] * robot(start, end, 1, depth_part_one, comb)
            temp_part_two = coeffs[i] * robot(start, end, 1, depth_part_two, comb)

            if temp_part_one < min_result_part_one:
                min_result_part_one = temp_part_one
            if temp_part_two < min_result_part_two:
                min_result_part_two = temp_part_two
        
        result_part_one += min_result_part_one
        result_part_two += min_result_part_two

        start = end


print("Part 1: " + str(result_part_one))
print("Part 2: " + str(result_part_two))


