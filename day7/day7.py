from aocd import get_data

def read_data():
    global dataRaw, data
    # dataRaw = get_data(year=2024, day=1)
    # with open("example.txt", "r") as file:
    with open("input.txt", "r") as file:
        dataRaw = file.read()

    data = dataRaw.split("\n")

def do_part1():
    total_sum = 0
    for line in data:
        total = int(line.split(":")[0])
        numbers = [int(x) for x in line.split(":")[1].split()]

        options = [numbers[0]]

        for i, num in enumerate(numbers):
            if i == 0:
                continue
            new_options = []
            for option in options:
                new_option1 = option + num
                new_option2 = option * num

                if new_option1 <= total:
                    new_options.append(new_option1)
                if new_option2 <= total:
                    new_options.append(new_option2)

            options = new_options

        for option in options:
            if option == total:
                total_sum += total
                break
    print(total_sum)

def do_part2():
    total_sum = 0
    for line in data:
        total = int(line.split(":")[0])
        numbers = [int(x) for x in line.split(":")[1].split()]

        options = [numbers[0]]

        for i, num in enumerate(numbers):
            if i == 0:
                continue
            new_options = []
            for option in options:
                new_option1 = option + num
                new_option2 = option * num
                new_option3 = int(str(option)+ str(num))

                if new_option1 <= total:
                    new_options.append(new_option1)
                if new_option2 <= total:
                    new_options.append(new_option2)
                if new_option3 <= total:
                    new_options.append(new_option3)

            options = new_options

        for option in options:
            if option == total:
                total_sum += total
                break
    print(total_sum)

if __name__ == '__main__':
    read_data()
    do_part1()
    do_part2()

