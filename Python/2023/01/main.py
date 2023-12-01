input = open("input2", 'r')

data = []

for line in input:
    numbers = []
    for i, char in enumerate(line):
        # Part 1
        if char in set("1234567890"):
            numbers.append(char)

        # Part 2
        elif char in set("otfsen"):
            if line[i:i+3] == "one":
                numbers.append("1")
            elif line[i:i+3] == "two":
                numbers.append("2")
            elif line[i:i+5] == "three":
                numbers.append("3")
            elif line[i:i+4] == "four":
                numbers.append("4")
            elif line[i:i+4] == "five":
                numbers.append("5")
            elif line[i:i+3] == "six":
                numbers.append("6")
            elif line[i:i+5] == "seven":
                numbers.append("7")
            elif line[i:i+5] == "eight":
                numbers.append("8")
            elif line[i:i+4] == "nine":
                numbers.append("9")
    # Both
    data.append(int(numbers[0] + numbers[-1]))

print(sum(data))
