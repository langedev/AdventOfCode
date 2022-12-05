input = open("input", 'r')
# input = open("sample", 'r')

data = [[] for i in range(9)]
data2 = [[] for i in range(9)]

total = 0
total2 = 0


mode = 0


for line in input:
    if line == "\n":
        mode = 1
        continue
    if mode == 0:
        line = line.strip()
        for i in range(0, len(line), 4):
            if line[i] == "[":
                data[i//4].insert(0, line[i+1])
                data2[i//4].insert(0, line[i+1])
    elif mode == 1:
        move, quantity, frm, stackA, to, stackB = line.strip().split(" ")
        for i in range(int(quantity)):
            top = data[int(stackA)-1].pop()
            data[int(stackB)-1].append(top)

        #part 2
        print(line)
        print(data2)
        move = data2[int(stackA)-1][-int(quantity):]
        print(move)
        del data2[int(stackA)-1][-int(quantity):]
        for crate in move:
            data2[int(stackB)-1].append(crate)


for stack in data:
    print(stack.pop(), end="")
print()
for stack in data2:
    print(stack.pop(), end="")
