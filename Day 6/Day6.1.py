total_sum = 0
import math

with open("input.txt", 'r') as ifp:
    input = ifp.read().splitlines()
data = [line.split() for line in input[:-1]]
for i, line in enumerate(data):
    data[i] = [int(x) for x in line]
# transpose matrix to simplify loop
data = zip(*data)
operators = input[-1].split()

for i, line in enumerate(data):
    if operators[i] == '+':
        total_sum += sum(line)
    else:
        total_sum += math.prod(line)
print(total_sum)