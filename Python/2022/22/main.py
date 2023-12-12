# input = open("input", 'r')
input = open("sample", 'r')

sample = True
data = []
instr = []
total = 0
sz = 4 if sample else 50
length = 16 if sample else 150

mode = 0
for line in input:
    if line == "\n":
        mode = 1
        continue
    # Map
    if mode == 0:
        line = line[:-1]
        row = []
        for char in line:
            row.append(char)
        while len(row) < length:
            row.append(" ")
        data.append(row)
    else:
        line = line.strip()
        num = ""
        for char in line:
            if char in ["1","2","3","4","5","6","7","8","9","0"]:
                num += char
            else:
                if num != "":
                    instr.append(int(num))
                    num = ""
                instr.append(char)
        instr.append(int(num))

# Right, Down, Left, Up
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
row = 0
column = sz
facing = 0
for ins in instr:
    if type(ins) == int:
        for _ in range(ins):
            # Column, row
            dr = row + dirs[facing][0]
            dc = column + dirs[facing][1]
            if dr >= len(data):
                dr = 0
            elif dr < 0:
                dr = len(data)-1

            if dc >= len(data[0]):
                dc = 0
            elif dc < 0:
                dc = len(data[0])-1

            piece = data[dr][dc]
            while piece == " ":
                dr += dirs[facing][0]
                dc += dirs[facing][1]
                if dr >= len(data):
                    dr = 0
                elif dr < 0:
                    dr = len(data)-1

                if dc >= len(data[0]):
                    dc = 0
                elif dc < 0:
                    dc = len(data[0])-1

                piece = data[dr][dc]
            if piece == ".":
                row = dr
                column = dc
            elif piece == "#":
                break
    else:
        facing += 1 if ins == "R" else -1
        facing %= 4

print(1000 * (row+1) + 4 * (column+1) + facing)

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
row = 0
column = sz
facing = 0
for ins in instr:
    if type(ins) == int:
        for _ in range(ins):
            # Column, row
            dr = row + dirs[facing][0]
            dc = column + dirs[facing][1]
            if dr >= len(data):
                dr = 0
            elif dr < 0:
                dr = len(data)-1

            if dc >= len(data[0]):
                dc = 0
            elif dc < 0:
                dc = len(data[0])-1

            piece = data[dr][dc]
            if piece == " ":
            if piece == ".":
                row = dr
                column = dc
            elif piece == "#":
                break
    else:
        facing += 1 if ins == "R" else -1
        facing %= 4
