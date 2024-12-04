from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")

def do_part1():
    xmas = 0
    for l, line in enumerate(data):
        # max to still go down
        mgd = len(data) - 3

        for i, ch in enumerate(line):
            if ch != "X":
                continue

            # max to still go right
            mgr = len(line) - 3

            # horizontal
            if i < mgr and line[i:i + 4] == "XMAS":
                xmas += 1
            if i > 2 and line[i - 3:i + 1] == "SAMX":
                xmas += 1

            # vertical
            if l > 2 and data[l - 3][i] == "S" and data[l - 2][i] == "A" and data[l - 1][i] == "M":
                xmas += 1
            if l < mgd and data[l + 1][i] == "M" and data[l + 2][i] == "A" and data[l + 3][i] == "S":
                xmas += 1

            # diagonal going up
            if l > 2:
                if i < mgr and data[l - 3][i + 3] == "S" and data[l - 2][i + 2] == "A" and data[l - 1][i + 1] == "M":
                    xmas += 1
                if i > 2 and data[l - 3][i - 3] == "S" and data[l - 2][i - 2] == "A" and data[l - 1][i - 1] == "M":
                    xmas += 1
            # diagonal going down
            if l < mgd:
                if i < mgr and data[l + 1][i + 1] == "M" and data[l + 2][i + 2] == "A" and data[l + 3][i + 3] == "S":
                    xmas += 1
                if i > 2 and data[l + 1][i - 1] == "M" and data[l + 2][i - 2] == "A" and data[l + 3][i - 3] == "S":
                    xmas += 1
    print(xmas)

def do_part2():
    xmas = 0
    ms = {"M", "S"}
    for l, line in enumerate(data):
        if l == 0 or l == len(data) - 1:
            continue

        for i, ch in enumerate(line):
            if ch != "A" or i == 0 or i == len(line) - 1:
                continue

            top_left = data[l - 1][i - 1]
            top_right = data[l - 1][i + 1]
            bottom_left = data[l + 1][i - 1]
            bottom_right = data[l + 1][i + 1]

            if top_left in ms and bottom_right in ms and bottom_right != top_left and \
               top_right in ms and bottom_left in ms and bottom_left != top_right:
                xmas += 1
    print(xmas)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

