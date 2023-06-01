# Below is my Day 2 Puzzle Part 1
# Goal: What do you get if you multiply your final horizontal position by your final depth?

# Define if we are using the test file or non-test input file
test = False
if test:
    data_file = 'test_input.txt'
else:
    data_file = 'data/input.txt'

# Assign the input data into the variable known as 'array_commands'
with open(data_file, 'r') as file_input:
    array_commands = file_input.read().splitlines()

# Print out how many commands there are in the input file
total_commands = len(array_commands)
print(f'There are {total_commands} total submarine command(s)')

# Declare and assign positions to zero
horizontal_position = 0
depth = 0

# Condition that read the array (sumbarine_commands) and re-assign positions
for i in range(0, total_commands):
    # Forward command
    if (array_commands[i].startswith('f')):
        last_num = array_commands[i][-1]
        horizontal_position += int(last_num)
    # Up command
    if (array_commands[i].startswith('u')):
        last_num = array_commands[i][-1]
        depth -= int(last_num)
    # Down command
    if (array_commands[i].startswith('d')):
        last_num = array_commands[i][-1]
        depth += int(last_num)

# Print out the horizontal and depth positions since they were re-assigned in the prior if blocks
print(f"Your horizontal position is : {horizontal_position}  and depth is : {depth}") 
answer = horizontal_position * depth
print(f"Answer to the part 1 puzzle is : {answer}\n\n\n\n")
# Answer is horizontal = 1950 and depth = 823. The product of these two numbers = 1,604,850

# ******************************************************************************
print()
# Below is my Day 2 Puzzle Part 2
# Goal: What do you get if you multiply your final horizontal position by your final depth?

# Define if we are using the test file or non-test input file
test = False
if test:
    data_file = 'test_input.txt'
else:
    data_file = 'data/input_part2.txt'

# Assign the input data into the variable known as 'array_commands'
with open(data_file, 'r') as file_input:
    array_commands = file_input.read().splitlines()

# Print out how many commands there are in the input file
total_commands = len(array_commands)
print(f'There are {total_commands} total submarine command(s)')

# Declare and assign positions to zero
horizontal_position = 0
depth = 0
aim = 0

# Condition that read the array (sumbarine_commands) and re-assign positions
for i in range(0, total_commands):
    # Forward command
    if (array_commands[i].startswith('f')):
        last_num = array_commands[i][-1]
        horizontal_position += int(last_num)
        depth += (int(last_num) * aim)
    # Up command
    if (array_commands[i].startswith('u')):
        last_num = array_commands[i][-1]
        aim -= int(last_num)
    # Down command
    if (array_commands[i].startswith('d')):
        last_num = array_commands[i][-1]
        aim += int(last_num)

# Print out the horizontal and depth positions since they were re-assigned in the prior if blocks
print(f"Your horizontal position is : {horizontal_position}  ,  depth is : {depth}  ,  and aim is : {aim}") 
answer = horizontal_position * depth
print(f"Answer to the puzzle is : {answer}")
# Answer is horizontal = 1950, depth = 864198, and aim = 823. The answer = 1,685,186,100