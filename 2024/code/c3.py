import re

text = ""
with open('../data/d3.txt', 'r') as file:
    for line in file:
        text += "-" + line

# Part 1
pattern = "mul\((\d+),(\d+)\)"
muls = re.findall(pattern, text)

result = 0
for mul in muls:
    x = int(mul[0])
    y = int(mul[1])
    result += x * y

print("Part 1: " + str(result))

# Part 2
pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
sub_pattern = "mul\((\d+),(\d+)\)"
muls = re.findall(pattern, text)

do = True
result = 0
for mul in muls:
    if mul == "do()":
        do = True
    elif mul == "don't()":
        do = False
    else:
        if do:
            nums = re.findall(sub_pattern, mul)[0]
            x = int(nums[0])
            y = int(nums[1])
            result += x * y

print("Part 2: " + str(result))




