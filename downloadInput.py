import os

day = 0
path = 0

for i in range(1, 26):
    day = str(i)
    path = str(os.getcwd()) + "/day" + day
    # Create folder from input
    try:
        os.mkdir(path)
        break
    except OSError:
        print("Creation of the directory %s failed" % path)

# Create and Write to part1.py
part1 = path + "/day" + day + ".py"
f = open(part1, "a")
f.write("from aocd import get_data\n\n")
f.write("def read_data():\n")
f.write("    global dataRaw, data\n")
f.write("    # dataRaw = get_data(year=2024, day=1)\n")
f.write('    # with open("example.txt", "r") as file:\n')
f.write('    with open("input.txt", "r") as file:\n')
f.write("        dataRaw = file.read()\n\n")
f.write("    data = dataRaw.split(\"\\n\")\n\n")
f.write('def do_part1():\n')
f.write('   pass\n\n')
f.write('def do_part2():\n')
f.write('   pass\n\n')
f.write("if __name__ == '__main__':\n")
f.write('    read_data()\n')
f.write('    do_part1()\n')
f.write('    # do_part2()\n\n')

f.close()

part1 = path + "/input.txt"
f = open(part1, "a")
f.close()

part1 = path + "/example.txt"
f = open(part1, "a")
f.close()

# Success?!
print(str(path) + " and adjacent files created!")
