import sys
input = open("input", 'r')
# input = open("sample", 'r')

data = []
total = 0
mypos = (0, 0)
epos = (0, 0)

x = 0
y = 0
for line in input:
    data.append([])
    x = 0
    for c in line.strip():
        if c == "S":
            mypos = (x, y)
            data[y].append(ord("a") - ord("a"))
        elif c == "E":
            epos = (x, y)
            data[y].append(ord("z") - ord("a"))
        else:
            data[y].append(ord(c) - ord("a"))
        x += 1
    y += 1

move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def dijkstras(m, start):
    unvisited = []
    for y in range(len(m)):
        for x in range(len(m[0])):
            unvisited.append((x,y))

    sp = {}
    pn = {}

    max_value = sys.maxsize
    for node in unvisited:
        sp[node] = max_value
    sp[start] = 0

    while unvisited:
        cmn = None
        for pos in unvisited:
            if cmn == None:
                cmn = pos
            elif sp[pos] < sp[cmn]:
                cmn = pos

        neighbors = []
        for side in move:
            newPos = (cmn[0] + side[0], cmn[1] + side[1])
            if newPos[0] < 0 or newPos[0] >= len(m[0]):
                continue
            elif newPos[1] < 0 or newPos[1] >= len(m):
                continue
            posV = m[cmn[1]][cmn[0]]
            nposV = m[newPos[1]][newPos[0]]
            if posV + 1 >= nposV:
                neighbors.append(newPos)

        for neighbor in neighbors:
            tv = sp[cmn] + 1
            if tv < sp[neighbor]:
                sp[neighbor] = tv
                pn[neighbor] = cmn

        unvisited.remove(cmn)

    return pn, sp

pn, sp = dijkstras(data, mypos)

print(sp[epos])
aStarts = []

move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def dijkstras_rev(m, start):
    unvisited = []
    for y in range(len(m)):
        for x in range(len(m[0])):
            unvisited.append((x,y))

    sp = {}
    pn = {}

    max_value = sys.maxsize
    for node in unvisited:
        sp[node] = max_value
    sp[start] = 0

    while unvisited:
        cmn = None
        for pos in unvisited:
            if cmn == None:
                cmn = pos
            elif sp[pos] < sp[cmn]:
                cmn = pos

        neighbors = []
        for side in move:
            newPos = (cmn[0] + side[0], cmn[1] + side[1])
            if newPos[0] < 0 or newPos[0] >= len(m[0]):
                continue
            elif newPos[1] < 0 or newPos[1] >= len(m):
                continue
            posV = m[cmn[1]][cmn[0]]
            nposV = m[newPos[1]][newPos[0]]
            if posV - 1 <= nposV:
                neighbors.append(newPos)

        for neighbor in neighbors:
            tv = sp[cmn] + 1
            if tv < sp[neighbor]:
                sp[neighbor] = tv
                pn[neighbor] = cmn

        unvisited.remove(cmn)

    return pn, sp

pn, sp = dijkstras_rev(data, epos)


aMin = []
for key in sp:
    if data[key[1]][key[0]] == 0:
        aMin.append(sp[key])

print(min(aMin))
