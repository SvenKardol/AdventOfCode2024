import functools

from aocd import get_data


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def do_part1():
    stones = [int(x) for x in dataRaw.split(" ")]

    for i in range(25):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                l = int(len(str(stone)) / 2)
                new_stones.append(int(str(stone)[:l]))
                new_stones.append(int(str(stone)[l:]))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    print(len(stones))


def do_part2():
    stones = [int(x) for x in dataRaw.split(" ")]
    total_stones = 0
    for stone in stones:
        total_stones += num_stones_after_done_blinking(stone, 75)

    print(total_stones)


@functools.cache
def num_stones_after_done_blinking(stone, blinks_todo):
    if blinks_todo == 0:
        return 1

    new_blinks_todo = blinks_todo - 1
    if stone == 0:
        return num_stones_after_done_blinking(1, new_blinks_todo)

    if len(str(stone)) % 2 == 0:
        l = int(len(str(stone)) / 2)
        first_stone = int(str(stone)[:l])
        second_stone = int(str(stone)[l:])
        num_from_first_stone = num_stones_after_done_blinking(first_stone, new_blinks_todo)
        num_from_second_stone = num_stones_after_done_blinking(second_stone, new_blinks_todo)
        return num_from_first_stone + num_from_second_stone

    return num_stones_after_done_blinking(stone * 2024, new_blinks_todo)


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
