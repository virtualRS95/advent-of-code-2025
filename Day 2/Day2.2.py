# input files
task_input_file = "input.txt"
debug_input_file1 = "debuginput1.txt" # answer should be 1227775554 for task 1
debug_input_file2 = "debuginput2.txt" # answer should be 4174379265 for task 2

# Define font formatting codes for easy use
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'

def string_into_segments(string, segment_length):
    """splits string into segment_lenght long substrings generator object"""
    for i in range(0, len(string), segment_length):
        yield string[i: i + segment_length]

def check_if_invalid1(number):
    """Checks if first and last half of number's digits are equal"""
    str_num = str(number)
    if len(str(number))%2 == 0 and str_num[:int(len(str_num)/2)] == str_num[int(len(str_num)/2):]:
        # print(f"debug: invalid ID(1) found: {number}") # debug print statement
        return(number)  
    return 0

def check_if_invalid2(number):
    """checks if number is only made up of repeating digits"""
    str_num = str(number)
    # Find all possible divisors for a number's length to check for repeating pattern
    for seglength in range(1, int(len(str_num)/2) + 1):
        if len(str_num) % seglength == 0:
            segments = string_into_segments(str_num, seglength)
            # if one segment differs, number is not invalid
            all_equal = True
            first_segment = next(segments)
            for segment in segments:
                if segment != first_segment:
                    all_equal = False
                    break
            # return if invalid, to avoid double counting e.g. 12121212 (2x and 4x repeating).
            if all_equal:
                #print(f"debug: invalid ID(2) found: {number}") # debug print statement
                return number
    return 0

def main(input_file, expected_result1 = None, expected_result2 = None):
    """Prints the sum of invalid numbers that occur in the input_file"""
    # reading input file
    with open(input_file) as ifp:
        data = ifp.read().split(',')

    # make list of lists with start- and endpoints of ranges
    for i in range(len(data)):
        a, b = data[i].split('-')
        data[i] = [int(a), int(b)] # int function call removes leading zeros

    # loop over regions and check for invalid ID's by comparing first and second half of values in the range
    invalid_id_sum1 = 0
    invalid_id_sum2 = 0
    for data_range in data:
        for number in range(data_range[0], data_range[1] + 1):
            invalid_id_sum1 += check_if_invalid1(number)
            invalid_id_sum2 += check_if_invalid2(number)

    # output PASS/FAIL on tests or the result for both invalid ID sums
    if expected_result1:
        if invalid_id_sum1 == expected_result1:
            print(f"{BOLD}{GREEN}PASS{RESET}: Sum of invalid IDs (1): {invalid_id_sum1}. Expected Result: {expected_result1}.")
        else:
            print(f"{BOLD}{RED}FAIL{RESET}: Sum of invalid IDs (1): {invalid_id_sum1}. Expected Result: {expected_result1}.")
    if expected_result2:
        if invalid_id_sum2 == expected_result2:
            print(f"{BOLD}{GREEN}PASS{RESET}: Sum of invalid IDs (2): {invalid_id_sum2}. Expected Result: {expected_result2}.")
        else:
            print(f"{BOLD}{RED}FAIL{RESET}: Sum of invalid IDs (2): {invalid_id_sum2}. Expected Result: {expected_result2}.")
    if not expected_result1 and not expected_result2:
        print(f"Sum of invalid IDs (1): {invalid_id_sum1}")
        print(f"Sum of invalid IDs (2): {invalid_id_sum2}")

main(debug_input_file1, 1227775554)
main(debug_input_file2, None , 4174379265)
main(task_input_file)