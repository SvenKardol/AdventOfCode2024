from aocd import get_data


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    with open("example.txt", "r") as file:
    # with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def do_part1():
    files, free_spaces, disk_map = [], [], []
    pos, file_id = 0, 0
    for i, ch in enumerate(dataRaw):
        amount = int(ch)

        if i % 2 == 0:
            disk_map += [str(file_id)] * amount
            files += [(pos + x, file_id) for x in range(amount)]
            file_id += 1
        else:
            free_spaces.append((pos, amount))
            disk_map += "." * amount

        pos += amount

    for (pos, file_id) in reversed(files):
        for index_fs, (pos_fs, amount_fs) in enumerate(free_spaces):
            if pos_fs < pos and amount_fs > 0:
                disk_map[pos] = "."
                disk_map[pos_fs] = str(file_id)

                free_spaces[index_fs] = (pos_fs + 1, amount_fs - 1)
                break

    total_sum = 0
    for i, file_id in enumerate(disk_map):
        if file_id != ".":
            total_sum += i * int(file_id)

    calculate_result(disk_map)


def do_part2():
    files, free_spaces, disk_map = [], [], []
    pos, file_id = 0, 0
    for i, ch in enumerate(dataRaw):
        amount = int(ch)

        if i % 2 == 0:
            disk_map += [str(file_id)] * amount
            files += [(pos, file_id, amount)]
            file_id += 1
        else:
            free_spaces.append((pos, amount))
            disk_map += "." * amount

        pos += amount

    for (pos, file_id, amount) in reversed(files):
        for index_fs, (pos_fs, amount_fs) in enumerate(free_spaces):
            if pos_fs < pos and amount <= amount_fs:
                for a in range(amount):
                    disk_map[pos + a] = "."
                    disk_map[pos_fs + a] = str(file_id)

                free_spaces[index_fs] = (pos_fs + amount, amount_fs - amount)
                break

    calculate_result(disk_map)


def calculate_result(disk_map):
    total_sum = 0
    for i, file_id in enumerate(disk_map):
        if file_id != ".":
            total_sum += i * int(file_id)
    print(total_sum)


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
