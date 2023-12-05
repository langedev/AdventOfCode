input = open("input", 'r')

data = []

for line in input:
    card = line.rstrip().split(": ")[1]
    winning, present = card.split(" | ")
    winning = [int(num) for num in winning.split(" ") if num != ""]
    present = [int(num) for num in present.split(" ") if num != ""]
    data.append({
        "wins": winning,
        "pres": present
    })

total = 0
wins = {card_num: 0 for card_num in range(len(data))}

for i, card in enumerate(data):
    for number in card["pres"]:
        if number in card["wins"]:
            wins[i] += 1
    if wins[i]:
        total += 2 ** (wins[i]-1)

print(total)

cards = {card_num: 1 for card_num in range(len(data))}

print(wins)

for num, count in wins.items():
    for i in range(count):
        cards[num+i+1] += cards[num]

print(cards)

total = 0
for _, count in cards.items():
    total += count

print(total)
