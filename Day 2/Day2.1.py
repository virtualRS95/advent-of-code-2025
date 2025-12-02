task_input_file = "input.txt"
debug_input_file1 = "debuginput1.txt" # answer should be 1227775554

# Define font formatting codes for easy use
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'


def main(input_file, expected_result = None):
    # function to read in input-file
    with open(input_file) as ifp:
        data = ifp.read().split(',')

    # make list of lists with start- and endpoints of ranges
    for i in range(len(data)):
        a, b = data[i].split('-')
        data[i] = [int(a), int(b)] # int function call removes leading zeros

    # loop over regions and check for invalid ID's by comparing first and second half of values in the range
    invalid_id_sum = 0
    for data_range in data:
        for number in range(data_range[0], data_range[1] + 1):
            str_num = str(number)
            # check if number has odd number of digits (can be eliminated):
            if len(str(number))%2 == 1:
                continue

            if str_num[:int(len(str_num)/2)] == str_num[int(len(str_num)/2):]:
                invalid_id_sum += number
                # print(f"debug: invalid ID found: {number}") # debug print statement

    if expected_result:
        if invalid_id_sum == expected_result:
            print(f"{BOLD}{GREEN}PASS{RESET}: Sum of invalid IDs: {invalid_id_sum}. Expected Result: {expected_result}.")
        else:
            print(f"{BOLD}{RED}FAIL{RESET}: Sum of invalid IDs: {invalid_id_sum}. Expected Result: {expected_result}.")
    else:
        print(f"Sum of invalid IDs: {invalid_id_sum}")

main(debug_input_file1, 1227775554)
main(task_input_file)