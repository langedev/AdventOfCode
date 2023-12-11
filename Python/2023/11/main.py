import math

input = open("input", 'r')

data = []

for i, line in enumerate(input):
    line = list(line.rstrip())
    data.append(line)


# expansion_factor = 1
expansion_factor = 1_000_000 - 1
cols = dict()
rows = dict()
offset = 0

for row in range(len(data)):
    if all(data[row][col] == '.' for col in range(len(data[row]))):
        offset += expansion_factor
    else:
        rows[row] = row + offset
offset = 0
for col in range(len(data[0])):
    if all(data[row][col] == '.' for row in range(len(data))):
        offset += expansion_factor
    else:
        cols[col] = col + offset

galaxies = []

for i, line in enumerate(data):
    for j, point in enumerate(line):
        if point == "#":
            galaxies.append((rows[i],cols[j]))

def shortestPath(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

paths = []

for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        paths.append(shortestPath(galaxy1, galaxy2))

print(sum(paths))
