input = open("input.txt", 'r')

data = []

for line in input:
    data.append(list(line.strip().split(" ")))

letters = [set() for i in range(0, 10)]
dataset = ['a','b','c','d','e','f','g']
total = 0

for line in data:
    letters = [set() for i in range(0, 10)]
    for i in range(0, 10):
        entry = line[i]
        if len(entry) == 2:
            letters[1] = set([frozenset(entry)])
        elif len(entry) == 3:
            letters[7] = set([frozenset(entry)])
        elif len(entry) == 4:
            letters[4] = set([frozenset(entry)])
        elif len(entry) == 5:
            letters[2].update(set([frozenset(entry)]))
            letters[3].update(set([frozenset(entry)]))
            letters[5].update(set([frozenset(entry)]))
        elif len(entry) == 6:
            letters[0].update(set([frozenset(entry)]))
            letters[6].update(set([frozenset(entry)]))
            letters[9].update(set([frozenset(entry)]))
        elif len(entry) == 7:
            letters[8] = set([frozenset(entry)])
    cf = letters[1].pop()
    letters[1].add(cf)
    for st in letters[3]:
        if st.intersection(cf) == cf:
            letters[3] = set([st])
            letters[2].remove(st)
            letters[5].remove(st)

    acf = letters[7].pop()
    letters[7].add(acf)
    for st in letters[6]:
        if st.intersection(acf) != acf:
            letters[6] = set([st])
            letters[0].remove(st)
            letters[9].remove(st)

    abdefg = letters[6].pop()
    letters[6].add(abdefg)
    c = frozenset(dataset).difference(abdefg)
    for st in letters[2]:
        if st.intersection(c) == c:
            letters[2] = set([st])
            letters[5].remove(st)

    bcdf = letters[4].pop()
    letters[4].add(bcdf)
    for st in letters[9]:
        if st.intersection(bcdf) == bcdf:
            letters[9] = set([st])
            letters[0].remove(st)
    num = ''
    for i in range(11, 15):
        entry = frozenset(line[i])
        j = 0
        for decoder in letters:
            popStorage = decoder.pop()
            decoder.add(popStorage)
            if popStorage == entry:
                num += chr(j+48)
            j += 1
    total += int(num)

print(total)
