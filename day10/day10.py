from aocd import get_data
from collections import Counter


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    # with open("example2.txt", "r") as file:
    # with open("example_large.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def within_grid(pos):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data)


def do_part1():
    trail_score = 0

    options = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for l, line in enumerate(data):
        for c, char in enumerate(line):
            if char != "0":
                continue

            trail_ends = []
            queue = [[c, l, 0]]
            while len(queue) > 0:
                item = queue.pop()
                for option in options:
                    new_item = [item[0] + option[0], item[1] + option[1]]
                    if (within_grid(new_item) and data[new_item[1]][new_item[0]] != "." and
                            item[2] + 1 == int(data[new_item[1]][new_item[0]])):
                        if int(data[new_item[1]][new_item[0]]) == 9 and new_item not in trail_ends:
                            trail_score += 1
                            trail_ends.append(new_item)
                        else:
                            queue.append([new_item[0], new_item[1], item[2] + 1])

    print(trail_score)


def do_part2():
    trail_score = 0

    options = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for l, line in enumerate(data):
        for c, char in enumerate(line):
            if char != "0":
                continue

            queue = [[c, l, 0]]
            while len(queue) > 0:
                item = queue.pop()
                for option in options:
                    new_item = [item[0] + option[0], item[1] + option[1]]
                    if (within_grid(new_item) and data[new_item[1]][new_item[0]] != "." and
                            item[2] + 1 == int(data[new_item[1]][new_item[0]])):
                        if int(data[new_item[1]][new_item[0]]) == 9:
                            trail_score += 1
                        queue.append([new_item[0], new_item[1], item[2] + 1])

    print(trail_score)


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
