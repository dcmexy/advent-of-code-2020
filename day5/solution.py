#  Part 1 Solution
#  Get Seat Id


def getSeatId(boardingPass):
    rowCount = 128
    colCount = 8
    rowTrack = 0
    colTrack = 0

    # Scan Boarding Pass
    for i in boardingPass:
        # Track upper half rows
        if i == 'B':
            rowCount = rowCount // 2
            rowTrack += rowCount

        # Track lower half rows
        if i == 'F':
            rowCount = rowCount // 2

        # Track upper half columns
        if i == 'R':
            colCount = colCount // 2
            colTrack += colCount

        # Track lower half columns
        if i == 'L':
            colCount = colCount // 2
    # print((rowTrack * 8) + colTrack)
    return (rowTrack * 8) + colTrack


# Read data from file
with open('input.txt') as f:
    highestSeatId = 0
    for line in f:
        seatId = getSeatId(line.strip())
        if seatId > highestSeatId:
            highestSeatId = seatId

    print("Highest Seat Id: ", highestSeatId)
