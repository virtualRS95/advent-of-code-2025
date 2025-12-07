task_file_name = "input.txt"
test_file_name = "debuginput1.txt"
big_file_name = "bigboy7.txt"

def open_testcase (file_name): 
    with open(file_name) as ifp:
        lines = ifp.read().splitlines()#[:5]
        # assume field is rectangular
        n_rows = len(lines)
        n_cols = len(lines[0])
        print(f"The input field is of size {n_rows}x{n_cols}")

    # initialise array of possible beam locations
    beam_locations = [0]*n_cols

    # find start point
    start_index = lines[0].index("S")
    beam_locations[start_index] += 1
    beam_active = set([start_index])

    splits_count = 0
    paths_count = 0 # 1 path for the start

    for line in lines[1:]:
        if "^" not in line:
            continue
        split_indices = [i for i, x in enumerate(line) if x == "^"]
        #print([x for x in line])
        for idx in split_indices:
            if idx in beam_active:
                # keep track of beam
                splits_count += 1
                beam_active.remove(idx)
                beam_active.add(idx-1)
                beam_active.add(idx+1)
                # keep track of paths
                #paths_count += 2 * beam_locations[idx]
                n_paths = beam_locations[idx]
                beam_locations[idx] -= 1*n_paths
                beam_locations[idx-1] += 1*n_paths
                beam_locations[idx+1] += 1*n_paths
        #print([str(x) for x in beam_locations])
    paths_count = sum(beam_locations)

    print(f"Splits count: {splits_count}")
    print(f"Paths count: {paths_count}.")

open_testcase(task_file_name)
#open_testcase(test_file_name)
open_testcase(big_file_name)