input = open("input", 'r')

data = []

for line in input:
    data.append(line.rstrip())

number_pos = set()

for i, line in enumerate(data):
    for j, character in enumerate(line):
        if not character.isdigit() and character != '.':
            for x,y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                if data[i+y][j+x].isdigit():
                    number_pos.add((i+y,j+x))

seen_pos = set()
numbers = []

for pos_y,pos_x in number_pos:
    if (pos_y, pos_x) in seen_pos:
        continue
    seen_pos.add((pos_y, pos_x))
    line = data[pos_y]

    start = pos_x
    end = pos_x

    while line[start-1].isdigit():
        start -= 1
        if start-1 < 0:
            break
    while line[end+1].isdigit():
        end += 1
        if end+1 >= len(line):
            break

    for i in range(start,end+1):
        seen_pos.add((pos_y,i))

    numbers.append(int(line[start:end+1]))


print(numbers)

print(sum(numbers))
