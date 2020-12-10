
# Solve part 1


def processAdapters(data):
    prev = 0

    # captures diffs for 1-jolt, and 3-jolts
    diffs = [0, 0]
    for i in data:

        if i - prev > 3:
            break
        if i - prev == 1:
            diffs[0] += 1
        if i - prev == 3:
            diffs[1] += 1
        prev = i

    # Add built in adapter
    diffs[1] += 1

    # return diff for 1-jolt * diffs for 3-jolts
    return diffs[0] * diffs[1]


# Read data from file
with open('input.txt') as f:
    data = []
    for line in f:
        data.append(int(line.strip()))

    # Sort data
    data.sort()

    print("Part 1 =", processAdapters(data))
