total_sum = 0
import math

with open("input.txt", 'r') as ifp:
    input = ifp.read().splitlines()
    # find the columns in each line that are continuous to find the fixed with of cells.
#data = [line.split() for line in input[:-1]]
data = input[:-1]
n_cols = len(data) #terminology inverted
n_rows = len(data[0])
#print(f"n_cols {n_cols}, n_rows {n_rows}")
data = zip(*input[:-1])
data = [list(row) for row in data]
operators = input[-1].split()
print(data)

numbers = []
operator_count = 0
for i in range(n_rows):
    number_digits = []
    empty_column = True
    for j in range(n_cols):
        #print(data[i][j])
        if data[i][j] != " ":
            number_digits.append(data[i][j])
            empty_column = False
    if empty_column == False:
        numbers.append(int("".join(number_digits)))
    else: 
        #print(f"numbers: {numbers}, operator: {operators[operator_count]}")
        if operators[operator_count] == "+":
            print(f"to add: {sum(numbers)}")
            total_sum += sum(numbers)
        else:
            print(f"to add: {math.prod(numbers)}")
            total_sum += math.prod(numbers)
        operator_count += 1
        number_digits = []
        numbers = []
if operators[operator_count] == "+":
    print(f"to add: {sum(numbers)}")
    total_sum += sum(numbers)
else:
    print(f"to add: {math.prod(numbers)}")
    total_sum += math.prod(numbers)


print(total_sum)