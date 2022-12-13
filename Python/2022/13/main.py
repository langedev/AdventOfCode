from functools import cmp_to_key
input = open("input", 'r')
# input = open("sample", 'r')

data = []
total = []
pair = None
for line in input:
    if line == "\n":
        continue
    data.append(eval(line.strip()))

def compare(l, r):
    if type(l) != type(r):
        # One int, one list, convert both to lists
        if type(l) != list:
            l = [l]
        if type(r) != list:
            r = [r]

    # If both lists
    if type(l) == list:
        for i in range(len(l)):
            lval = l[i]
            if len(r) <= i:
                return -1
            rval = r[i]
            val = compare(lval, rval)
            if val == 1:
                continue
            elif val == 2:
                return 2
            elif val == -1:
                return -1
        if len(l) == len(r):
            return 1
        elif len(l) < len(r):
            return 2
        else:
            return -1
    # If both ints
    else:
        if l < r:
            return 2
        elif l > r:
            return -1
        else:
            return 1

pair = 1
for i in range(0, len(data), 2):
    a = data[i]
    b = data[i+1]
    order = compare(a, b)
    if order != -1:
        total.append(pair)
    pair += 1

print(sum(total))

data.append([[2]])
data.append([[6]])

part2 = sorted(data,key=cmp_to_key(compare), reverse=True)
total2 = 1
for i, packet in enumerate(part2):
    if packet == [[2]] or packet == [[6]]:
        total2 *= (i + 1)

print(total2)
