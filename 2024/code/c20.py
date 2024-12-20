from collections import deque

with open('../data/d20.txt', 'r') as file:
    maze = [[item for item in line.strip()] for line in file]

m = len(maze)
n = len(maze[0])

def find_position(item):
    for i in range(m):
        for j in range(n):
            if maze[i][j] == item:
                maze[i][j] = '.'
                return (i, j)
    return (-1, -1)


def find_path(start, end):
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    paths = deque([[start]])
    seen = set(start)
    shortest_distance = 0
    process_finished = False

    while paths:

        path = paths.popleft()

        for dir in dirs:
            path_copy = path[:]
            new_pos = (path[-1][0] + dir[0], path[-1][1] + dir[1])

            if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n and maze[new_pos[0]][new_pos[1]] != '#' and new_pos not in seen:
                path_copy.append(new_pos)
                seen.add(new_pos)
                paths.append(path_copy)
                if new_pos == end:
                    shortest_distance = len(path_copy) - 1
                    process_finished = True
                    break

        if process_finished:
            break
    
    return {'distance' : shortest_distance, 'path' : paths[-1]}


def create_memory(path):
    
    memory = {}
    path = path[::-1]

    for k, pos in enumerate(path):
        memory[pos] = k

    return memory


def cheat(jump):

    count = 0

    for current_steps, pos in enumerate(path):

        for i in range(-jump, jump + 1):
            for j in range(-jump + abs(i), jump - abs(i) + 1):
                
                new_pos = (pos[0] + i, pos[1] + j)
                
                if new_pos in memory:
                    if current_steps + abs(i) + abs(j) + memory[new_pos] <= distance - 100:
                        count += 1
                        # print(round((current_steps + 1)/distance * 100, 2), '% ,', count)

    return count


start = find_position('S')
end = find_position('E')
path_info = find_path(start, end)
distance = path_info['distance']
path = path_info['path']
memory = create_memory(path)


# Part 1
print("Part 1: " + str(cheat(jump = 2)))

# Part 2
print("Part 2: " + str(cheat(jump = 20)))







