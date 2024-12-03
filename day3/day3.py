from aocd import get_data
import re

def read_data():
    global dataRaw, data
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.replace("\n", "")

def do_part1():
    total = 0
    t = re.findall("mul\([0-9]+,[0-9]+\)", data)

    for item in t:
        total +=  int(item.replace("mul(", "").replace(")", "").split(",")[0]) * int(item.replace("mul(", "").replace(")", "").split(",")[1])

    print(total)

def do_part2():
    total = 0
    stripped_line=re.sub(r"don't\(\).+?do\(\)""", "", data)
    t = re.findall("mul\([0-9]+,[0-9]+\)", stripped_line)

    for item in t:
        total += int(item.replace("mul(", "").replace(")", "").split(",")[0]) * int(
            item.replace("mul(", "").replace(")", "").split(",")[1])

    print(total)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

