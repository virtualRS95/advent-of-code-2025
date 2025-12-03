# input files
task_input_file = "input.txt"
#task_input_file = "debug_input_2.txt"
n_batteries_1 = 2
n_batteries_2 = 12

def calc_largest_joltage(line, n_batteries):
    """Returns the largest number that can be built from the ordered digits in the line
    Does not work if n_batteries is larger than the number of digits in line"""
    # remove newline char \n
    values = list(line)[:-1]
    
    # find largest number that is before the last element
    digits = [0]*n_batteries
    indices = [0]*n_batteries

    # find first digit because it limits the range for the next search
    digits[0] = max(values[:-(n_batteries-1)]) # leave (n_batteries-1) elements values to get valid number
    indices[0] = values.index(digits[0])
    
    # repeat for the remaining digits
    for i in range(1, n_batteries):
        # bruh why is python like this, i want to do a[:-0] if the remaining number is forced...
        limiter = -(n_batteries-i-1)
        if limiter == 0: limiter = None
        
        digits[i] = max(values[indices[i-1]+1:limiter]) # leave (n_batteries-1) elements values to get valid number
        indices[i] = values[indices[i-1]+1:].index(digits[i])+indices[i-1]+1
        
    # calculate final decimal number
    joltage = 0
    for i, digit in enumerate(reversed(digits)):
        joltage += int(digit) * 10**i
    # print(f"Joltage calculated: {joltage}")
    return joltage

sum_joltage1 = 0
sum_joltage2 = 0

with open(task_input_file) as ifp:
    lines = ifp.readlines()

for line in lines:
    sum_joltage1 += calc_largest_joltage(line, 2)
    sum_joltage2 += calc_largest_joltage(line, 12)

print(f"The highest achievable joltage1 is: {sum_joltage1}")
print(f"The highest achievable joltage2 is: {sum_joltage2}")