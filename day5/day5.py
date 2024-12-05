from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n\n")


def do_part1():
    instructions = [[int(x), int(y)] for i in data[0].split("\n") for x, y in [i.split("|")]]
    lines = data[1].split("\n")

    middle_sum = 0

    for line in lines:
        pages = [int(x) for x in line.split(",")]
        pages_are_correctly_ordered = check_instructions(instructions, pages)

        if pages_are_correctly_ordered:
            middle = int((len(pages) - 1) / 2)
            middle_sum += pages[middle]

    print(middle_sum)


def check_instructions(instructions, pages):
    for instruction in instructions:
        first, second = instruction[0], instruction[1]
        if first in pages and second in pages and pages.index(first) > pages.index(second):
            return False
    return True


def do_part2():
    instructions = [[int(x), int(y)] for i in data[0].split("\n") for x, y in [i.split("|")]]
    lines = data[1].split("\n")

    middle_sum = 0

    for line in lines:
        pages = [int(x) for x in line.split(",")]
        pages_are_correctly_ordered = False
        loop_count = 0
        while not pages_are_correctly_ordered:
            pages_are_correctly_ordered = check_instructions_swap_pages(instructions, pages)
            loop_count += 1

        if loop_count > 1:
            middle = int((len(pages)-1)/2)
            middle_sum += pages[middle]

    print(middle_sum)


def check_instructions_swap_pages(instructions, pages):
    for instruction in instructions:
        first, second = instruction[0], instruction[1]
        if first in pages and second in pages and pages.index(first) > pages.index(second):
            pages.pop(pages.index(second))
            pages.insert(pages.index(first) + 1, second)
            return False
    return True


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

