from copy import deepcopy

puzzle = []

# Part 1 of solution - Day 11


def process():
    # Count number of columns
    colLength = len(puzzle[0])
    # Count number of rows
    rowLength = len(puzzle)
    # Set bounds
    bounds = [-1, 0, 1]

    while True:
        puzzle2 = deepcopy(puzzle)
        totalOccupied = 0
        for r in range(rowLength):
            for c in range(colLength):
                adjOccupied = 0
                for rb in bounds:
                    for cb in bounds:
                        if (r + rb >= 0 and r + rb < rowLength) and (c + cb >= 0 and c + cb < colLength):
                            if not (rb == 0 and cb == 0):
                                if puzzle2[r + rb][c + cb] == '#':
                                    adjOccupied += 1

                if adjOccupied == 0 and puzzle[r][c] == 'L':
                    puzzle[r][c] = '#'

                if puzzle[r][c] == '#':
                    totalOccupied += 1
                    if adjOccupied >= 4:
                        puzzle[r][c] = 'L'

        if puzzle == puzzle2:
            print("Total Occupied", totalOccupied)
            break


def process2():
    # Count number of columns
    colLength = len(puzzle[0])
    # Count number of rows
    rowLength = len(puzzle)

    while True:
        puzzle2 = deepcopy(puzzle)
        totalOccupied = 0
        isSame = True
        for r in range(rowLength):
            for c in range(colLength):
                if puzzle[r][c] == '.':
                    continue
                adjOccupied = 0
                bounds = [-1, 0, 1]

                for rb in bounds:
                    for cb in bounds:
                        rbt = r + rb
                        cbt = c + cb
                        if rb == 0 and cb == 0:
                            continue
                        while (rbt >= 0 and rbt < rowLength) and (cbt >= 0 and cbt < colLength and puzzle2[rbt][cbt] == '.'):
                            rbt += rb
                            cbt += cb

                        if (rbt >= 0 and rbt < rowLength) and (cbt >= 0 and cbt < colLength) and puzzle2[rbt][cbt] == '#':
                            adjOccupied += 1
                if adjOccupied == 0 and puzzle[r][c] == 'L':
                    puzzle[r][c] = '#'
                    isSame = False
                elif puzzle[r][c] == '#':
                    totalOccupied += 1
                    if adjOccupied >= 5:
                        puzzle[r][c] = 'L'
                        isSame = False

        if isSame:
            print("Total Occupied", totalOccupied)
            break


    # Read data from file
with open('input.txt') as f:
    for line in f:
        puzzle.append(list(line.strip('\n').split(' ')[0]))

    # process()
    process2()
