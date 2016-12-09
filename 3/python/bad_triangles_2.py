from itertools import combinations
from copy import copy

INPUT_FILE = 'input.txt'
VALID_TRIANGLES = 0

INPUT = []
# TODO - surely there is a better way to loop through three elements of a list
# at a time
START_IDX = 0
END_IDX = 3

with open(INPUT_FILE, 'r') as f:
    for line in f:
        INPUT.append(line.strip().split())

def is_triangle_valid(entry):
    entry = list(map(lambda x: int(x), entry))
    for combo in combinations(entry, 2):
        entry_copy = copy(entry)
        for triangle_side in combo:
            entry_copy.remove(triangle_side)
        if sum(combo) <= entry_copy[0]:
            return False
    return True

while END_IDX <= len(INPUT):
    input_chunk = INPUT[START_IDX:END_IDX]
    for a,b,c in zip(*input_chunk):
        if is_triangle_valid([a,b,c]):
            VALID_TRIANGLES += 1
    START_IDX += 3
    END_IDX += 3

print(VALID_TRIANGLES)
