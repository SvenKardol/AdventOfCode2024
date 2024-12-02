from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()
    data = dataRaw.split("\n")

def do_part1():
    safe = 0

    for line in data:
        items = [int(x) for x in line.split()]

        res = all(i < j and j - i < 4 for i, j in zip(items, items[1:]))
        res2 = all(i > j and i - j < 4 for i, j in zip(items, items[1:]))

        if res or res2:
            safe += 1

    print (safe)

def do_part2():
    safe = 0

    for line in data:
        items = [int(x) for x in line.split()]

        for i in range(len(items)):
            items2 = items.copy()
            items2.pop(i)

            res = all(i < j and 0 < j - i < 4 for i, j in zip(items2, items2[1:]))
            res2 = all(i > j and 0 < i - j < 4 for i, j in zip(items2, items2[1:]))

            if res or res2:
                safe += 1
                break

    print(safe)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

