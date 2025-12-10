import re

# input files
debug_input_file = "debuginput10.1.txt"
task_input_file = "input.txt"

with open(task_input_file, 'r') as ifp:
    lines = ifp.read().splitlines()
num_input_lines = len(lines)
print(f"Number of Problems in input file: {num_input_lines}")

# split lines into a lights string, a list of button tuples and a list of joltages
lights = []
buttons = []
joltages = []
for i, line in enumerate(lines):
    a = re.findall('\[([^\]]*)', line)[0]
    lights.append([1 if x == '#' else 0 for x in a])

    b = re.findall('\(([^\)]*)', line)
    temp_buttons = []
    for string in b:
        temp_buttons.append(tuple([int(x) for x in string.split(',')]))
    buttons.append(temp_buttons)

    """ignore reading in C for part 1"""
    #c = re.findall('\{([^\}]*)', line)
    #print(type(c), c)
    #print([int(x) for x in c])
    #joltages.append([int(x) for x in c])

#print(lights)
#print(buttons)
#print(joltages)
print(f"Maximum number of buttons in a problem line: {len(max(buttons))}")


def buttons_to_lights(button_list, active_string, num_lights):
    # evaluates the lights for active buttons
    # returns list of ints of 0 (off) and 1 (on)

    # the active button press list must be as long as the number of buttons
    if len(button_list) != len(active_string):
        print(f"Warning, length of button list: {len(button_list)}, and active elements {len(active_string)}")
        return -1
    
    # create list of results
    result = [0]*num_lights
    for button, active in zip(button_list, active_string):
        if active == '1':
            for light_id in button:
                result[light_id] += 1

    # Modulus of all results gives on or off states
    for i, x in enumerate(result):
        result[i] = x % 2

    return result

# calculate minimum number of button presses needed to get desired lights, starting from zeros.
# pressing a button twice is useless, as it acts like no press.
# iterating over every combination of button presses would be (2^m - 1), doable for 9 buttons
sum_of_min_presses = 0
for light, button in zip(lights, buttons):
    # intialise minimum result with very high value, and number of buttons and lights
    min_presses = 10e9
    num_buttons = len(button)
    num_lights = len(light)

    # initialise matrix of active buttons
    active_matrix = 0b01
    result_found = False

    # loop over every possible button combination, expressed as a binary number
    for i in range(2**num_buttons - 1):
        current_active = f"{active_matrix:0{num_buttons}b}"
        #print(current_active)
        result = buttons_to_lights(button, current_active, num_lights)

        # if solution correct, make new min. number of guesses if lower than before
        if result == light:  
            result_found = True
            if current_active.count('1') < min_presses:
                min_presses = current_active.count('1')
        
        # increment binary representation of active buttons
        active_matrix += 1

    # Warning in case the buttons cannot produce the required combination of lights
    if result_found == False:
        print(f"Warning! No results found for light: {light}, button: {button}")
    
    # sum up the final result
    sum_of_min_presses += min_presses

print(f"Sum of minimum number of buttons needed: {sum_of_min_presses}")

