input = open("input2", 'r')

data = []

elf  = 0
curr = 0

for line in input:
    if line == "\n":
        data.append(curr)
        curr = 0
    else:
        curr += int(line)

sortedData = sorted(data, reverse=True)

print(sortedData[0])
print(sortedData[0] + sortedData[1] + sortedData[2])
