# input files
task_input_file = "input.txt"
#debug_input_file = "debuginput1.txt"
"""Can be expanded to read expected solutions from test files for comparison"""

# define functions to create and manipulate the play field
def open_testcase (file_name, debug = False): 
    with open(file_name) as ifp:
        lines = ifp.read().splitlines()
        """expected_result1 = None
        #expected_result2 = None
        #if debug:
        #    expected_result2 = lines.pop()
        #    expected_result1 = lines.pop()"""
        # assume playing field is rectangular
        n_rows = len(lines)
        n_cols = len(lines[0])
        print(f"The input play field is of size {n_rows}x{n_cols}")
    return lines, n_rows, n_cols #, expected_result1, expected_result2

def print_field(field):
    """A nicer way to output the field"""
    for row in field:
        print(list(str(val) for val in row))

def add_ghost_cells(lines):
    """Add ghost cells around the playfield"""
    field = [list(line) for line in lines]
    for line in field:
        line.insert(0, ".")
        line.append(".")
    field.insert(0, ["."]*(n_cols+2))
    field.append(["."]*(n_cols+2))
    return field

def count_accessible_rolls(field, n_rows, n_cols):
    """Counts all accessible rolls on the field"""
    num_accessible_rolls = 0
    # Iterate over the playfield and replace rolls (@) with number of neighbours
    for i in range(1, n_rows+1):
        for j in range(1, n_cols+1):
            # subtract roll itself before counting every @ or number for the 3x3 area around i,j
            num_neighbours = -1
            item = field[i][j]
            if field[i][j] != ".":
                for si in range(i-1, i+2):
                    for sj in range(j-1, j+2):
                        if field[si][sj] != ".":
                            num_neighbours += 1
                # replace roll symbol (@) by the number of neighbours
                field[i][j] = num_neighbours
                if num_neighbours < 4:
                    num_accessible_rolls += 1

    #print(num_accessible_rolls)
    return field, num_accessible_rolls
        
def remove_accessible_rolls(field, n_rows, n_cols):
    """returns field with numbers below 4 replaced with '.' """
    for i in range(1, n_rows+1):
        for j in range(1, n_cols+1):
            if type(field[i][j]) == int and field[i][j] < 4:
                field[i][j] = "."
    return field

lines, n_rows, n_cols, = open_testcase(task_input_file, False)
field = add_ghost_cells(lines)

# count first batch of accessible rolls rolls:
field, num_accessible_rolls = count_accessible_rolls(field, n_rows, n_cols)
num_accessible_rolls1 = num_accessible_rolls
num_accessible_rolls2 = num_accessible_rolls

# remove and repeat until no more rolls left.
while num_accessible_rolls > 0:
    field = remove_accessible_rolls(field, n_rows, n_cols)
    field, num_accessible_rolls = count_accessible_rolls(field, n_rows, n_cols)
    num_accessible_rolls2 += num_accessible_rolls

#print_field(field)
print(f"Number of accessible rolls (1): {num_accessible_rolls1}.")
print(f"Number of accessible rolls (2): {num_accessible_rolls2}.")
