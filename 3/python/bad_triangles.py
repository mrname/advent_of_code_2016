from itertools import combinations
from copy import copy

INPUT_FILE = 'input.txt'
VALID_TRIANGLES = 0

INPUT = []
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

for entry in INPUT:
    if is_triangle_valid(entry):
        VALID_TRIANGLES += 1

print(VALID_TRIANGLES)
