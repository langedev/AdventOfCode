from collections import deque as queue
import sys
import time
input = open("input.txt", 'r')

data = []

for line in input:
    row = []
    for character in line:
        if character == '\n':
            continue
        row.append(int(character))
    data.append(row)

def risk_level(point):
    return 1 + point

def check_minimum(columnn, row, data):
    value = data[row][columnn]
    for i in range(row-1, (row+1)+1):
        if i < 0 or i >= len(data):
            continue
        for j in range(column-1,(column+1)+1):
            if j < 0 or j >= len(data[i]):
                continue
            if i == row and j == column:
                continue
            if data[i][j] <= value:
                return False

    return True

def is_valid(vis, row, col, data):
    if row < 0 or col < 0 or row >= len(data) or col >= len(data[row]):
        return False
    if vis[row][col]:
        return False
    if data[row][col] >= 9:
        return False

    return True

dirRow = [-1, 0, 1, 0]
dirCol = [0, 1, 0, -1]

def update_vis(vis, row, column, value):
    for i in vis:
        for j in i:
            if j:
                sys.stdout.write("\N{ESC}[31m")
            else:
                sys.stdout.write("\N{ESC}[34m")
            sys.stdout.write(str(int(j)))
        sys.stdout.write("\n")
    sys.stdout.flush()
    time.sleep(0.1)
    vis[row][column] = value


def calc_basin_size(row, column, data, vis):
    q = queue()

    q.append((row, column))

    update_vis(vis, row, column, True)

    while len(q) > 0:
        location = q.popleft()
        x = location[0]
        y = location[1]

        for i in range(4):
            adj_x = x + dirRow[i]
            adj_y = y + dirCol[i]
            if is_valid(vis, adj_x, adj_y, data):
                q.append((adj_x, adj_y))
                update_vis(vis, adj_x, adj_y, True)
    total = 0
    for r in vis:
        for c in r:
            total += int(c)
    return total


maximums = []
answer = 0

vis = [[False for i in range(len(data[0]))] for i in range(len(data))]
for row in range(0, len(data)):
    previous = 10
    for column in range(0, len(data[row])):
        if previous > data[row][column]:
            if check_minimum(column, row, data):
                if vis[row][column]:
                    previous = data[row][column]
                    continue
                # answer += risk_level(data[row][column])
                size = calc_basin_size(row, column, data, vis)
                maximums.append(size)
        previous = data[row][column]

maximums.sort()
print(maximums[-1]*maximums[-2]*maximums[-3])
