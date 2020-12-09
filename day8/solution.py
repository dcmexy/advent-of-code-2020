# Initialize instructions
instructions = []

# Initialize visited positions
visitedPos = []


def process(pos, acc):
    if not instructions or pos < 0:
        return 0

    if pos in visitedPos:
        return acc

    visitedPos.append(pos)

    if instructions[pos][0] == 'nop':
        # process next item
        return process(pos + 1, acc)
    if instructions[pos][0] == 'acc':
        # adjust acc and process next item
        acc += int(instructions[pos][1])
        return process(pos + 1, acc)

    if instructions[pos][0] == 'jmp':
        # skip to next item
        return process(pos + int(instructions[pos][1]), acc)

    return acc


# Read data from file
with open('input.txt') as f:

    for line in f:
        instructions.append(line.strip('.\n').split(' '))

    print(process(0, 0))
