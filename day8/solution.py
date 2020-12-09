# Initialize instructions
instructions = []

# Initialize visited positions
visitedPos = []
mutatedVisit = []

# funtion to mutate(swap) instruction action and then check for normal termination behaviour
# pos = current position, acc = current accumulated points


def mutateInstruction(action, pos, acc):

    # Get a fresh copy of all instructions
    inst = instructions.copy()

    # mutate insstruction action
    inst[pos][0] = action

    # Clear mutated visit list
    mutatedVisit.clear()

    return processMutatedInstruction(pos, acc, inst)

# function to process Task 1


def processInstruction(pos, acc, task=1):
    # Check for empty or negative indices
    if not instructions or pos < 0:
        return False

    # Check that instruction has not executed run at least once
    if pos in visitedPos:
        return False if task == 2 else acc

    # Check for normal termination
    if pos >= len(instructions) and task == 2:
        return acc

    # Track current instruction
    visitedPos.append(pos)

    # unpack instruction and execute accordingly

    if instructions[pos][0] == 'nop':
        # process next item
        nopVal = processInstruction(pos + 1, acc, task)
        if not nopVal and task == 2 and int(instructions[pos][1]) != 0:
            return mutateInstruction('jmp', pos, acc)
        return nopVal

    if instructions[pos][0] == 'acc':
        # adjust acc, then skip and process next item
        acc += int(instructions[pos][1])
        return processInstruction(pos + 1, acc, task)

    if instructions[pos][0] == 'jmp':
        # skip to next item
        jmpVal = processInstruction(pos + int(instructions[pos][1]), acc, task)
        if not jmpVal and task == 2:
            return mutateInstruction('nop', pos, acc)
        return jmpVal

    return acc


def processMutatedInstruction(pos, acc, inst):
    # Check for empty or negative indices
    if not inst or pos < 0:
        return False

    # Check that mutated instruction has not executed run at least once
    if pos in mutatedVisit:
        return False

    # Check for normal termination
    if pos >= len(inst):
        return acc

    # Track current mutated instruction
    mutatedVisit.append(pos)

    if inst[pos][0] == 'nop':
        # process next item
        return processMutatedInstruction(pos + 1, acc, inst)
    if inst[pos][0] == 'acc':
        # adjust acc and process next item
        acc += int(instructions[pos][1])
        return processMutatedInstruction(pos + 1, acc, inst)

    if inst[pos][0] == 'jmp':
        # skip to next item
        return processMutatedInstruction(pos + int(inst[pos][1]), acc, inst)

    # print(instructions[pos])
    return False


# Read data from file
with open('input.txt') as f:
    # populate instruction list
    for line in f:
        instructions.append(line.strip('.\n').split(' '))

# Execute Tasks processInstruction(pos, acc, task)
# For Task 2
print(processInstruction(0, 0, 2))
# For Task 1
# print(processInstruction(0, 0))
