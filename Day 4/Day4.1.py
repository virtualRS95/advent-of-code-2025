# input files
task_input_file = "input.txt"
#debug_input_file = "debuginput1.txt"

def open_testcase (file_name, debug = False): 
    with open(file_name) as ifp:
        lines = ifp.read().splitlines()
        expected_result = None
        if debug:
            expected_result = lines.pop()
        # assume playing field is rectangular
        n_rows = len(lines)
        n_cols = len(lines[0])
        print(f"The input play field is of size {n_rows}x{n_cols}")
    return lines, n_rows, n_cols, expected_result

def print_field(field):
    for row in field:
        print(list(str(val) for val in row))

#lines, n_rows, n_cols, expected_result = open_testcase(debug_input_file, True)
lines, n_rows, n_cols, expected_result = open_testcase(task_input_file, False)

# Add ghost cells around the playfield
field = [list(line) for line in lines]
for line in field:
    line.insert(0, ".")
    line.append(".")
field.insert(0, ["."]*(n_cols+2))
field.append(["."]*(n_cols+2))

num_accessible_rolls = 0
# Iterate over the playfield and replace rolls (@) with number of neighbours
for i in range(1, n_rows+1):
    for j in range(1, n_cols+1):
        # subtract roll itself before counting every @ or number for the 3x3 area around i,j
        num_neighbours = -1
        item = field[i][j]
        if field[i][j] == "@":            
            for si in range(i-1, i+2):
                for sj in range(j-1, j+2):
                    #print(f"  Field: {si:3},{sj:3}, {field[si][sj]}, not '.'")
                    if field[si][sj] != ".":
                        num_neighbours += 1
            field[i][j] = num_neighbours

            if num_neighbours < 4:
                num_accessible_rolls += 1

        #print(f"x={i:3}, y={j:3}, item: {item}   neighbours found: {locals().get('num_neighbours', 'N/A'):2}")

print_field(field)
print(f"Number of accessible rolls: {num_accessible_rolls}.")
