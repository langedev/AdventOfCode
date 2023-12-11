import math

input = open("input", 'r')

data = []
start = (0,0)

for i, line in enumerate(input):
    line = line.rstrip()
    if "S" in line:
        for j in range(len(line)):
            if line[j] == "S":
                start = (i, j)
    data.append(list(line))

# replace "S" with character based on input so I don't need a bunch of code for it. line[j] = "7"
data[start[0]][start[1]] = "7"
# data[start[0]][start[1]] = "F"

explored = [["." for _ in line] for line in data]

def north(pos):
    return ((pos[0]-1, pos[1]), "s")
def south(pos):
    return ((pos[0]+1, pos[1]), "n")
def east(pos):
    return ((pos[0], pos[1]+1), "w")
def west(pos):
    return ((pos[0], pos[1]-1), "e")

def next_tile(pos, prev_card):
    tile = data[pos[0]][pos[1]]
    explored[pos[0]][pos[1]] = tile
    if tile == "|":
        return north(pos) if prev_card == "s" else south(pos)
    if tile == "L":
        return north(pos) if prev_card == "e" else east(pos)
    if tile == "J":
        return north(pos) if prev_card == "w" else west(pos)
    if tile == "F":
        return south(pos) if prev_card == "e" else east(pos)
    if tile == "7":
        return south(pos) if prev_card == "w" else west(pos)
    if tile == "-":
        return east(pos) if prev_card == "w" else west(pos)
    print("ERROR")
    return (pos, prev_card)

forward = next_tile(start, "w")
backward = next_tile(start, "s")

iters = 1
while forward[0] != backward[0]:
    forward = next_tile(*forward)
    backward = next_tile(*backward)
    iters += 1

print(iters)

insides = 0

# for row in explored:
#     for column in row:
#         print(column, end=" ")
#     print()

for i, row in enumerate(explored):
    pipes_crossed = 0
    j = 0
    while j < len(row):
        start_j = j
        tile = row[j]
        if tile == "." and pipes_crossed % 2 == 1:
            explored[i][j] = "I"
            insides += 1
        elif tile == "|":
            pipes_crossed += 1
        elif tile == "L":
            j += 1
            tile = row[j]
            while tile == "-":
                j += 1
                tile = row[j]
            if tile == "7":
                pipes_crossed += 1
        elif tile == "F":
            j += 1
            tile = row[j]
            while tile == "-":
                j += 1
                tile = row[j]
            if tile == "J":
                pipes_crossed += 1
        j += 1

# for row in explored:
#     for column in row:
#         print(column, end="")
#     print()

print(insides)
