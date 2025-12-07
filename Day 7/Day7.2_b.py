#from collections import deque

task_file_name = "input.txt"

def open_testcase (file_name, debug = False): 
    with open(file_name) as ifp:
        lines = ifp.read().splitlines()#[:5]
        # assume field is rectangular
        n_rows = len(lines)
        n_cols = len(lines[0])
        print(f"The input field is of size {n_rows}x{n_cols}")

    # find start point
    start_index = lines[0].index("S")
    current_beam = [start_index]
    print(f"Current beam at {current_beam}")

    # go line-by-line and update the tachyon beam columns
    splits_count = 0
    paths_count = 0
    for line in lines:
        if "^" not in line:
            continue
        split_indices = [i for i, x in enumerate(line) if x == "^"]
        for idx in split_indices:
            if idx in current_beam:
                beam_list_index = current_beam.index(idx)
                current_beam[beam_list_index] = idx-1
                current_beam.insert(beam_list_index+1, idx+1)
                splits_count += 1
        paths_count += len(current_beam)
            #current_beam = list(set(current_beam))
            #print(f"Current beam at {current_beam}")

        #print(f"line splitting beam at {split_indices}")
    print(f"Splits count: {splits_count}")

    # task 2: count all possible particle paths. Lets do recursion!
    print(f"Paths count: {paths_count}.")
    # at each split call a recusive function that goes both paths. When the end of the board is reached, increment the number of paths
    


open_testcase(task_file_name)