import collections

from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")
    global size, num
    # size = 6
    # num = 12
    size = 70
    num = 1024


def do_part1():
    start = (0,0,0)
    end = (size,size)
    unsafe = get_unsafe_cords()

    queue = ([start])
    visited = []
    while len(queue) > 0:
        cords = queue[0]
        queue = queue[1:]
        x,y, dist = cords
        if (x,y) == end:
            print(dist)
            break

        for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
            new = (x+dx, y+dy, dist + 1)
            if not (0 <= new[0] <= size) or not (0 <= new[1] <= size):
                continue
            if (new[0], new[1]) in unsafe[:num] or (new[0], new[1]) in visited:
                continue

            if new not in queue:
                queue.append(new)
            visited.append((new[0], new[1]))


def get_unsafe_cords():
    unsafe = []
    for line in data:
        x, y = [int(a) for a in line.split(",")]
        unsafe.append((x, y))
    return unsafe


def do_part2():
    unsafe = get_unsafe_cords()

    lower = 0
    upper = len(unsafe)
    while upper != lower + 1:
        i = (upper + lower) // 2

        if will_reach_end(size, unsafe, i):
            lower = i + 1
        else:
            upper = i

    print(unsafe[lower])


def will_reach_end(size, unsafe, i):
    start = (0,0,0)
    end = (size,size)
    queue = ([start])
    visited = []
    while len(queue) > 0:
        cords = queue[0]
        queue = queue[1:]
        x, y, dist = cords
        if (x, y) == end:
            return True

        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new = (x + dx, y + dy, dist + 1)
            if not (0 <= new[0] <= size) or not (0 <= new[1] <= size):
                continue
            if (new[0], new[1]) in unsafe[:i] or (new[0], new[1]) in visited:
                continue

            if new not in queue:
                queue.append(new)
            visited.append((new[0], new[1]))
    return False


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

