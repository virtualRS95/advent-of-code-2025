from time import perf_counter
import bisect

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
    t00 = perf_counter()
    with open(input_file, 'r') as ifp:
        data = ifp.read().splitlines()
    
    # check if this file is a test, which includes expected results
    test_results = []
    while "result" in data[-1]:
        test_results.append(int(data.pop().split()[-1]))
    t1 = perf_counter()
    print(f"{BOLD}Timing:{RESET} File read in: {(t1-t00):.3f} s.")

    # split data into ranges of fresh ingredients and available ingredients (separated by empty line)
    split_idx = data.index("")
    fresh = data[:split_idx] # make 2x int tuple
    for i in range(len(fresh)):
        a, b = fresh[i].split('-')
        fresh[i] = (int(a), int(b))
    ingredients = list([int(x) for x in data[split_idx+1:]]) # list of integers
    t2 = perf_counter()
    print(f"{BOLD}Timing:{RESET} Split data in ranges: {(t2-t1):.3f} s.")

    # sort the lists ascending and merge overlaps
    fresh.sort()
    ingredients.sort()
    t3 = perf_counter()
    print(f"{BOLD}Timing:{RESET} Sorted both lists: {(t3-t2):.3f} s.")

    # check for duplicate ingredients (not required, duplicates are counted in theory):
    if len(ingredients) != len(set(ingredients)):
        print(f"{RED}No. of ingredients: {len(ingredients)}, No. of unique ingredients: {len(set(ingredients))}.{RESET}")
    else:
        print(f"{GREEN}No. of ingredients: {len(ingredients)}, all are unique.{RESET}")

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
    print(f"{BOLD}Timing:{RESET} Merged fresh ingredient ranges: {(t4-t3):.3f} s.")

    # count the numer of possible valid IDs in the merged ranges
    num_fresh_ids = 0
    for curr_start, curr_end in merged:
        num_fresh_ids += (curr_end-curr_start) + 1 # +1 to include final value
    t4_1 = perf_counter()
    print(f"{BOLD}Timing:{RESET} Counted number of possible valid fresh IDs: {(t4_1-t4):.3f} s.")
    
    # Per range, find the smallest and largest ID that can fit to find how many numbers are valid
    # use binary search O(log n). Don't remove found IDs from future searches because its a O(n), 50000x slower for n=10^6
    fresh_ingredients = 0
    for i, (curr_start, curr_end) in enumerate(merged):
        min_index = bisect.bisect_left(ingredients, curr_start)
        max_index = bisect.bisect_right(ingredients, curr_end)
        # if no numbers are found, indices are equal and nothing is added
        fresh_ingredients += max_index - min_index

        # write progress output at set intervals, at least 500 ranges
        if (i+1) % max((len(merged)//10, 500)) == 0:
            print(f"Ranges searched: {i}/{len(merged)} ({i/len(merged):.2%}).\n\
  Time elapsed: {(perf_counter()-t00)*1000:.1f} ms.\n\
  Predicted total finishing time: {(t4_1-t00)+(perf_counter()-t4_1)/(i+1)*len(merged):.1f} s.")

    t5 = perf_counter()
    print(f"{BOLD}Timing:{RESET} Counted number of fresh ingredients: {(t5-t4_1):.3f} s.")

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
print(f"{BOLD}Timing:{RESET} Total execution time: {(t6-t0)*1000:.1f} ms.")