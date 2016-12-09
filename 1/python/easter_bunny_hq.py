INSTRUCTIONS = 'R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3'

DIRECTION_MAP = ['N', 'E', 'S', 'W']
DIRECTION_IDX = 0
STEP_TRACKER = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

instructions = map(lambda x: x.strip(), INSTRUCTIONS.split(','))
for instruction in instructions:
    direction = instruction[0:1]
    if direction == 'L':
        DIRECTION_IDX -= 1
    else:
        DIRECTION_IDX += 1
    num_steps = int(instruction[1:])
    STEP_TRACKER[DIRECTION_MAP[DIRECTION_IDX % 4]] += num_steps
print(abs(STEP_TRACKER['N'] - STEP_TRACKER['S']) +
      abs(STEP_TRACKER['W'] - STEP_TRACKER['E'])
    )
