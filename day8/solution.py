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


def processInstruction(pos, acc):
    # Check for empty or negative indices
    if not instructions or pos < 0:
        return 0

    # Check that instruction has not executed run at least once
    if pos in visitedPos:
        return acc

    # Track current instruction
    visitedPos.append(pos)

    # unpack instruction and execute accordingly
    # print(pos)
    if instructions[pos][0] == 'nop':
        # process next item
        return processInstruction(pos + 1, acc)

    if instructions[pos][0] == 'acc':
        # adjust acc and process next item
        acc += int(instructions[pos][1])
        return processInstruction(pos + 1, acc)

    if instructions[pos][0] == 'jmp':
        # skip to next item
        return processInstruction(pos + int(instructions[pos][1]), acc)

    return acc


def processInstruction2(pos, acc):

    if not instructions or pos < 0:
        return False

    if pos in visitedPos:
        return False

    if pos >= len(instructions):
        # print("here")
        return acc

    visitedPos.append(pos)

    if instructions[pos][0] == 'nop':
        nopVal = processInstruction2(pos + 1, acc)
        if not nopVal and int(instructions[pos][1]) != 0:
            return mutateInstruction('jmp', pos, acc)
        return nopVal
    if instructions[pos][0] == 'acc':
        # adjust acc and process next item
        acc += int(instructions[pos][1])
        return processInstruction2(pos + 1, acc)

    if instructions[pos][0] == 'jmp':
        # skip to next item
        # return processInstruction2(pos + int(instructions[pos][1]), acc)

        jmpVal = processInstruction2(pos + int(instructions[pos][1]), acc)
        if not jmpVal:
            return mutateInstruction('nop', pos, acc)
        return jmpVal

    # print(instructions[pos])
    return acc


def processMutatedInstruction(pos, acc, inst):
    # print(pos, inst[pos])
    # return False
    if not inst or pos < 0:
        return False

    if pos in mutatedVisit:
        return False

    if pos >= len(inst):
        # print("here")
        return acc

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


print(processInstruction2(0, 0))
print(processInstruction(0, 0))
