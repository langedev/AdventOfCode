input = open("input", 'r')
# input = open("sample", 'r')
# input = open("test", 'r')

pairwise = lambda a,b: (a[0] + b[0], a[1]+b[1], a[2]+b[2])

data = []
data2 = []
total = 0

for line in input:
    line = line.strip()
    x,y,z = line.split(",")
    data.append([(int(x),int(y),int(z)), [False for _ in range(6)]])
    data2.append((int(x),int(y),int(z)))

dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

for cubedata in data:
    for i,dr in enumerate(dirs):
        if cubedata[1][i]:
            continue
        side = pairwise(cubedata[0],dr)
        if side in data2:
            ind = data2.index(side)
            cubedata[1][i] = True
            if i % 2 == 0:
                data[ind][1][i+1] = True
            else:
                data[ind][1][i-1] = True

for cubedata in data:
    for covered in cubedata[1]:
        if not covered:
            total += 1

# print(data)
print(total)
total2 = total
all_cubes = {(x,y,z) for x in range(22) for y in range(22) for z in range(22)}
empty_cubes = all_cubes-scanned_cubes
q = [(0,0,0)]
while q:
    c = q.pop()
    if c in empty_cubes:
        empty_cubes.remove(c)
        q.extend(adj_cubes(c))
for cube in empty_cubes:
    p2 += 6
    for adj in adj_cubes(cube):
        if adj in scanned_cubes:
            p2 -= 2
    scanned_cubes.add(cube)
print("Part 2:",p2)
