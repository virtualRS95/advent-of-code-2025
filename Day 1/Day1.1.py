initial_number = 50
input_file = "input.txt"

# open the input file
with open(input_file) as ifp:
    instructions = ifp.readlines()

# replace L and R in the instructions with - and +
for i in range(len(instructions)):
    if instructions[i][0] == "L":
        instructions[i] = -1* int(instructions[i][1:])
    else: instructions[i] = int(instructions[i][1:])

# iteratively add instructions to initial number and count the zero results
zeros = 0
number = initial_number
for instruction in instructions:
    # modulo operator because number range is 0-99., 0 minus 5 --> 95
    number = (number+instruction) % 100
    if number == 0:
        zeros += 1

print(f"The number of zeros is {zeros}")