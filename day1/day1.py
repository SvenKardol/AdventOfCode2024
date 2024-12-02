import math
from aocd import get_data

def read_data():
    global dataRaw, data
    # get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()
    data = dataRaw.split("\n")

def do_part1():
    # parse all data
    left = []
    right = []
    total = 0
    for line in data:

        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))
        left.sort()
        right.sort()

    for(x, y) in zip(left, right):
        total += math.fabs(x - y)
    print(total)

def do_part2():
    left = []
    right = []
    total = 0
    for line in data:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    for x  in left:
        y = right.count(x)

        total += y * x
    print(total)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

