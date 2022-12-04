input = open("input", 'r')
# input = open("sample", 'r')

data = []
data2 = []

total = 0
total2 = 0

for line in input:
    pair = line.strip().split(",")
    r1 = pair[0].split("-")
    r2 = pair[1].split("-")

    if int(r1[0]) <= int(r2[0]) and int(r1[1]) >= int(r2[1]):
        total += 1
    elif int(r2[0]) <= int(r1[0]) and int(r2[1]) >= int(r1[1]):
        total += 1

    for i in range(int(r1[0]),int(r1[1])+1):
        for j in range(int(r2[0]),int(r2[1])+1):
            if i == j:
                total2 += 1
                break
        if i == j:
            break


print(total)
print(total2)
