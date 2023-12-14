import numpy as np

input = open("input", 'r').read()

data = [[row for row in island.split("\n") if row != ""] for island in input.split("\n\n")]

def print_island(island):
    for row in island:
        print("".join(row))
    print()

def findMirror(island, ignore=-1, fix_mistake=False):
    left_columns = 0
    for column in range(1, len(island[0])):
        fixed_mistake = False
        mirror = True
        for row in island:
            right = column
            left = right - 1
            while left >= 0 and right < len(island[0]):
                if row[left] != row[right]:
                    if fix_mistake and not fixed_mistake:
                        fixed_mistake = True
                    else:
                        mirror = False
                left -= 1
                right += 1
            if not mirror:
                break
        if mirror and column != ignore:
            left_columns = column
            break
    return left_columns

mirrors = []

for island in data:
    column = 0
    row = 0
    island = np.array([list(row) for row in island])
    column = findMirror(island)
    flipped_island = np.transpose(island)
    row = findMirror(flipped_island)
    mirrors.append((row, column))

print(sum([column for _, column in mirrors]) +
      sum([row for row, _ in mirrors]) * 100)

mirrors_2 = []

for i, island in enumerate(data):
    column = 0
    row = 0
    island = np.array([list(row) for row in island])
    column = findMirror(island, mirrors[i][1], True)
    flipped_island = np.transpose(island)
    row = findMirror(flipped_island, mirrors[i][0], True)
    mirrors_2.append((row, column))

print(sum([column for _, column in mirrors_2]) +
      sum([row for row, _ in mirrors_2]) * 100)
