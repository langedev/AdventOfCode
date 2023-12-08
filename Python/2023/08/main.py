import math

input = open("input", 'r')

instructions = input.readline().rstrip()
data = {}
all_nodes = []

_ = input.readline()

for line in input:
    line = line.rstrip()
    node, nexts = line.split(" = ")
    left, right = nexts.split(", ")

    all_nodes.append(node)

    data[node] = {
        "left": left[1:],
        "right": right[:-1]
    }


current = "AAA"
inst = 0

steps = 0

while current != "ZZZ":
    go = instructions[inst]
    steps += 1
    inst = (inst + 1) % len(instructions)
    if go == "L":
        current = data[current]["left"]
    else:
        current = data[current]["right"]

print(steps)

def fromAToZ(start, ends):
    current = start
    inst = 0
    steps = 0

    while current not in ends:
        go = instructions[inst]
        steps += 1
        inst = (inst + 1) % len(instructions)
        direct = "left" if go == "L" else "right"
        current = data[current][direct]

    return steps

starts = [node for node in all_nodes if node[-1] == "A"]
ends = [node for node in all_nodes if node[-1] == "Z"]

print(math.lcm(*[fromAToZ(start, ends) for start in starts]))
