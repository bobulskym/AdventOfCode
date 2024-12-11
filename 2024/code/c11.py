with open('../data/d11.txt', 'r') as file:
    for line in file:
        stones = list(map(int, line.split()))


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stone = [1]
        else:
            stone_string = str(stone)
            if len(stone_string) % 2 == 0:
                new_stone = [int(stone_string[:int(len(stone_string)/2)]), int(stone_string[int(len(stone_string)/2):])]
            else:
                new_stone = [stone * 2024]
            
        new_stones += new_stone

    return new_stones
    

memory = {}
def generate_memory(stone):
    stones = [stone]
    for _ in range(25):
        stones = blink(stones)

    stones.sort()
    counts = {}
    for s in stones:
        if s not in counts:
            counts[s] = 1
        else:
            counts[s] += 1
    
    memory[stone] = counts


def investigate(num, step = 1, part_one = True):
    if num not in memory:
        generate_memory(num)

    obj = memory[num]

    if step == 3 or part_one:
        return sum(obj.values())
    else:
        partial = 0
        for key, value in obj.items():
            partial += value * investigate(key, step + 1, part_one)
        return partial
    

# Part 1
result = 0
for stone in stones:
    result += investigate(stone)

print("Part 1: " + str(result))


# Part 2
result = 0
for stone in stones:
    result += investigate(stone, part_one = False)

print("Part 2: " + str(result))