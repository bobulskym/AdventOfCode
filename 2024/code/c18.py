from collections import deque

with open('../data/d18.txt', 'r') as file:
    bytes = [tuple(map(int, line.strip().split(','))) for line in file]

def find_path(bytes, number_of_bytes, map_size):
    
    bytes = bytes[:number_of_bytes]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    paths = deque([[(0, 0)]])
    seen = set((0, 0))
    shortest_distance = 0
    process_finished = False

    while paths:

        path = paths.popleft()

        for dir in dirs:
            path_copy = path[:]
            new_pos = (path[-1][0] + dir[0], path[-1][1] + dir[1])

            if 0 <= new_pos[0] < map_size and 0 <= new_pos[1] < map_size and new_pos not in bytes and new_pos not in seen:
                path_copy.append(new_pos)
                seen.add(new_pos)
                paths.append(path_copy)
                if new_pos == (map_size - 1, map_size - 1):
                    shortest_distance = len(path_copy) - 1
                    process_finished = True
                    break

        if process_finished:
            break
    
    return shortest_distance


# Part 1
result = find_path(bytes, 1024, 71)
print("Part 1: " + str(result))


# Part 2
start = 0
end = len(bytes)

while start <= end:

    mid = int((start + end) / 2)

    if find_path(bytes, mid, 71) == 0:
        if find_path(bytes, mid - 1, 71) > 0:
            break
        else:
            end = mid
    else:
        start = mid

print("Part 2: " + str(bytes[mid - 1][0]) + ',' + str(bytes[mid - 1][1]))




