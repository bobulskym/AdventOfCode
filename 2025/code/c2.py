with open('../data/d2.txt', 'r') as file:
    data = [[interval.split("-") for interval in line.split(",")] for line in file]
    data = data[0]


def check1(num):
    
    invalid = True
    num = str(num)
    n = len(num)
    
    if n % 2 != 0:
        return(False)
    
    for i in range(int(n/2)):
        if num[i] != num[i + int(n/2)]:
            invalid = False

    return(invalid)

def check2(num):
    
    invalid = False
    num = str(num)
    n = len(num)
    
    for i in range(int(n/2)):
        part = num[:(i + 1)]
        times = int(len(num) / len(part))
        new_num = part * times
        if num == new_num:
            invalid = True

    return(invalid)


result1 = 0
result2 = 0

for interval in data:
    
    start = int(interval[0])
    end = int(interval[1])
    
    while start <= end:     
        if check1(start):
            result1 += start
        if check2(start):
            result2 += start
        start += 1


print("Part 1: " + str(result1))
print("Part 2: " + str(result2))



