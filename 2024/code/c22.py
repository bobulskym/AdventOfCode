from collections import deque, defaultdict

def generate_number(num):

    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216

    return num


last_four_dict = defaultdict(int)
def generate_nth(num, n):

    last_four = deque()
    last_four_history = set()

    k = 0
    while k < n:
        new_num = generate_number(num)
        diff = int(str(new_num)[-1]) - int(str(num)[-1])
        last_four.append(diff)
        if k > 3:
            last_four.popleft()

            if tuple(last_four) not in last_four_history:
                last_four_dict[tuple(last_four)] += int(str(new_num)[-1])

            last_four_history.add(tuple(last_four))
        
        num = new_num
        k += 1

    return num


# Part 1
result = 0
with open('../data/d22.txt', 'r') as file:
    for line in file:
        num = int(line.strip())
        result += generate_nth(num, 2000)

print("Part 1: " + str(result))


# Part 2
print("Part 2: " + str(max(last_four_dict.values())))

