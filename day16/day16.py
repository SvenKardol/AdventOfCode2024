import collections
import functools

from aocd import get_data


def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    # with open("example2.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")


def within_grid(pos):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data)


def find_start():
    start = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "S":
                start = (x, y)
    return start


def find_end():
    start = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "E":
                start = (x, y)
    return start


@functools.cache
def updated_states(state):
    options = ((1, 0), (0, 1), (-1, 0), (0, -1))
    cords, direction = state
    new_cords = (cords[0] + options[direction][0], cords[1] + options[direction][1])
    return {
        (new_cords, direction): 1,
        (cords, (direction + 1) % 4): 1000,
        (cords, (direction - 1) % 4): 1000
    }

@functools.cache
def reverse_states(state):
    options = ((1, 0), (0, 1), (-1, 0), (0, -1))
    cords, direction = state
    new_cords = (cords[0] - options[direction][0], cords[1] - options[direction][1])
    return {
        (new_cords, direction): 1,
        (cords, (direction + 1) % 4): 1000,
        (cords, (direction - 1) % 4): 1000
    }


def do_part1():
    final_state = find_final_states()

    print(best_score(final_state))


@functools.cache
def find_final_states():

    start = find_start()
    states = collections.defaultdict(lambda: 10 ** 10)
    states[(start, 0)] = 0
    queue = ([(start, 0)])
    while len(queue) > 0:
        item = queue.pop()
        original_cost = states[item]

        new_states = updated_states(item)

        for new_state, cost in new_states.items():
            if not within_grid(new_state[0]):
                continue
            if data[new_state[0][1]][new_state[0][0]] == "#":
                continue

            new_cost = original_cost + cost
            if new_cost < states[new_state]:
                states[new_state] = new_cost
                queue.append(new_state)

    return states


def best_score(states):
    scores = []
    end = find_end()
    for state in states.keys():
        if state[0] == end:
            scores.append(states[state])
    return min(scores)

def find_best_state(states):
    end = find_end()
    best_state = min(((end, _) for _ in range(4)), key=states.get)

    return best_state


def do_part2():
    final_states = find_final_states()

    # work back from best state:
    best_state = find_best_state(final_states)

    unique_locations = {best_state[0]}

    queue = ([best_state])
    while len(queue) > 0:
        item = queue.pop()
        original_cost = final_states[item]

        new_states = reverse_states(item)

        for new_state, cost in new_states.items():
            if not within_grid(new_state[0]):
                continue
            if data[new_state[0][1]][new_state[0][0]] == "#":
                continue

            if final_states[new_state] + cost == original_cost:
                queue.append(new_state)
                unique_locations.add(new_state[0])


    print(len(unique_locations))


if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()
