data = []

with open('../data/d5.txt', 'r') as file:
    for line in file:
        data.append(line.strip())

delim = data.index('')

rules = data[:delim]
rules = [list(map(int, rule.split("|"))) for rule in rules]
rules_dict = {}
for rule in rules:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = [rule[1]]
    else:
        rules_dict[rule[0]].append(rule[1])

updates = data[delim + 1:]
updates = [list(map(int, update.split(","))) for update in updates]

def order_update(update, rules):

    for _ in range(len(update)):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                first = update.index(rule[0])
                second = update.index(rule[1])
                if first > second:
                    update[first] = rule[1]
                    update[second] = rule[0]

    return update


result_part_1 = 0
result_part_2 = 0
for update in updates:

    is_update_ok = True
    for i in range(1, len(update)):

        page = update[i]

        if page in rules_dict:
            if any([check in rules_dict.get(page) for check in update[:i]]):
                is_update_ok = False
                break

    n = len(update)
    mid = int((n - 1)/2)

    if is_update_ok:
        result_part_1 += update[mid]
    else:
        update_ordered = order_update(update, rules)
        result_part_2 += update_ordered[mid]


print("Part 1: " + str(result_part_1))
print("Part 2: " + str(result_part_2))
