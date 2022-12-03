input = open("input", 'r')
# input = open("sample", 'r')

data = []
data2 = []

total = 0

for line in input:
    data2.append(line.strip())
    size = len(line) // 2
    f = line[:size]
    s = line[size:]

    letter = None
    for char1 in f:
        for char2 in s:
            if char1 == char2:
                letter = char1
                break

    r = ord(letter)

    if r >= 97:
        total += r - ord('a') + 1
    else:
        total += r - ord('A') + 27

total2 = 0

print(data2)

for i in range(0, len(data2),3):
    f = data2[i]
    s = data2[i+1]
    t = data2[i+2]

    letter = None
    for char1 in f:
        for char2 in s:
            for char3 in t:
                if char1 == char2 and char1 == char3:
                    letter = char1
                    break

    r = ord(letter)

    if r >= 97:
        total2 += r - ord('a') + 1
    else:
        total2 += r - ord('A') + 27


print(total)
print(total2)
