from aocd import get_data
from collections import defaultdict


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def within_grid(pos):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data)


def find_antennas():
    antennas = defaultdict(list)
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch != ".":
                antennas[ch].append([x, y])
    return antennas


def do_part1():
    antennas = find_antennas()

    anti_nodes = []
    for values in antennas.values():
        for value in values:
            for value2 in values:
                if value == value2:
                    continue

                dx = value[0] - value2[0]
                dy = value[1] - value2[1]

                anti_nodes1 = [value[0] + dx, value[1] + dy]
                anti_nodes2 = [value2[0] - dx, value2[1] - dy]

                if anti_nodes1 not in anti_nodes and within_grid(anti_nodes1):
                    anti_nodes.append(anti_nodes1)
                if anti_nodes2 not in anti_nodes and within_grid(anti_nodes2):
                    anti_nodes.append(anti_nodes2)

    print(len(anti_nodes))


def do_part2():
    antennas = defaultdict(list)

    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch != ".":
                antennas[ch].append([x, y])

    anti_nodes = []
    for values in antennas.values():
        for value in values:
            for value2 in values:
                if value == value2:
                    continue

                dx = value[0] - value2[0]
                dy = value[1] - value2[1]

                for delta_x, delta_y in [(dx, dy), (-dx, -dy)]:
                    counter = 1
                    while True:
                        anti_node = [value[0] + delta_x * counter, value[1] + delta_y * counter]
                        if anti_node not in anti_nodes and within_grid(anti_node):
                            anti_nodes.append(anti_node)

                        if not within_grid(anti_node):
                            break
                        counter += 1

    print(len(anti_nodes))


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
