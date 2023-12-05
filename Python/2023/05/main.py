input = open("input", 'r')

mode = 0
seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

for line in input:
    if line.rstrip() == "":
        continue
    if line.startswith("seeds:"):
        seeds = line.rstrip().split(": ")[1].split(" ")
        continue
    elif line.startswith("seed-to-soil"):
        mode = 1
        continue
    elif line.startswith("soil-to-fertilizer"):
        mode = 2
        continue
    elif line.startswith("fertilizer-to-water"):
        mode = 3
        continue
    elif line.startswith("water-to-light"):
        mode = 4
        continue
    elif line.startswith("light-to-temperature"):
        mode = 5
        continue
    elif line.startswith("temperature-to-humidity"):
        mode = 6
        continue
    elif line.startswith("humidity-to-location"):
        mode = 7
        continue

    if mode == 1:
        seed_to_soil.append(line.rstrip().split(" "))
    elif mode == 2:
        soil_to_fertilizer.append(line.rstrip().split(" "))
    elif mode == 3:
        fertilizer_to_water.append(line.rstrip().split(" "))
    elif mode == 4:
        water_to_light.append(line.rstrip().split(" "))
    elif mode == 5:
        light_to_temperature.append(line.rstrip().split(" "))
    elif mode == 6:
        temperature_to_humidity.append(line.rstrip().split(" "))
    elif mode == 7:
        humidity_to_location.append(line.rstrip().split(" "))

def findIn(value, converters):
    for converter in converters:
        dest, source, length = converter
        source = int(source)
        length = int(length)
        dest = int(dest)
        if value >= source and value <= source + length - 1:
            diff = value - source
            return dest + diff

    return value

locations = []

for seed in seeds:
    soil = findIn(int(seed), seed_to_soil)
    fertilizer = findIn(soil, soil_to_fertilizer)
    water = findIn(fertilizer, fertilizer_to_water)
    light = findIn(water, water_to_light)
    temperature = findIn(light, light_to_temperature)
    humidity = findIn(temperature, temperature_to_humidity)
    location = findIn(humidity, humidity_to_location)
    locations.append(location)

print(min(locations))

locations = []

for i in range(len(seeds) // 2):
    start = int(seeds[i*2])
    stride = int(seeds[i*2+1])
    print(i)
    for seed in range(start, start+stride):
        soil = findIn(seed, seed_to_soil)
        fertilizer = findIn(soil, soil_to_fertilizer)
        water = findIn(fertilizer, fertilizer_to_water)
        light = findIn(water, water_to_light)
        temperature = findIn(light, light_to_temperature)
        humidity = findIn(temperature, temperature_to_humidity)
        location = findIn(humidity, humidity_to_location)
        locations.append(location)

print(min(locations))
