import functools

from aocd import get_data


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    # with open("example2.txt", "r") as file:
    # with open("example3.txt", "r") as file:
    with open("example_large.txt", "r") as file:
        # with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def num_neighbors(i, j):
    count = 0

    options = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for option in options:
        if within_grid((i + option[0], j + option[1])) and data[i][j] == data[i + option[0]][j + option[1]]:
            count += 1
    return count


def within_grid(pos):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data)


def find_perimeter(area):
    perimeter = 0
    for (i, j) in area:
        perimeter += (4 - num_neighbors(i, j))
    return perimeter


def find_unique_perimeter(area):
    perimeter = 0
    for (i, j) in area:
        # outside corners
        perimeter += (i - 1, j) not in area and (i, j - 1) not in area  # top left
        perimeter += (i + 1, j) not in area and (i, j - 1) not in area  # bottom left
        perimeter += (i - 1, j) not in area and (i, j + 1) not in area  # top right
        perimeter += (i + 1, j) not in area and (i, j + 1) not in area  # bottom right

        # inside corners
        perimeter += (i - 1, j) in area and (i, j - 1) in area and (i - 1, j - 1) not in area  # top left gap
        perimeter += (i + 1, j) in area and (i, j - 1) in area and (i + 1, j - 1) not in area  # bottom left gap
        perimeter += (i - 1, j) in area and (i, j + 1) in area and (i - 1, j + 1) not in area  # top right gap
        perimeter += (i + 1, j) in area and (i, j + 1) in area and (i + 1, j + 1) not in area  # bottom right gap
    return perimeter


@functools.cache
def get_areas():
    areas = []
    options = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i, line in enumerate(data):
        for j, ch in enumerate(data[i]):
            if any((i, j) in area for area in areas):
                area = next(area for area in areas if (i, j) in area)
                for option in options:
                    if (i + option[0], j + option[1]) in area:
                        continue
                    if any((i + option[0], j + option[1]) in a and data[i][j] == data[i + option[0]][j + option[1]] for
                           a in areas):
                        actual_area = next(a for a in areas if (i + option[0], j + option[1]) in a)
                        for p in area:
                            actual_area.append(p)
                        areas.pop(areas.index(area))
                    if within_grid((i + option[0], j + option[1])) and data[i][j] == data[i + option[0]][j + option[1]]:
                        area.append((i + option[0], j + option[1]))
            else:
                area = [(i, j)]
                actual_area = []
                for option in options:
                    if any((i + option[0], j + option[1]) in a and data[i][j] == data[i + option[0]][j + option[1]] for
                           a in areas):
                        actual_area = next(a for a in areas if (i + option[0], j + option[1]) in a)
                        for p in area:
                            actual_area.append(p)
                        continue
                    if any((i + option[0], j + option[1]) in a for a in areas):
                        continue
                    if within_grid((i + option[0], j + option[1])) and data[i][j] == data[i + option[0]][j + option[1]]:
                        if len(actual_area) > 0:
                            actual_area.append((i + option[0], j + option[1]))
                        else:
                            area.append((i + option[0], j + option[1]))

                if len(actual_area) == 0:
                    areas.append(area)
    print(areas)
    return areas


def do_part1():
    areas = get_areas()

    total = 0
    for area in areas:
        perimeter = find_perimeter(area)
        total += len(area) * perimeter

    print(total)


def do_part2():
    areas = get_areas()
    total = 0
    for area in areas:
        perimeter = find_unique_perimeter(area)
        total += perimeter * len(area)

    print(total)


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
