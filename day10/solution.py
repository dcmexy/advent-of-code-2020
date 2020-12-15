data = [0]
# Solve part 1


def processAdapters():
    prev = 0

    # captures diffs for 1-jolt, and 3-jolts
    diffs = [0, 0, 0]
    skips = []
    bigData = []

    prev
    for i in range(len(data)):

        if data[i] - prev > 3:
            break

        # Track differences
        if data[i] - prev == 1:
            diffs[0] += 1
        if data[i] - prev == 2:
            diffs[1] += 1
        if data[i] - prev == 3:
            diffs[2] += 1
        prev = data[i]

    return diffs[0] * diffs[2]


def calculateArrangement(count=0):
    val = 0
    visited = {}

    if count + 1 == len(data):
        return 1

    if count in visited:
        return visited[count]

    for i in range(count + 1, len(data)):
        if data[i] - data[count] <= 3:
            val += calculateArrangement(i)
    visited[count] = val
    return val


    # Read data from file
with open('input.txt') as f:
    for line in f:
        data.append(int(line.strip()))

    # Sort data
    data.sort()

    # Add built in adapter
    data.append(max(data) + 3)

    print("Part 1 =", processAdapters())
    print("Part 2 =", calculateArrangement())
