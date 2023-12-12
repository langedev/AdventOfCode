input = open("input", 'r')
# input = open("sample", 'r')

data = []
total = 0

ROW = 2_000_000
# ROW = 10

taxicab = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1])
tuning = lambda x: 4_000_000*x[0] + x[1]

minx = 10_000_000
maxx = 0

beaconsRow = set()

for line in input:
    line = line.strip()
    sensor, beacon = line.split(": ")
    sx, sy = sensor.split(", ")
    bx, by = beacon.split(", ")
    sensor = (int(sx.split("=")[1]), int(sy.split("=")[1]))
    beacon = (int(bx.split("=")[1]), int(by.split("=")[1]))
    minx = min(sensor[0], beacon[0], minx)
    maxx = max(sensor[0], beacon[0], maxx)
    data.append((sensor, beacon))

distance = []
for sensor, beacon in data:
    d = taxicab(beacon, sensor)
    if beacon[1] == ROW and beacon not in beaconsRow:
        beaconsRow.add(beacon)
        total -= 1
    distance.append((sensor, d))

for x in range(minx*2, (maxx*2+1)):
    for sensor, dist in distance:
        psd = taxicab(sensor, (x, ROW))
        if dist >= psd:
            # print(x)
            total +=1
            break

print(total)

found = False
for sensor, dist in distance:
    for dx in range(dist+2):
        dy = (dist+1) - dx
        for dirx, diry in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            x = sensor[0] + (dx*dirx)
            y = sensor[1] + (dy*diry)
            if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                continue

            found = True
            for sensor, dist in distance:
                psd = taxicab((x,y),sensor)
                if psd <= dist:
                    found = False
                    break
            if found:
                print(tuning((x,y)))



# for x in range(0, 4_000_000):
#     for y in range(0, 4_000_000):
#         for sensor, dist in distance:
#             psd = taxicab(sensor, (x, ROW))
#             if dist >= psd:
#                 break
#             print((x,y), tuning((x,y)))
