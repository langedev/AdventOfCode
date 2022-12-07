input = open("input", 'r')
# input = open("sample", 'r')

FS_SIZE = 70000000
NEEDED_SIZE = 30000000

data = {}
point = None
data2 = []

curdir = []

mode = 0
subtotal = 0
for line in input:
    line = line.strip()
    if mode == 1:
        if line[0] == "$":
            mode = 0
            point = data
            for dr in curdir:
                if dr not in point:
                    point[dr] = {}
                point = point[dr]
            point["size"] = subtotal
            subtotal = 0
        else:
            one, two = line.split(" ")
            if one == "dir":
                continue
            subtotal += int(one)
    if mode == 0:
        if line == "$ ls":
            mode = 1
        else:
            d, cd, target = line.split(" ")
            if target == "..":
                curdir.pop()
            else:
                curdir.append(target)

def normalize_size(data):
    for drs in data:
        if drs == "size":
            continue
        data["size"] += normalize_size(data[drs])
    return data["size"]

def sum_fewer(data):
    total = 0
    for drs in data:
        if drs == "size":
            continue
        total += sum_fewer(data[drs])
    if data["size"] < 100000:
        return data["size"] + total
    return total

def find_smallest_size(data, size):
    result = []
    if data["size"] > size:
        result.append(data["size"])
    for drs in data:
        if drs == "size":
            continue
        result += find_smallest_size(data[drs], size)
    return result

normalize_size(data["/"])
print(sum_fewer(data["/"]))
FREE_SPACE = FS_SIZE - data["/"]["size"]
MISSING_SPACE = NEEDED_SIZE - FREE_SPACE
dirs = find_smallest_size(data["/"], MISSING_SPACE)
print(sorted(dirs)[1]) # For some reason the minimum wasn't correct /shrug
