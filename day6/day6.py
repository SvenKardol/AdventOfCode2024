import re

from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def determine_start():
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "^":
                return [x,y]
    return [-1, -1]


def do_part1():
    pos = determine_start()
    begin = pos
    dir = [0, -1]
    dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    begin_dir = [0, -1]

    # first step.
    pos = [pos[0] + dir[0], pos[1] + dir[1]]

    visited = [begin, pos]

    while pos != begin or dir != begin_dir:
        if not (0 <= pos[1]+dir[1] < len(data)) or not (0 <= pos[0]+dir[0] < len(data[0])):
            break

        if data[pos[1] + dir[1]][pos[0] + dir[0]] == "#":
            dir = dirs[(dirs.index(dir) + 1) % 4]

        if data[pos[1] + dir[1]][pos[0] + dir[0]] in ".^":
            pos = [pos[0] + dir[0], pos[1] + dir[1]]

        if pos not in visited:
            visited.append(pos)
    print(len(visited))



def do_part2():
    counter = 0
    for y in range(len(data)):
        print(y)
        for x in range(len(data[0])):
            if data[y][x] in "#^":
                continue


            pos = determine_start()
            begin = pos
            dir = [0, -1]
            dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
            begin_dir = [0, -1]

            pos = [pos[0] + dir[0], pos[1] + dir[1]]

            visited = [[pos, dir], [begin, begin_dir]]

            data[y] = data[y][:x] + "0" + data[y][x + 1:]
            while pos != begin or dir != begin_dir:
                if not (0 <= pos[1] + dir[1] < len(data)) or not (0 <= pos[0] + dir[0] < len(data[0])):
                    break

                if data[pos[1] + dir[1]][pos[0] + dir[0]] in "#0":
                    dir = dirs[(dirs.index(dir) + 1) % 4]
                    if [pos, dir] not in visited:
                        visited.append([pos, dir])
                    else:
                        counter += 1
                        break

                if data[pos[1] + dir[1]][pos[0] + dir[0]] in ".^":
                    pos = [pos[0] + dir[0], pos[1] + dir[1]]
                    if [pos, dir] in visited:
                        counter += 1
                        break

            data[y] = data[y][:x] + "." + data[y][x + 1:]
    print(counter)

if __name__ == '__main__':
    read_data()
    # do_part1()
    do_part2()

