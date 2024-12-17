import collections
import functools

import scipy.special
from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    # with open("example2.txt", "r") as file:
    # with open("example3.txt", "r") as file:
    # with open("example4.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n\n")

def do_part1():
    print(run_program())


def run_program(value_A = 0, part2=False):
    registers = collections.defaultdict()
    for machine in data[0].split("\n"):
        letter = machine.split(" ")[1].split(":")[0]
        number = int(machine.split(":")[1].strip())

        if part2 and letter == "A":
            registers[letter] = value_A
        else:
            registers[letter] = number
    program = [int(x) for x in data[1].split(":")[1].split(",")]
    instruction = 0
    output = []
    while instruction < len(program) - 1:
        code = program[instruction]
        operand = program[instruction + 1]

        if code == 0:
            combo = get_combos(operand, registers)
            registers["A"] = registers["A"] // 2 ** combo
        elif code == 1:
            registers["B"] = registers["B"] ^ operand
        elif code == 2:
            combo = get_combos(operand, registers)
            registers["B"] = combo % 8
        elif code == 3:
            if registers["A"] != 0:
                instruction = operand
                continue
        elif code == 4:
            registers["B"] = registers["B"] ^ registers["C"]
        elif code == 5:
            combo = get_combos(operand, registers)
            output.append(combo % 8)
        elif code == 6:
            combo = get_combos(operand, registers)
            registers["B"] = registers["A"] // 2 ** combo
        elif code == 7:
            combo = get_combos(operand, registers)
            registers["C"] = registers["A"] // 2 ** combo

        instruction += 2
    return output


def get_combos(i, registers):
    combo_in = get_combo(i)
    return combo_in if not isinstance(combo_in, str) else registers[combo_in]


def get_combo(i):
    if i <= 3:
        return i
    if i == 4 :
        return "A"
    if i == 5:
        return "B"
    if i == 6:
        return "C"
    if i == 7:
        return -1


def do_part2():
    program = [int(x) for x in data[1].split(":")[1].split(",")]

    # start with A = 0 and work from the back to get right digit. Then multiply by 8 for the next digit.
    values_to_check = [(1, 0)]
    next_iteration_needed = True
    for current_length_match, value_a in values_to_check:
        if not next_iteration_needed:
            break
        for input_a in range(value_a, value_a + 8):
            output = run_program(input_a,True)

            # match on last couple digits, new item is included in values_to_check
            if  output == program[-current_length_match:]:
                values_to_check.append([current_length_match + 1, input_a * 8])

                # 100% match. We're done!!!
                if output == program:
                    print(input_a)
                    next_iteration_needed = False
                    break

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

