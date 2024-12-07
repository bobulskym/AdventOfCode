def new_operator(a, b):
    return int(str(a) + str(b))

def combine(vector, value, part_two = False): 
    
    mult = [item * value for item in vector]
    
    add = [item + value for item in vector]
    
    if part_two:
        conc = [new_operator(item, value) for item in vector]
    else:
        conc = []

    return mult + add + conc


ans1 = 0
ans2 = 0
with open('../data/d7.txt', 'r') as file:

    for line in file:

        eq = [eq.strip() for eq in line.split(':')]
        eq = [int(eq[0]), [int(rs) for rs in eq[1].split()]]
        
        result = eq[0]
        params = eq[1]

        v1 = [params[0]]
        v2 = [params[0]]

        for i in range(1, len(params)):
            v1 = combine(v1, params[i])
            v2 = combine(v2, params[i], part_two = True)

        if any([option == result for option in v1]):
            ans1 += result

        if any([option == result for option in v2]):
            ans2 += result

print("Part 1: " + str(ans1))
print("Part 2: " + str(ans2))





