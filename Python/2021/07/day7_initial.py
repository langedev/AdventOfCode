with open("input.txt", 'r') as f:
    data = f.readlines()
    data = list(map(int, data[0].strip().split(",")))

def crabMove(crab, pos):
    difference = abs(pos - crab)
    # return difference
    return (difference*(difference+1))/2

bestPos = 0
bestFuel = 1000000000
for i in range(min(data), max(data)):
    fuelCost = 0
    for crab in data:
        fuelCost += crabMove(crab, i)
    if fuelCost < bestFuel:
        bestFuel = fuelCost
        bestPos = i

print(bestFuel)
