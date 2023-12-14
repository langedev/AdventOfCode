import numpy as np
import functools

input = open("input", 'r')#.read()

data = []

for i, line in enumerate(input):
    line = line.rstrip()
    data.append(list(line))

def printA(A):
    for row in A:
        print("".join(row))
    print()

def tilt():
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            moveto = j
            if char == "O":
                while moveto-1 >= 0 and data[moveto-1][i] == ".":
                    moveto -= 1
                data[j][i] = "."
                data[moveto][i] = "O"

def load():
    load = []

    for j, row in enumerate(data):
        for i, char in enumerate(row):
            if char == "O":
                load.append(len(data)-j)

    return sum(load)

def cycle():
    # North
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            moveto = j
            if char == "O":
                while moveto-1 >= 0 and data[moveto-1][i] == ".":
                    moveto -= 1
                data[j][i] = "."
                data[moveto][i] = "O"
    # West
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            moveto = i
            if char == "O":
                while moveto-1 >= 0 and data[j][moveto-1] == ".":
                    moveto -= 1
                data[j][i] = "."
                data[j][moveto] = "O"
    # South
    for j in range(len(data)-1, -1, -1):
        row = data[j]
        for i, char in enumerate(row):
            char = row[i]
            moveto = j
            if char == "O":
                while moveto+1 < len(row) and data[moveto+1][i] == ".":
                    moveto += 1
                data[j][i] = "."
                data[moveto][i] = "O"
    # East
    for j, row in enumerate(data):
        for i in range(len(row)-1, -1, -1):
            char = row[i]
            moveto = i
            if char == "O":
                while moveto+1 < len(row) and data[j][moveto+1] == ".":
                    moveto += 1
                data[j][i] = "."
                data[j][moveto] = "O"

def dataStr(data):
    return "".join(["".join(row) for row in data])

# Part 1

# tilt()
# print(load())

# Part 2

datadict = {}
target = 1000000000
i = 1

load_val = None

while load_val == None:
    cycle()
    strdata = dataStr(data)

    if strdata in datadict:
        old_i = datadict[strdata][0]
        cycle = i - old_i
        for j,loaded in datadict.values():
            if j >= old_i and j % cycle == target % cycle:
                load_val = loaded

    datadict[strdata] = (i, load())
    i += 1

print(load_val)
