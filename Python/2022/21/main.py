input = open("input", 'r')
# input = open("sample", 'r')

data = {}
total = 0

for line in input:
    line = line.strip()
    monkey, value = line.split(": ")
    if len(value) > 5:
        m1,op,m2 = value.split(" ")
        data[monkey] = [m1, m2, op]
    else:
        data[monkey] = [int(value)]

def evaluate(monkey, graph):
    if len(graph[monkey]) > 1:
        m1, m2, op = graph[monkey]
        left = evaluate(m1, graph)
        right = evaluate(m2, graph)
        return eval(f"{left}{op}{right}")
    else:
        return graph[monkey][0]

print(evaluate("root", data), end="\n\n")

r1, r2, op = data["root"]
data["root"] = [r1, r2, "=="]

def evaluate2(monkey, graph):
    if len(graph[monkey]) > 1:
        m1, m2, op = graph[monkey]
        left = evaluate(m1, graph)
        right = evaluate(m2, graph)
        return eval(f"{left}{op}{right}")
    else:
        return graph[monkey][0]

print(evaluate("wcnp", data))
data["humn"] = [3876027196100]
print(evaluate("pgnv", data))
print(evaluate("wcnp", data) > evaluate("pgnv", data))
print(evaluate("wcnp", data) == evaluate("pgnv", data))

# for i in range(3876027190000,3876028190000):
#     data["humn"] = [i]
#     if evaluate("root", data):
#         print(i)
#         break
