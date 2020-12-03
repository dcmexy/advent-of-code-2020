
puzzle = []
colLength = 0

# Read data from file
with open('input.txt') as f:
    # lines = f.read().splitlines()
    for line in f:
        puzzle.append(line.strip('\n').split(' ')[0])
    colLength = len(puzzle[0])


# Solution - traverse puzzle and count trees in any given direction


def countTrees(right, down):
    track = 0
    trees = 0
    for i in range(down, len(puzzle), down):
        j = track + right
        if puzzle[i][j] == '#':
            trees += 1
        if colLength - j <= right:
            track = j - colLength
        else:
            track += right
    return trees


# Part 1 solution
print(countTrees(3, 1))

# Print part 2 individual parts
print(countTrees(1, 1), countTrees(3, 1), countTrees(
    5, 1), countTrees(7, 1), countTrees(1, 2))

# Print Part two solution
print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1)
      * countTrees(7, 1) * countTrees(1, 2))
