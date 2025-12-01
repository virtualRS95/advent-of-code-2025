initial_number = 50
input_file = "input.txt"
# input_file = "debuginput3.txt"

# open the input file
with open(input_file) as ifp:
    instructions = ifp.readlines()

# replace L and R in the instructions with - and +
for i in range(len(instructions)):
    if instructions[i][0] == "L":
        instructions[i] = -1* int(instructions[i][1:])
    else: instructions[i] = int(instructions[i][1:])

"""
Task 1 Iteratively add instructions to initial number and count intermediate zeros
Task 2: Also count every time 0 is passed during an instruction
    50+60 --> 110      Add 1
    50-50 --> 0        Add 1
    However: 
    50+150 --> 200     Add only 2 (1 for rotation past 0 and 1 for landing on it)
    50-150 --> -100    Add only 2
"""
zeros = 0
number = initial_number
for instruction in instructions:
    """
    Instead of executing positive and negative clicks, we invert the number line on the negative,
    which creates a scalar operation without issues of floor/ceiling operations on positive and 
    negative overflows around zero.
    """
    # remember the previous iterations number
    prev_number = number

    # Condition 0: We are on zero and change nothing (this should not happen)
    if instruction == 0 and number == 0:
        zeros += 1

    # Condition 1: The instruction is negative (Left rotation), reverse addition
    # % 100 is needed because in the inverse numbers from 1-100 can exist instead of 0-99
    if instruction < 0:
        number = (100 - number) % 100 

    # (Condition 2): No adjustment needed for positive instructions
    raw_number = number + abs(instruction)
    number = raw_number % 100

    # use floor division to determine how many times we passed or hit 0
    hundreds_raw_number = raw_number//100
    hundreds_number = number//100
    times_passed_zero = abs(hundreds_raw_number-hundreds_number)

    zeros += times_passed_zero

    # Revert back the inverted addition from Condition 1
    if instruction < 0:
        number = (100 - raw_number) % 100 

    print(
        f"debug:\n"
        f"prev_number={prev_number}\n"
        f"instruction={instruction}\n"
        f"Raw_number={raw_number}\n"
        f"number={number}\n"
        f"hundreds_raw_number={hundreds_raw_number}\n"
        f"hundreds_number={hundreds_number}\n"
        f"times_passed_zero={times_passed_zero}\n"
        f"zeros={zeros}\n"
        )
    
print(f"The number of times zero was passed or hit is {zeros}")