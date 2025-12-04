# input files
task_input_file = "input.txt"
#task_input_file = "debug_input_2.txt"
n_batteries_1 = 2
n_batteries_2 = 12

def calc_largest_joltage(num_list, n_batteries):
    """Returns the largest number that can be built from the ordered digits in the line.
    Crashes if num_list has fewer than n_batteries elements.""" 
    # create empty string array for the chosen digits
    digits = []

    # Count down the number of batteries left to choose, which limits the search space for max()
    for batteries_left in range(n_batteries, 0, -1):
        digit = max(num_list[:len(num_list)-batteries_left+1])
        digits.append(digit)
        # slice off invalid numbers from num_list
        num_list = num_list[num_list.index(digit)+1:]
    return int("".join(digits))

sum_joltage1 = 0
sum_joltage2 = 0

with open(task_input_file) as ifp:
    lines = ifp.read().splitlines()

for line in lines:
    sum_joltage1 += calc_largest_joltage(list(line), 2)
    sum_joltage2 += calc_largest_joltage(list(line), 12)

print(f"The highest achievable joltage1 is: {sum_joltage1}")
print(f"The highest achievable joltage2 is: {sum_joltage2}")