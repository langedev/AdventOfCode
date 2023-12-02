input = open("input", 'r')

data = []

for line in input:
    values = line.rstrip().split(": ")[1]
    rounds = values.split("; ")
    rounds = [rnd.split(", ") for rnd in rounds]
    this_game = []
    for rnd in rounds:
        this_round = []
        for game in rnd:
            vals = game.split(" ")
            this_round.append(vals)
        this_game.append(this_round)
    data.append(this_game)

valid_games = set([i+1 for i in range(len(data))])

for i, game in enumerate(data):
    for rnd in game:
        for num, color in rnd:
            if color == "red" and int(num) > 12:
                if i+1 in valid_games:
                    valid_games.remove(i+1)
            if color == "green" and int(num) > 13:
                if i+1 in valid_games:
                    valid_games.remove(i+1)
            if color == "blue" and int(num) > 14:
                if i+1 in valid_games:
                    valid_games.remove(i+1)

print(sum(list(valid_games)))

# Part 2

power_sets = []

for i, game in enumerate(data):
    min_red = 0
    min_blue = 0
    min_green = 0
    for rnd in game:
        for num, color in rnd:
            if color == "red":
                min_red = max(min_red, int(num))
            if color == "green":
                min_green = max(min_green, int(num))
            if color == "blue":
                min_blue = max(min_blue, int(num))
    power_sets.append(min_blue*min_red*min_green)

print(sum(power_sets))
