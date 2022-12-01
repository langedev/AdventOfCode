input = open("input", 'r')

data = [0 for _ in range(400)]

elf = 0

for line in input:
    if line == "\n":
        elf += 1
    else:
        if data[elf]:
            data[elf] += int(line)
        else:
            data[elf] = int(line)

sortedData = sorted(data, reverse=True)

print(sortedData[0])
print(sortedData[0] + sortedData[1] + sortedData[2])
