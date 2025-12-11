import threading
debug_input_file = "debuginput11.txt"
task_input_file = "input.txt"


# read in file and split every line into source and possible destinations
with open(task_input_file, 'r') as ifp:
    lines = ifp.read().splitlines()
nodes = {}
for line in lines:
    x, y = line.split(': ')
    nodes[x] = [z.strip() for z in y.split()]

# remove key, value pairs from the dictionary if they do not have any connections coming in
# need to do this iteratively, not just once 
keys_to_remove = []
for key in nodes.keys():
    is_connected = False
    for value in nodes.values():
        if key in value:
            is_connected = True
    if is_connected == False:
        keys_to_remove.append(key)
for item in keys_to_remove:            
    nodes.pop(item, None)
print(f"Removed {len(keys_to_remove)} nodes without incoming paths.")


# walk down the path towards the end
# keep track of nodes already visited in a set. Exclude them from searches.
# If it does not terminate at "out", multiply paths with 0.

# go recursively backwards from out. At every node, sum the contributions of paths to that node. The contributions are evaluated next by going deeper in the tree. At every recusive function pass on the set of visited points to exclude from searches. If we find "you", multiply by 1, otherwise if no sets found, return 0

def recursively_count_previous_nodes(nodes: dict, current_node: str, visited_nodes: set, path_multiplier: int):
    """fixed end node 'out' and fixed start node 'you'
    returns 1 if it finds 'you', 
    returns n number of paths into the previous node for any others
    returns 0 if we cant find 'you' (available points - set is empty)
    
    nodes: <dict> of all nodes and their outgoing connections
    current node: <string> of current location to search for incoming connections
    visited nodes: <set> of strings of locations already visited to avoid loops
    path_multiplier <int> idk yet"""
    # find all nodes that connect into the current one
    deeper_nodes = []
    for key, value in nodes.items():
        if current_node in value:
            #print(f"Key {key} connects to {current_node}.")
            deeper_nodes.append(key)

    # Remove all already visited points from deeper nodes
    valid_nodes = set(deeper_nodes) - visited_nodes
    print(f"I am at node {current_node} with {path_multiplier} paths and will search next at {valid_nodes}.")
    
    # check if there are no unvisited deeper nodes
    if len(valid_nodes) == 0:
        print("No more valid nodes available, returning 0")
        return 0

    # recursively go into deeper nodes
    current_multiplier = 0
    visited_nodes.add(current_node)
    #print(f"debug {visited_nodes}")
    for next_node in valid_nodes:
        # check if 'you' was reached
        if next_node == 'you':
            print("Found the starting point, returning 1")
            current_multiplier += 1
        else:
            current_multiplier += recursively_count_previous_nodes(nodes, next_node, visited_nodes, path_multiplier)

    print(f"Node {current_node}, current multiplier: {current_multiplier}, total multiplier {path_multiplier + current_multiplier}.")
    return path_multiplier + current_multiplier
    
def recursively_count_next_nodes(nodes: dict, current_node):
    if current_node == 'out': return 1
    path_value = 0
    for node in nodes[current_node]:
        path_value += recursively_count_next_nodes(nodes, node)
    return path_value

number_of_paths = recursively_count_next_nodes(nodes, 'you')
#number_of_paths = recursively_count_previous_nodes(nodes, 'out', set(), 0)
print(f"Number of paths: {number_of_paths}")







"""source = []
destinations = [] 
for line in lines:
    x, y = line.split(':')
    source.append(x.strip())
    destinations.append([z.strip() for z in y.split()])

# create a dictionary of the input
nodes = dict(zip(source, destinations))"""