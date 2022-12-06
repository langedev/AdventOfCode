input = open("input", 'r')
# input = open("sample", 'r')

for line in input:
    line = line.strip()
    for i in range(len(line)):
        marker = set(line[i:i+4])
        if sum(1 for item in marker) >= 4:
            print(i+4)
            break

    for i in range(len(line)):
        marker = set(line[i:i+14])
        if sum(1 for item in marker) >= 14:
            print(i+14)
            break
