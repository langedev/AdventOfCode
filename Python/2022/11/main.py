input = open("input", 'r')
# input = open("sample", 'r')
data = []
total = 0

for line in input:
    data.append(line.strip())

divisor = 1
monkeys = []
for line in data:
    if len(line) <= 0:
        continue
    if line[0] == "M":
        monkeys.append({})
    else:
        if line[0] == "S":
            text, items = line.split(": ")
            monkeys[-1]["items"] = [int(item) for item in items.split(", ")]
        elif line[0] == "O":
            formula = line.split("old ")[1]
            op = "+" if formula[0] == "+" else "*"
            num = formula[2:]
            monkeys[-1]["opp"] = (op, num)
        elif line[0] == "T":
            monkeys[-1]["test"] = int(line.split("divisible by ")[1])
            divisor *= monkeys[-1]["test"]
        elif line[3] == "t":
            monkeys[-1]["true"] = int(line.split("monkey ")[1])
        elif line[3] == "f":
            monkeys[-1]["false"] = int(line.split("monkey ")[1])

# inspects = [0 for _ in range(len(monkeys))]
# for r in range(20):
#     # round
#     for m, monkey in enumerate(monkeys):
#         length = len(monkey["items"])
#         inspects[m] += length
#         for i in range(length):
#             item = monkey["items"][0]
#             del monkey["items"][0]
#             value = int(monkey["opp"][1]) if monkey["opp"][1] != "old" else item
#             if monkey["opp"][0] == "*":
#                 item = item * value
#             elif monkey["opp"][0] == "+":
#                 item = item + value

#             item = item // 3

#             if item % monkey["test"] == 0:
#                 monkeys[monkey["true"]]["items"].append(item)
#             else:
#                 monkeys[monkey["false"]]["items"].append(item)

# isorted = sorted(inspects, reverse=True)
# print(isorted[0] * isorted[1])

inspects = [0 for _ in range(len(monkeys))]
for r in range(10000):
    # round
    for m, monkey in enumerate(monkeys):
        length = len(monkey["items"])
        inspects[m] += length
        for i in range(length):
            item = monkey["items"][0]
            del monkey["items"][0]
            value = int(monkey["opp"][1]) if monkey["opp"][1] != "old" else item
            if monkey["opp"][0] == "*":
                item = item * value
            elif monkey["opp"][0] == "+":
                item = item + value

            item = item % divisor

            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)

isorted = sorted(inspects, reverse=True)
print(isorted[0] * isorted[1])
