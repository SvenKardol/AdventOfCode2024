from aocd import get_data


def read_data():
    global dataRaw, data, width, height
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")

    width = 101
    height = 103
    # example grid
    # width = 11
    # height = 7


def update_robot(robot):
    pos = robot[0]
    vel = robot[1]

    pos[0] += vel[0]
    pos[1] += vel[1]

    pos[0] = pos[0] % width
    pos[1] = pos[1] % height


def do_part1():
    robots = []
    for line in data:
        pos = [int(x) for x in line.split("=")[1].split(" ")[0].strip().split(",")]
        vel = [int(x) for x in line.split(" ")[1].strip().split("=")[1].split(",")]
        robots.append([pos, vel])

    for i in range(100):
        for robot in robots:
            update_robot(robot)

    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot[0][0] < int(width / 2) and robot[0][1] < int(height / 2):
            quadrants[0] += 1
        elif robot[0][0] >= int(width / 2) + 1 and robot[0][1] < int(height / 2):
            quadrants[1] += 1
        elif robot[0][0] < int(width / 2) and robot[0][1] >= int(height / 2) + 1:
            quadrants[2] += 1
        elif robot[0][0] >= int(width / 2) + 1 and robot[0][1] >= int(height / 2) + 1:
            quadrants[3] += 1

    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


def do_part2():
    robots = []
    for line in data:
        pos = [int(x) for x in line.split("=")[1].split(" ")[0].strip().split(",")]
        vel = [int(x) for x in line.split(" ")[1].strip().split("=")[1].split(",")]
        robots.append([pos, vel])

    seconds = 0
    while True:
        grid = []
        seconds += 1

        all_unique = True
        for robot in robots:
            update_robot(robot)
            if robot[0] in grid:
                all_unique = False
            else:
                grid.append(robot[0])

        if all_unique:
            print("Iteration: " + str(seconds))
            display_robots(robots)
            break


def display_robots(robots):
    positions = [robot[0] for robot in robots]
    for i in range(height):
        for j in range(width):
            if [j, i] in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
