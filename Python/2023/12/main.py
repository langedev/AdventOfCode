import math

input = open("input", 'r')

data = []

for i, line in enumerate(input):
    line = line.rstrip()
    springs, groups = line.split(" ")
    data.append((springs + ".", [int(v) for v in groups.split(",")]))

arrangements = []

SS = {}
def getArrangements(springs, groups, spring, group, length):
    if spring == len(springs):
        if group == len(groups): # Valid solution
            return 1
        return 0

    pos = (spring, group, length)
    if pos in SS:
        return SS[pos]

    arrangements = 0
    if springs[spring]=="." or springs[spring]=="?":
        if length == 0:
            arrangements += getArrangements(springs, groups, spring+1,
                                            group, length)
        elif group < len(groups) and groups[group] == length:
            arrangements += getArrangements(springs, groups, spring+1,
                                            group+1, 0)
    if springs[spring]=="#" or springs[spring]=="?":
        arrangements += getArrangements(springs, groups, spring+1,
                                        group, length+1)
    SS[pos] = arrangements
    return arrangements

for springs, groups in data:
    arrangements.append(getArrangements(springs, groups, 0, 0, 0))
    SS = {}

print(sum(arrangements))

data2 = [("?".join([springs[:-1]] * 5) + ".", groups * 5)
         for springs, groups in data]

print(data2[0])

arrangements = []

for springs, groups in data2:
    arrangements.append(getArrangements(springs, groups, 0, 0, 0))
    SS = {}

print(sum(arrangements))
