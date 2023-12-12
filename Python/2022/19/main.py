
import functools

input = open("input", 'r')
# input = open("sample", 'r')

data = []
total = 0

for line in input:
    line = line.strip()
    parts = line.split(".")
    orecost = int(parts[0].split("costs ")[1][0])
    claycost = int(parts[1].split("costs ")[1][0])
    obsCostX = parts[2].split("costs ")[1]
    obsCost = [int(obsCostX[0]), int(obsCostX.split("and ")[1].split(" ")[0])]
    geoCostX = parts[3].split("costs ")[1]
    geoCost = [int(geoCostX[0]), int(geoCostX.split("and ")[1].split(" ")[0])]

    data.append([orecost, claycost, obsCost, geoCost])

@functools.cache
def maximize_geodes(i, resources, robots, time):
    # Previous rounds resources
    resources = (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3])

    if time >= 24:
        return resources[3]

    paths = [0 for i in range(5)]

    if data[i][0] <= resources[0]:
        # Buy Orebot
        tempRobot = (robots[0] + 1, robots[1], robots[2], robots[3])
        tempResources = (resources[0] - data[i][0], resources[1], resources[2], resources[3])
        paths[0] = maximize_geodes(i, tempResources, tempRobot, time+1)
    if data[i][1] <= resources[0]:
        # Buy Claybot
        tempRobot = (robots[0], robots[1]+1, robots[2], robots[3])
        tempResources = (resources[0] - data[i][1], resources[1], resources[2], resources[3])
        paths[1] = maximize_geodes(i, tempResources, tempRobot, time+1)
    if data[i][2][0] <= resources[0] and data[i][2][1] <= resources[1]:
        # Buy ObsBot
        tempRobot = (robots[0], robots[1], robots[2]+1, robots[3])
        tempResources = (resources[0] - data[i][2][0], resources[1]-data[i][2][1], resources[2], resources[3])
        paths[1] = maximize_geodes(i, tempResources, tempRobot, time+1)
    if data[i][3][0] <= resources[0] and data[i][3][1] <= resources[2]:
        # Buy GeodeBot
        tempRobot = (robots[0], robots[1], robots[2], robots[3]+1)
        tempResources = (resources[0] - data[i][3][0], resources[1], resources[2]-data[i][3][1], resources[3])
        paths[1] = maximize_geodes(i, tempResources, tempRobot, time+1)

    # Do Nothing
    paths[4] = maximize_geodes(i, resources, robots, time+1)

    return max(paths)


ql = [0 for _ in data]
dp = [[] for minute in range(24)]

for i, bp in enumerate(data):
    bpNum = i + 1
    print(bpNum)
    ql[i] = bpNum * maximize_geodes(i, (0,0,0,0), (1,0,0,0), 2)
    print(ql)



print(sum(ql))
