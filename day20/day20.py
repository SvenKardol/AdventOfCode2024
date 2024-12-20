import collections

from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")

def find_start():
    start = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "S":
                start = (x, y, 0)
    return start


def find_end():
    end = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "E":
                end = (x, y)
    return end

def within_grid(pos):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data)

def do_part1():
    start = find_start()
    end = find_end()
    queue = ([start])
    visited = []
    path = collections.defaultdict(int)
    while len(queue) > 0:
        cords = queue.pop()

        x,y, dist = cords
        path[(x, y)] = dist
        if (x,y) == end:
            break

        for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
            new = (x+dx, y+dy, dist + 1)
            if not within_grid(new):
                continue
            if (new[0], new[1]) in visited:
                continue
            if data[new[1]][new[0]] == "#":
                continue

            if new not in queue:
                queue.append(new)
            visited.append((new[0], new[1]))

    cheat = 0
    for cheat_step in path:
        for step in path:
            dx = abs(step[0] - cheat_step[0])
            dy = abs(step[1] - cheat_step[1])
            if dx + dy > 2:
                continue

            if path[cheat_step] - path[step] -dx -dy >= 100:
                cheat += 1

    print(cheat)


def do_part2():
    start = find_start()
    end = find_end()
    queue = ([start])
    visited = []
    path = collections.defaultdict(int)

    # why is this so slow?
    while len(queue) > 0:
        cords = queue.pop()

        x, y, dist = cords
        path[(x, y)] = dist
        if (x, y) == end:
            break

        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new = (x + dx, y + dy, dist + 1)
            if not within_grid(new):
                continue
            if (new[0], new[1]) in visited:
                continue
            if data[new[1]][new[0]] == "#":
                continue

            if new not in queue:
                queue.append(new)

            visited.append((new[0], new[1]))

    cheat = 0
    for cheat_step in path:
        for step in path:
            dx = abs(step[0] - cheat_step[0])
            dy = abs(step[1] - cheat_step[1])
            if dx + dy > 20:
                continue

            if path[cheat_step] - path[step] -dx -dy >= 100:
                cheat += 1

    print(cheat)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

