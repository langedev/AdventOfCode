input = open("input", 'r')
# input = open("sample", 'r')

data = {}
total = 0
validLocations = []

for line in input:
    line = line.strip()
    valve, to = line.split("; ")

    name, rate = valve.split(" has")
    name = name[-2:]
    rate = int(rate.split("=")[1])

    tonames = to.split("valve")[1].split(", ")
    tonames[0] = tonames[0][-2:]

    if rate > 0:
        validLocations.append(name)
    data[name] = [rate, tonames, False]

# Part 1
