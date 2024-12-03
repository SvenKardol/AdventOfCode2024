from aocd import get_data
import re

def read_data():
    global dataRaw, data
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.replace("\n", "")

def do_part1(input):
    total = 0
    t = re.findall("mul\([0-9]+,[0-9]+\)", input)

    for item in t:
        numbers = re.findall(r'\d+', item)
        total += int(numbers[0]) * int(numbers[1])

    print(total)

def do_part2():
    input_part2 = re.sub(r"don't\(\).*", "", re.sub(r"don't\(\).+?do\(\)", "", data))
    do_part1(input_part2)


if __name__ == '__main__':
    read_data()
    do_part1(data)
    do_part2()

