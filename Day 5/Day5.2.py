from time import perf_counter

# load test and task files
test_input_file = "debug_file_2.txt"
task_input_file = "input.txt"
big_input_file = "KtGx.txt"
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
    t00 = perf_counter()

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
    ingredients = [int(x) for x in data[split_idx+1:]] # make unique int list
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
    print(f"time spent up to t4: {t4-t00}")

    # count the numer of valid IDs in the merged ranges
    num_fresh_ids = 0
    for curr_start, curr_end in merged:
        num_fresh_ids += (curr_end-curr_start) + 1 # +1 to include final value
    
    # count how many ingredient IDs are contained in the merged ranges
    fresh_ingredients = 0
    skip_ranges = 0
    for iid in ingredients:
        for i in range(skip_ranges, len(merged)):#[skip_ranges:]:
            num_range = merged[i]
            if iid < num_range[0]:
                break
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
        print(f"Number of valid fresh IDs: {num_fresh_ids}")
    else:
        # check part 1 solution
        if fresh_ingredients == test_results[0]:
            print(f"{BOLD}{GREEN}PASS{RESET}: Fresh ingredients: {fresh_ingredients}, expected result: {test_results[0]}")
        else:
            print(f"{BOLD}{RED}FAIL{RESET}: Fresh ingredients: {fresh_ingredients}, expected result: {test_results[0]}")

        # check part 2 solution
        if num_fresh_ids == test_results[1]:
            print(f"{BOLD}{GREEN}PASS{RESET}: Num valid IDs: {num_fresh_ids}, expected result: {test_results[1]}")
        else:
            print(f"{BOLD}{RED}FAIL{RESET}: Num valid IDs: {num_fresh_ids}, expected result: {test_results[1]}")

    

get_fresh_ids(test_input_file)
get_fresh_ids(task_input_file)
get_fresh_ids(big_input_file)

t6 = perf_counter()
print(f"Total execution time: {(t6-t0)*1000:3f} ms.")