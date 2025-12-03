# input files
task_input_file = "input.txt"

with open(task_input_file) as ifp:
    lines = ifp.readlines()

sum_joltage = 0
# Find the largest joltage for every line (bank)
for line in lines:
    values = list(line)[:-1] # remove newline char \n
    # find largest number that is before the last element
    first_digit = max(values[:-1])
    index_first_digit = values.index(first_digit)
    # search to the right of the first highest first digit for the highest second digit
    second_digit = max(values[index_first_digit+1:])
    #print(f"values: {values}, first_digit: {first_digit}, index_first: {index_first_digit}, second_digit: {second_digit}")
    sum_joltage += (int(first_digit)*10 + int(second_digit))

print(f"The highest achievable joltage is: {sum_joltage}")