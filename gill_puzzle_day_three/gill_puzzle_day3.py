# Ajay Gill
# Advent of Code 2021 : Puzzle 3 Parts 1 and 2
# 31 May 2023

# Goal = What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

test = True
if test:
    data_file = 'test_input.txt'
else:
    data_file = 'data/input.txt'

# Assign the input data into the variable known as 'bits'
with open(data_file, 'r') as file_input:
    report_numbers = file_input.read().splitlines()

# Print out how many bits there are in the input file
total_number_lines = len(report_numbers)
print(f'There are {total_number_lines} total binary numbers')

# Declare and assign gamma and epsilon rates
gamma_rate = 0
epsilon_rate = 0

# Declare and assign gamma and epsilon bits
total_ones = 0
total_zeros = 0

# Condition that read the array (total_number_lines) and re-assigns gamma/epsilon rates
for i in range(0, total_number_lines):
# Check first bit
    first_bit = report_numbers[i][0]
    if (first_bit == "1"):
        total_ones += 1
    else:
        total_zeros += 1
    print(f'Total number of ones is: {total_ones} and total number of zeros is: {total_zeros}')
# Check second bit
    second_bit = report_numbers[i][1]
    if (second_bit == "1"):
        total_ones += 1
    else:
        total_zeros += 1
# Check first bit
    third_bit = report_numbers[i][2]
    if (third_bit == "1"):
        total_ones += 1
    else:
        total_zeros += 1
# Check fourth bit
    fourth_bit = report_numbers[i][3]
    if (fourth_bit == "1"):
        total_ones += 1
    else:
        total_zeros += 1
# Check fifth bit
    fifth_bit = report_numbers[i][4]
    if (fifth_bit == "1"):
        total_ones += 1
    else:
        total_zeros += 1
