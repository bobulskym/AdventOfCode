with open('../data/d19.txt', 'r') as file:
    designs = [line.strip() for line in file]
    patterns = list(map(str.strip, designs[0].split(',')))
    designs = designs[2:]

patterns_grouped = {}
for pattern in patterns:
    if pattern[0] not in patterns_grouped:
        patterns_grouped[pattern[0]] = [pattern]
    else:
        patterns_grouped[pattern[0]].append(pattern)

memory = {}

def find_combinations(design):
    if design not in memory:
        
        first_letter = design[0]
        count = 0

        if first_letter in patterns_grouped:
            for pattern in patterns_grouped[first_letter]:
                len_pattern = len(pattern)
                len_design = len(design)
                if len_pattern < len_design:
                    if design[:len_pattern] == pattern:
                        new_design = design[len_pattern:]
                        count += find_combinations(new_design)
                elif len_pattern == len_design:
                    if design == pattern:
                        count += 1
        
        memory[design] = count
        return count
    else:
        return memory[design]


results = []
for design in designs:
    result = find_combinations(design)
    results.append(result)

print("Part 1: " + str(sum(map(lambda x: x != 0, results))))
print("Part 2: " + str(sum(results)))