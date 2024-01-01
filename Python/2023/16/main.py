# y, x
# j, i

input = open("input", 'r')#.read().rstrip()

data = []

for line in input:
    data.append(list(line.rstrip()))


def printenergized(pos, energized):
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            if pos == (j,i):
                print("*", end="")
            elif (j, i) in energized:
                print("#", end="")
            else:
                print(char, end="")
        print()
    print()

def beam(split_stack):
    assert(len(data) == len(data[0]))
    energized = set()
    prevpos = set()
    while len(split_stack) > 0:
        pos, dr = split_stack.pop()
        while min(pos) >= 0 and max(pos) < len(data):
            energized.add(pos)
            if pos+dr in prevpos:
                break
            else:
                prevpos.add(pos+dr)
            # printenergized(pos, energized)
            curr_space = data[pos[0]][pos[1]]
            if curr_space == "/":
                dr = (-dr[1], -dr[0])
            elif curr_space == "\\":
                dr = (dr[1], dr[0])
            elif curr_space == "-" and dr[0] != 0:
                split_stack.append(((pos[0], pos[1]+1),(0, 1)))
                split_stack.append(((pos[0], pos[1]-1),(0,-1)))
                break
            elif curr_space == "|" and dr[1] != 0:
                split_stack.append(((pos[0]+1, pos[1]),( 1,0)))
                split_stack.append(((pos[0]-1, pos[1]),(-1,0)))
                break
            pos = tuple(sum(elems) for elems in zip(pos,dr))
    return energized

split_stack = [((0,0),(0,1))]
energized = beam(split_stack)
print(len(energized))

energizes = []

# Left & Right
for dr, x in zip([1, -1], [0, len(data[0])-1]):
    for j in range(len(data)):
        split_stack = [((j,x),(0,dr))]
        energizes.append(len(beam(split_stack)))

# Top & Bottom
for dr, y in zip([1, -1], [0, len(data)-1]):
    assert(len(data[-1]) == len(data[0]))
    for i in range(len(data[0])):
        split_stack = [((y,i),(dr,0))]
        energizes.append(len(beam(split_stack)))

print(max(energizes))
