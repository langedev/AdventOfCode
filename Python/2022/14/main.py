input = open("input", 'r')
# input = open("sample", 'r')

data = []
total = 0

minx = 1000
miny = 0
maxx = 500
maxy = 0
for line in input:
    nums = line.strip().split(" -> ")
    tempdata = []
    for string in nums:
        x, y = string.split(",")
        minx = min(minx, int(x))
        miny = min(miny, int(y))
        maxx = max(maxx, int(x))
        maxy = max(maxy, int(y))
        tempdata.append((int(x), int(y)))
    data.append(tempdata)

minx -= maxy

grid = [["." for _ in range(maxx-minx+1+maxy)] for _ in range(maxy-miny+1)]

for line in data:
    for one, two in zip(line, line[1:]):
        if one[0] == two[0]:
            i = min(one[1], two[1])
            a = max(one[1], two[1])
            for y in range(i, a+1):
                grid[y-miny][one[0]-minx] = "#"
        else:
            i = min(one[0], two[0])
            a = max(one[0], two[0])
            for x in range(i, a+1):
                grid[one[1]-miny][x-minx] = "#"

# Send sand
falling = False
while not falling:
    settled = False
    sandpos = (500-minx, 0-miny)
    while not settled:
        if sandpos[1]+1 >= len(grid):
            falling = True
            break
        if grid[sandpos[1]+1][sandpos[0]] == ".":
            sandpos = (sandpos[0], sandpos[1]+1)
        elif grid[sandpos[1]+1][sandpos[0]-1] == ".":
            sandpos = (sandpos[0]-1, sandpos[1]+1)
        elif grid[sandpos[1]+1][sandpos[0]+1] == ".":
            sandpos = (sandpos[0]+1, sandpos[1]+1)
        else:
            grid[sandpos[1]][sandpos[0]] = "o"
            settled = True
            total += 1
        # print(sandpos)

print(total)

grid.append(["." for _ in range(maxx-minx+1+maxy)])
grid.append(["#" for _ in range(maxx-minx+1+maxy)])

final = False
while not final:
    settled = False
    sandpos = (500-minx, 0-miny)
    while not settled:
        if grid[sandpos[1]+1][sandpos[0]] == ".":
            sandpos = (sandpos[0], sandpos[1]+1)
        elif grid[sandpos[1]+1][sandpos[0]-1] == ".":
            sandpos = (sandpos[0]-1, sandpos[1]+1)
        elif grid[sandpos[1]+1][sandpos[0]+1] == ".":
            sandpos = (sandpos[0]+1, sandpos[1]+1)
        else:
            if sandpos[1] == 0-miny and sandpos[0] == 500-minx:
                final = True
            grid[sandpos[1]][sandpos[0]] = "o"
            settled = True
            total += 1
        # print(sandpos)
for row in grid:
    for column in row:
        print(column, end="")
    print()
print(total)
