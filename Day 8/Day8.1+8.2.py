import math
import struct

# input files
debug_input_file = "debuginput8.1.txt"
task_input_file = "input.txt"
test_input_file = "bigboy8.txt"

def fast_inverse_sqrt(number):
    # Convert the input number to a 32-bit floating point value
    x = float(number)
    # Interpret the input number as a 32-bit signed integer
    i = struct.unpack('i', struct.pack('f', x))[0]
    # Use the magic number to estimate the square root
    i = 0x5F3759DF - (i >> 1)
    # Interpret the estimate as a 32-bit floating point value
    y = struct.unpack('f', struct.pack('i', i))[0]
    # Use Newton's method to refine the estimate
    return y * (1.5 - 0.5 * x * y * y)

def open_testcase(file_name, num_connections): 
    with open(file_name, 'r') as ifp:
        lines = ifp.read().splitlines()
        boxes = [tuple(int(num) for num in line.split(',')) for line in lines]#[(int(x), int(y), int(z) for line.split(',')) for line in lines]
    num_boxes = len(boxes)

    # allocate array of distances between boxes, then compute upper triangle without diagonal
    distances = [[math.inf]*num_boxes for _ in range(num_boxes)]
    for i in range(num_boxes):
        for j in range(i+1, num_boxes):
            xyz = zip(*[boxes[i], boxes[j]])
            diffs = sum([(a-b)**2 for a, b in xyz])
            distances[i][j] = 1/fast_inverse_sqrt(diffs)
            #distances[i][j] = math.sqrt(diffs)

    # now lets unroll all distances into a single list that can be sorted.
    # create two accompanying lists that know the IDs of the first and second box for that distance.
    flat_distances = [x for row in distances for x in row]
    flat_ids = [(i, j) for i in range(num_boxes) for j in range(num_boxes)]

    # sort by distances between circuits ascending (mirror the sort to the IDs).
    sorted_distances, sorted_ids = zip(*sorted(zip(flat_distances, flat_ids)))
    # remove all trailing, non-upper-triangle values
    sorted_distances = sorted_distances[:(num_boxes**2)//2-num_boxes//2]
    sorted_ids = sorted_ids[:(num_boxes**2)//2-num_boxes//2]

    
    # create a list of circuits and start with the smallest connection
    circuits = []
    a, b = sorted_ids[0]
    circuits.append({a, b})

    # add the remaining connections
    for i in range(1, num_connections):
        a, b = sorted_ids[i]
        contained_in = []
        for j, circuit in enumerate(circuits):
            if a in circuit or b in circuit:
                circuits[j].add(a)
                circuits[j].add(b)
                contained_in.append(j)
        if len(contained_in) == 0:
            circuits.append({a, b})
        if len(contained_in) > 1:
            # merge those circuits into circuits[j[0]] and remove circuits[j[n]]
            for j in range(1, len(contained_in)):
                circuits[contained_in[0]].update(circuits[contained_in[j]])
                del circuits[contained_in[j]]
        i2 = i

    # sort circuits descending by number of boxes contained
    circuits1 = sorted(circuits, key=len, reverse=True)
    set_of_included_circuits = set(box_id for circuit in circuits1 for box_id in circuit)
    unused_boxes = set([i for i in range(20)]) - set_of_included_circuits
    #print(f"Unusued boxes: {unused_boxes}. Total number of circuits: {len(circuits)+len(unused_boxes)}.")
    #for circuit in circuits:
    #    print([boxes[box_id] for box_id in circuit])

    # get the result by multiplying the lengths of the longest 3 circuits
    task_1_result = math.prod(len(circuit) for circuit in circuits1[:3])
    print(f"Task 1 result: {task_1_result}.")

    # now Continue with task 2
    while True:
        a, b = sorted_ids[i2]
        contained_in = []
        for j, circuit in enumerate(circuits):
            if a in circuit or b in circuit:
                circuits[j].add(a)
                circuits[j].add(b)
                contained_in.append(j)
        if len(contained_in) == 0:
            circuits.append({a, b})
        if len(contained_in) > 1:
            # merge those circuits into circuits[j[0]] and remove circuits[j[n]]
            for j in range(1, len(contained_in)):
                circuits[contained_in[0]].update(circuits[contained_in[j]])
                del circuits[contained_in[j]]
        set_of_included_circuits = set(box_id for circuit in circuits1 for box_id in circuit)
        unused_boxes = set([i for i in range(20)]) - set_of_included_circuits
        i2 += 1
        if len(unused_boxes) == 0 and len(circuits) == 1:
            print(a, b)
            print(f"Task 2 result: {boxes[a][0]*boxes[b][0]}.")
            break
    print(i2)

open_testcase(debug_input_file, 10)
open_testcase(task_input_file, 1000)