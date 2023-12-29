
input = open("input", 'r').read().rstrip()

data = input.split(",")

total = []

def hash(cv, inp):
    for char in inp:
        cv += ord(char)
        cv *= 17
        cv %= 256
    return cv

for inp in data:
    total.append(hash(0, inp))

print(sum(total))

boxes = [{} for _ in range(256)]

for inp in data:
    if inp[-1] == "-":
        label = inp[:-1]
        box = hash(0, label)
        if label in boxes[box]:
            del boxes[box][label]
    else:
        label, fl = inp.split("=")
        box = hash(0, label)
        boxes[box][label] = int(fl)

print(boxes)

total2 = []

for i, box in enumerate(boxes):
    for slot, fl in enumerate(box.values()):
        total2.append((i+1)*(slot+1)*fl)

print(sum(total2))
