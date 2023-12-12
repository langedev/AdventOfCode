input = open("input", 'r')
# input = open("sample", 'r')

data = []
total = []
dkey = 811589153

for line in input:
    line = line.strip()
    data.append(int(line) * dkey)

data2 = [num for num in data]

for _ in range(10):
    for num in data:
        if num == 0:
            continue
        pos = data2.index(num)
        del data2[pos]
        newpos = (pos + num) % len(data2)
        if newpos == 0:
            data2.append(num)
        else:
            data2.insert(newpos, num)

zeropos = data2.index(0)
total.append(data2[(zeropos + 1000) % len(data2)])
total.append(data2[(zeropos + 2000) % len(data2)])
total.append(data2[(zeropos + 3000) % len(data2)])

print(total)
print(sum(total))
