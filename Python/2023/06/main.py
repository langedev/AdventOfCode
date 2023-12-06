input = open("input", 'r')

times = input.readline().rstrip().split("   ")[1:]
distances = input.readline().rstrip().split("   ")[1:]
times = [int(time) for time in times if time != '']
distances = [int(dist) for dist in distances if dist != '']

start_speed = 0
acc = 1

record_beaters = []

for time, distance in zip(times, distances):
    scores = []
    for i in range(time):
        speed = i * acc + start_speed
        travel_time = time - i
        scores.append(travel_time * speed)
    passing_scores = [score for score in scores if score > distance]
    record_beaters.append(len(passing_scores))

product = 1

for record in record_beaters:
    product *= record

print(product)

single_time = int("".join([str(time) for time in times]))
single_dist = int("".join([str(dist) for dist in distances]))

scores = []
for i in range(single_time):
    speed = i * acc + start_speed
    travel_time = single_time - i
    scores.append(travel_time * speed)
passing_scores = [score for score in scores if score > single_dist]

print(len(passing_scores))
