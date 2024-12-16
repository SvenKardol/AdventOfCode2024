import collections

from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    # with open("example2.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n\n")


def determine_start(grid):
    start_grid = []
    start_pos = []
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch in "O":
                start_grid.append([j, i])
            if ch in "@":
                start_pos = [j, i]

    return start_pos, start_grid


def determine_start2(grid):
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch == "@":
               return j, i

    return ()


def do_part1():
    grid = data[0].split("\n")
    start_pos, start_grid = determine_start(grid)

    commands = collections.defaultdict(list)
    commands["^"] = [0, -1]
    commands["v"] = [0, 1]
    commands["<"] = [-1, 0]
    commands[">"] = [1, 0]

    command_string = data[1].replace("\n", "")
    for command in command_string:
        robot_can_move = False
        dx, dy = commands[command]

        pushed = 1
        while True:

            check_pos = [start_pos[0] + pushed * dx, start_pos[1] + pushed * dy]
            if check_pos in start_grid:
                pushed += 1
                continue
            if grid[check_pos[1]][check_pos[0]] == "#":
                break
            else:
                robot_can_move = True
                break

        if robot_can_move:
            start_pos[0] += dx
            start_pos[1] += dy
            if start_pos in start_grid:
                start_grid.remove(start_pos)
                start_grid.append([start_pos[0]+(pushed-1)*dx,start_pos[1]+(pushed-1)*dy])

    print_grid(start_grid, start_pos,grid)

    total = 0
    for pos in start_grid:
        total += 100*pos[1] + pos[0]

    print(total)


def print_grid(start_grid, start_pos, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if [j, i] == start_pos:
                print("@", end="")
            elif [j, i] in start_grid:
                print("O", end="")
            elif grid[i][j] == "#":
                print(grid[i][j], end="")
            else:
                print(".", end="")
        print()


def do_part2():
    grid = data[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.").split("\n")
    start_pos = determine_start2(grid)

    commands = collections.defaultdict(list)
    commands["^"] = [0, -1]
    commands["v"] = [0, 1]
    commands["<"] = [-1, 0]
    commands[">"] = [1, 0]

    command_string = data[1].replace("\n", "")
    for command in command_string:
        robot_can_move = True
        dx, dy = commands[command]

        positions_to_change = [start_pos]
        i = 0
        while i < len(positions_to_change):
            x, y = positions_to_change[i]
            new_x, new_y = x + dx, y + dy
            if grid[new_y][new_x] in "[]":
                if (new_x, new_y) not in positions_to_change:
                    positions_to_change.append((new_x, new_y))

                new_element = 1 if grid[new_y][new_x] == "[" else -1
                if (new_x + new_element, new_y) not in positions_to_change:
                    positions_to_change.append((new_x + new_element, new_y))
            elif grid[new_y][new_x] == "#":
                robot_can_move = False
                break
            i += 1

        if not robot_can_move:
            continue

        start_pos = (start_pos[0] + dx, start_pos[1] + dy)
        new_grid = [[grid[i][j] for j, _ in enumerate(line)] for i, line in enumerate(grid)]
        for x, y in positions_to_change:
            new_grid[y][x] = "."
        for x, y in positions_to_change:
            new_grid[y + dy][x + dx] = grid[y][x]

        grid = new_grid

    total = 0
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch == "[":
                total += 100 * i + j
    print(total)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

