import statistics
with open("input.txt", 'r') as f:
    data = f.readlines()
    data = list(map(int, data[0].strip().split(",")))

# Part 1
median = statistics.median(data)
fuelCost = 0
for crab in data:
    fuelCost += abs(median - crab)

print(fuelCost)

# Part 2
flist = []
# Definitely a better way than checking all of these
for pos in range(0, max(data)+1):
    fuel = 0
    for crab in data:
        fuel += (abs(pos - crab)*(abs(pos - crab)+1))/2
    flist.append(fuel)

print(min(flist))
