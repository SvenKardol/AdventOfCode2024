import functools

from aocd import get_data


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n\n")


@functools.cache
def pattern_possible(pattern):
    options = [c.strip() for c in data[0].split(",")]
    if len(pattern) == 0:
        return True

    for option in options:
        if pattern.startswith(option):
            if pattern_possible(pattern[len(option):]):
                return True

    return False


@functools.cache
def pattern_possible_options(pattern):
    options = [c.strip() for c in data[0].split(",")]
    possible_options = 0

    if len(pattern) == 0:
        return 1

    for option in options:
        if pattern.startswith(option):
            possible_options += pattern_possible_options(pattern[len(option):])

    return possible_options


def do_part1():
    possible = 0
    for pattern in data[1].split("\n"):
        if pattern_possible(pattern):
            possible += 1

    print(possible)


def do_part2():
    possible_options = 0
    for pattern in data[1].split("\n"):
        possible_options += pattern_possible_options(pattern)

    print(possible_options)


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
