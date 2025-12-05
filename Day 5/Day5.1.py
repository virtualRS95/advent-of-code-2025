from time import perf_counter

# load test and task files
test_input_file = "debug_file_1.txt"
task_input_file = "input.txt"
# Define font formatting codes for easy use
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'

# time code execution
t0 = perf_counter()

# load test and results file
def get_fresh_ids(input_file):
    with open(input_file, 'r') as ifp:
        data = ifp.read().splitlines()
    
    # check if this file is a test, which includes expected results
    test_results = []
    while "result" in data[-1]:
        test_results.append(int(data.pop().split()[-1]))    
    #print(f"The expected results for file {input_file} are {test_results}.")
    t1 = perf_counter()

    # split data into ranges of fresh ingredients and available ingredients (separated by empty line)
    split_idx = data.index("")
    fresh = data[:split_idx] # make 2x int tuple
    for i in range(len(fresh)):
        a, b = fresh[i].split('-')
        fresh[i] = (int(a), int(b))
    ingredients = list(set([int(x) for x in data[split_idx+1:]])) # make unique int list
    t2 = perf_counter()

    # sort the lists ascending and merge overlaps
    fresh.sort()
    ingredients.sort()
    t3 = perf_counter()

    # merge overlapping ranges by comparing and modifying previous range
    merged = [fresh[0]]
    for curr_start, curr_end in fresh[1:]:
        prev_start, prev_end = merged[-1]
        if curr_start <= prev_end:
            # make sure to pick the larger end range in case current is contained in previous
            merged[-1] = (prev_start, max(prev_end, curr_end))
        else:
            merged.append((curr_start, curr_end))
    t4 = perf_counter()
    
    # count how many ingredient IDs are contained in the merged ranges
    fresh_ingredients = 0
    skip_ranges = 0
    for iid in ingredients:
        for num_range in merged[skip_ranges:]:
            if num_range[0] <= iid <= num_range[1]:
                fresh_ingredients += 1
                break
            elif iid > num_range[1]:
                skip_ranges += 1
                #print(f"Number: {iid}, skipping range {num_range} from now on.")
    t5 = perf_counter()

    # output test or full result:
    if test_results == []:
        print(f"Number of fresh ingredients: {fresh_ingredients}")
    else:
        for test_result in test_results:
            if fresh_ingredients == test_result:
                print(f"{BOLD}{GREEN}PASS{RESET}: Fresh ingredients: {fresh_ingredients}, expected result: {test_result}")
            else:
                print(f"{BOLD}{RED}FAIL{RESET}: Fresh ingredients: {fresh_ingredients}, expected result: {test_result}")

    

get_fresh_ids(test_input_file)
get_fresh_ids(task_input_file)

t6 = perf_counter()
print(f"Total execution time: {(t6-t0)*1000:3f} ms.")