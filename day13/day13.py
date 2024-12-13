from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n\n")

def do_part1():
    total = 0
    for machine in data:
        lines = machine.split("\n")
        A = (int(lines[0].split("+")[1].split(",")[0]), int(lines[0].split("+")[2].split(" ")[0]))
        B = (int(lines[1].split("+")[1].split(",")[0]), int(lines[1].split("+")[2].split(" ")[0]))
        x = int(lines[2].split("=")[1].split(",")[0])
        y = int(lines[2].split("=")[2].split(" ")[0])

        # equation : x = a * Ax +  b * Bx
        # equation : y = a * Ay +  b * By
        # a = (x - b * Bx) / Ax
        # y = (x - b * Bx) / Ax * Ay + b * By
        # b = (y - x * Ay / Ax) / (By - Bx * Ay / Ax)
        b = (y - x * A[1] / A[0]) / (B[1] - B[0] * A[1] / A[0])
        a = (x - b * B[0]) / A[0]

        if not (0.0001 < a - int(a) < 0.999) and not (0.0001 < b - int(b) < 0.999):
            total += 3 * a + b
    print(total)

def do_part2():
    total = 0
    for machine in data:
        lines = machine.split("\n")
        A = (int(lines[0].split("+")[1].split(",")[0]), int(lines[0].split("+")[2].split(" ")[0]))
        B = (int(lines[1].split("+")[1].split(",")[0]), int(lines[1].split("+")[2].split(" ")[0]))
        x = int(lines[2].split("=")[1].split(",")[0]) + 10000000000000
        y = int(lines[2].split("=")[2].split(" ")[0]) + 10000000000000

        # equation : x = a * Ax +  b * Bx
        # equation : y = a * Ay +  b * By
        # a = (x - b * Bx) / Ax
        # y = (x - b * Bx) / Ax * Ay + b * By
        # b = (y - x * Ay / Ax) / (By - Bx * Ay / Ax)
        b = (y - x * A[1] / A[0]) / (B[1] - B[0] * A[1] / A[0])
        a = (x - b * B[0]) / A[0]

        if not (0.0001 < a - int(a) < 0.999) and not (0.0001 < b - int(b) < 0.999):
            total += 3 * a + b
    print(total)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

