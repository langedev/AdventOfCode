import math

input = open("input", 'r')

data = []

for line in input:
    line = line.rstrip()
    data.append([int(value) for value in line.split(" ")])

next_values = []

def getSubSequence(seq):
    new_seq = [y - x for x,y in zip(seq, seq[1:])]
    for item in new_seq:
        if item != 0:
            return getSubSequence(new_seq) + new_seq[-1]
    return 0

for sequence in data:
    next_values.append(getSubSequence(sequence) + sequence[-1])

print(sum(next_values))

prev_values = []

def getSubSequence2(seq):
    new_seq = [y - x for x,y in zip(seq, seq[1:])]
    for item in new_seq:
        if item != 0:
            return new_seq[0] - getSubSequence2(new_seq)
    return 0

for sequence in data:
    prev_values.append(sequence[0] - getSubSequence2(sequence))

print(sum(prev_values))
