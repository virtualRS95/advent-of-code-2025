initial_number = 50
input_file = "input.txt"

"""
Task 1 Iteratively add instructions to initial number and count intermediate zeros
Task 2: Also count every time zero is passed during an instruction
    50+60 --> 110      Add 1
    50-50 --> 0        Add 1
    However: 
    50+150 --> 200     Add only 2 (1 for rotation past 0 and 1 for landing on it)
    50-150 --> -100    Add only 2
"""

# open the input file
with open(input_file) as ifp:
    instructions = ifp.readlines()

# replace L and R in the instructions negative and positive integers
for i in range(len(instructions)):
    if instructions[i][0] == "L":
        instructions[i] = -1* int(instructions[i][1:])
    else: instructions[i] = int(instructions[i][1:])

# initialising the results counters and the number counter
zeros_1 = 0
zeros_2 = 0
number = initial_number

for instruction in instructions:
    # Use inverse calculation for negative instructions to avoid issues with floor division
    # Mod 100 is needed because the inverse number line yields 100 instead of 0 in some cases
    if instruction < 0:
        number = (100 - number) % 100 

    # Calculate raw_number after incrementation and modulo it
    raw_number = number + abs(instruction)
    number = raw_number % 100
    # Task 1: If we land on zero, increment zeros1
    if number == 0:
        zeros1 += 1
    
    # Use floor division on raw and modulo number to find how many times we passed n*100
    times_passed_zero = abs(raw_number//100 - number//100)
    zeros_2 += times_passed_zero

    # Invert the number line back to default.
    if instruction < 0:
        number = (100 - raw_number) % 100 

    # Edge case where the dial is not turned in an instruction.
    if instruction == 0 and number == 0:
        zeros2 += 1

print(f"The number of times zero was hit is {zeros1} and the number of times a zero was passed or hit is {zeros2}")