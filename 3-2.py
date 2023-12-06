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

def is_star(c):
    return c=='*'

stars = list(map(lambda line: list(map(is_star, line)), schematic))
stars = np.array(stars)
digits = list(map(lambda line: list(map(str.isdigit, line)), schematic))
schematic = np.array(schematic)
star_locs = np.transpose(stars.nonzero())

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
for i,j in star_locs:
    adjacent_locs.append(get_adjacent_locs(i,j))

def str_from_pos(serial_pos):
    start_pos, end_pos = serial_pos
    start_i, start_j = start_pos
    end_i, end_j = end_pos
    return int(schematic[start_i][start_j:end_j+1])

def get_gear_ratio(adjacent_locs):
    serials = []
    for serial in runs:
        serial_start, serial_end = serial
        serial_i, serial_start_j = serial_start
        serial_end_j = serial_end[1]
        for loc in adjacent_locs:
            loc_i, loc_j = loc
            if serial_i == loc_i and serial_start_j <= loc_j and serial_end_j >= loc_j:
                if serial not in serials:
                    serials.append(serial)
    if len(serials) != 2:
        return 0
    serials = list(map(str_from_pos, serials))
    print(serials)
    gear_ratio = serials[0] * serials[1]
    return gear_ratio

gear_ratios = list(map(get_gear_ratio, adjacent_locs))
print(gear_ratios)
print(sum(gear_ratios))
