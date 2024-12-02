import numpy as np

safe = 0
safe_adj = 0

def is_safe(level):
    dif = np.diff(level)
    return (all(dif > 0) & all(dif <= 3)) | (all(dif < 0) & all(dif >= -3))

with open('../data/d2.txt', 'r') as file:

    for line in file:

        level = list(map(int, line.split()))
        
        if is_safe(level):
            safe += 1
        else:
            for i in range(len(level)):
                level_adj = np.delete(level, i)
                if is_safe(level_adj):
                    safe_adj += 1
                    break

print("Part 1: " + str(safe))
print("Part 2: " + str(safe + safe_adj))