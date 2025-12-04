# input files
task_input_file = "input.txt"
# task_input_file = "debug_input_2.txt"
n_batteries_1 = 2
n_batteries_2 = 12

def calc_largest_joltage(num_list, n_batteries):
    """Returns the largest number that can be built from the ordered digits in the line.
    Crashes if num_list has fewer than n_batteries elements.""" 
    # create empty array for the chosen digits and their indices in num_list
    digits = [0]*n_batteries
    indices = [0]*n_batteries

    # find first digit because it limits the range for the next search
    digits[0] = max(num_list[:-(n_batteries-1)]) # leave (n_batteries-1) elements num_list to get valid number
    indices[0] = num_list.index(digits[0])
    
    # repeat for the remaining digits
    for i in range(1, n_batteries):
        # bruh why is python like this, i want to do a[:-0] if the remaining number is forced...
        limiter = -(n_batteries-i-1)
        if limiter == 0: limiter = None
        
        digits[i] = max(num_list[indices[i-1]+1:limiter]) # leave (n_batteries-1) elements num_list to get valid number
        indices[i] = num_list[indices[i-1]+1:].index(digits[i])+indices[i-1]+1
        
    # return final decimal number by joining digits
    return int("".join(str(x) for x in digits))

sum_joltage1 = 0
sum_joltage2 = 0

with open(task_input_file) as ifp:
    lines = ifp.read().splitlines()

for line in lines:
    sum_joltage1 += calc_largest_joltage(list(line), 2)
    sum_joltage2 += calc_largest_joltage(list(line), 12)

print(f"The highest achievable joltage1 is: {sum_joltage1}")
print(f"The highest achievable joltage2 is: {sum_joltage2}")