import numpy as np

schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

schematic = schematic.splitlines()

with open('3.txt') as f:
    schematic = f.readlines()

def is_symbol(c):
    return (not c.isdigit()) and (not c.isalpha()) and c!='.'

symbols = list(map(lambda line: list(map(is_symbol, line)), schematic))
symbols = np.array(symbols)
digits = list(map(lambda line: list(map(str.isdigit, line)), schematic))
schematic = np.array(schematic)
symbol_locs = np.transpose(symbols.nonzero())

runs = []

for i, row in enumerate(digits):
    in_run = False
    start = None
    for j, cell in enumerate(row):
        if cell == True and in_run == False:
            in_run = True
            start = (i,j)
        if cell == False and in_run == True:
            in_run = False
            runs.append((start, (i,j-1)))
    if in_run == True:
        j_max = len(schematic[0])-1
        runs.append((start, (i, j_max)))

def get_adjacent_locs(i,j):
    i_max = schematic.shape[0]-1
    j_max = len(schematic[0])-1
    locs = []
    if i>0 and j>0:
        locs += [(i-1, j-1)]
    if i>0:
        locs += [(i-1, j)]
    if i>0 and j<j_max:
        locs += [(i-1, j+1)]
    if j>0:
        locs += [(i, j-1)]
    if j<j_max:
        locs += [(i, j+1)]
    if i<i_max and j>0:
        locs += [(i+1, j-1)]
    if i<i_max:
        locs += [(i+1, j)]
    if i<i_max and j<j_max:
        locs += [(i+1, j+1)]
    return locs

adjacent_locs = []
for i,j in symbol_locs:
    adjacent_locs += get_adjacent_locs(i,j)

# now we have a list of all the starting and ending positions of any candidate serial numbers
# as well as a list of all the positions that them numbers would need to be within to be valid serial numbers
# so the plan is to check which of the candidate serial numbers are actually serial numbers

def is_valid_serial(candidate_pos):
    start_pos, end_pos = candidate_pos
    start_i, start_j = start_pos
    end_i, end_j = end_pos
    for adj_loc in adjacent_locs:
        i,j = adj_loc
        if start_i == i and start_j <= j and end_j >= j:
            return True
    return False

valid_serial_locs = list(filter(is_valid_serial, runs))
print(valid_serial_locs)

def str_from_pos(serial_pos):
    start_pos, end_pos = serial_pos
    start_i, start_j = start_pos
    end_i, end_j = end_pos
    return int(schematic[start_i][start_j:end_j+1])

serial_numbers = list(map(str_from_pos, valid_serial_locs))
print(serial_numbers)
print(sum(serial_numbers))
