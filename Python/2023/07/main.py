import functools

input = open("input", 'r')

data = []

for line in input:
    line = line.rstrip()
    hand, bid = line.split(" ")

    data.append({
        "hand": hand,
        "bid": int(bid)
    })

def getHandValue(hand):
    count = {}
    max_card = ""
    for card in hand:
        if card != "J":
            max_card = card
        if card in count:
            count[card] += 1
        else:
            count[card] = 1
    if "J" in count and count["J"] == 5:
        return 6
    if "J" in count and count["J"] != 0:
        for card in count:
            if card == "J":
                continue
            if count[card] > count[max_card]:
                max_card = card
        count[max_card] += count["J"]
        del count["J"]
    distincts = len(count)
    rank = 0
    if distincts == 1: # 5ok
        rank = 6
    elif distincts == 2: #4ok, fh
        num_cards = count[max_card]
        if num_cards == 4 or num_cards == 1:
            rank = 5
        else:
            rank = 4
    elif distincts == 3: # tk, tp
        rank = 2
        for card in count:
            if count[card] == 3:
                rank = 3
                break
    elif distincts == 4: # op
        rank = 1
    else: # high card
        rank = 0

    return rank

for hand in data:
    hand["rank"] = getHandValue(hand['hand'])

def convertCard(card):
    if card.isdigit():
        return int(card)
    elif card == "T":
        return 10
    elif card == "J":
        return 1
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14

def compare(h1, h2):
    if h1["rank"] > h2["rank"]:
        return 1
    if h1["rank"] < h2["rank"]:
        return -1
    for c1, c2 in zip(h1["hand"],h2["hand"]):
        c1 = convertCard(c1)
        c2 = convertCard(c2)
        if c1 > c2:
            return 1
        if c1 < c2:
            return -1
    return 0

data_s = sorted(data, key=functools.cmp_to_key(compare))

total = 0

for i, card in enumerate(data_s):
    total += (i+1) * card["bid"]

print(total)
