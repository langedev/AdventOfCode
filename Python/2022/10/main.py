input = open("input", 'r')
# input = open("sample", 'r')
data = []

mode = 0
total = 0
for line in input:
    data.append(line.strip())

x = 1
i = 1
for line in data:
    # No-op
    if len(line) == 4:
        i += 1
        if (i + 20) % 40 == 0:
            total += i * x
        continue
    # addx
    else:
        i += 1
        if (i + 20) % 40 == 0:
            total += i * x
        i += 1
        addx, num = line.split(" ")
        x += int(num)
        if (i + 20) % 40 == 0:
            total += i * x

print(total)
CRT = ["." for _ in range(40*6)]
def printcrt():
    for i, dot in enumerate(CRT):
        print(dot, end="")
        if (i+1) % 40 == 0:
            print()

data2 = []
i = 1
for line in data:
    # No-op
    if len(line) == 4:
        data2.append([line, 0])
        continue
    # addx
    else:
        addx, num = line.split(" ")
        data2.append(["noop", 0])
        data2.append([addx, int(num)])

x = 1
for i in range(40*6):
    index = i % 40
    rng = list(range(x-1, x+2))
    if index in rng:
        CRT[i] = "#"
    # run instruction
    instr = data2[i]
    if instr[0] == "addx":
        x += instr[1]

printcrt()
