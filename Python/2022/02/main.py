input = open("input", 'r')
#input = open("sample", 'r')

data = []

score1 = 0
score2 = 0

win = 6
draw = 3
lose = 0

for line in input:
    split = line.split(" ")
    elf = split[0]
    you = split[1].strip()

    # Part 1
    if you == "X":
        score1 += 1
        if elf == "A":
            score1 += draw
        if elf == "B":
            score1 += lose
        if elf == "C":
            score1 += win
    elif you == "Y":
        score1 += 2
        if elf == "A":
            score1 += win
        if elf == "B":
            score1 += draw
        if elf == "C":
            score1 += lose
    elif you == "Z":
        score1 += 3
        if elf == "A":
            score1 += lose
        if elf == "B":
            score1 += win
        if elf == "C":
            score1 += draw

    # Part 2
    if you == "X":
        score2 += lose
        if elf == "A":
            score2 += 3
        if elf == "B":
            score2 += 1
        if elf == "C":
            score2 += 2
    elif you == "Y":
        score2 += draw
        if elf == "A":
            score2 += 1
        if elf == "B":
            score2 += 2
        if elf == "C":
            score2 += 3
    elif you == "Z":
        score2 += win
        if elf == "A":
            score2 += 2
        if elf == "B":
            score2 += 3
        if elf == "C":
            score2 += 1


print(score1)
print(score2)
