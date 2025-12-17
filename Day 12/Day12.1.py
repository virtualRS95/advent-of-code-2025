# This is it, Day 12, the final frontier
import re

debug_input_file = "debuginput12.txt"
task_input_file = "input.txt"

with open(task_input_file, 'r') as ifp:
    data = ifp.read().split('\n\n')

# make list of available blocks. Each block is defined as a set of indices from top left to bottom right, by rows
block_templates = data[:-1]
for i, block in enumerate(block_templates):
    # create temporary list with location IDs (from 0 top left, 2 top right, ..  to 8 bottom right)
    block_temp = []
    # skip line 1 (2 char + 1 newline)=
    for y, line in enumerate(block[3:].splitlines()):
        for x, char in enumerate(line):
             if char == '#':
                 block_temp.append(3*y + x)
    block_templates[i] = block_temp

# convert list of problems into list of x, y size and number of building blocks
problems = data[-1].splitlines()
for i, problem in enumerate(problems):
    problems[i] =  [int(x) for x in re.findall('[0-9]+', problem)]

# keep track of results
num_unsolveable = 0
unsolveable_problems = set()

# find all obviously unsolveable problems (more block tiles than field tiles): 
print(f"Number of problems: {len(problems)}")
challenging_problems = []
for problem in problems:
    field_area = problem[0] * problem[1]
    sum_block_area = 0
    for block_ID, block_num in enumerate(problem[2:]):
        sum_block_area += block_num * len(block_templates[block_ID])    
    if sum_block_area > field_area:
        num_unsolveable += 1
    else:
        challenging_problems.append(problem)
print(f"Number of definitely unsolveable: {num_unsolveable}")

# find if any problems are trivially solveable without block overlapping
num_trivially_solvable = 0
for problem in problems:
    field_area = (problem[0]//3) * (problem[1]//3) * 9 # check smallest area that can contain all parts without overlap
    sum_block_area = 0
    for block_num in problem[2:]:
        sum_block_area += block_num * 9
    if sum_block_area <= field_area:
        num_trivially_solvable += 1
print(f"Number of trivially solvable problems: {num_trivially_solvable}")
print(f"Number of challenging problems: {len(problems) - num_trivially_solvable - num_unsolveable}")