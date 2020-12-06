#  Complete Solution
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

    if rowTrack > 200:
        print(rowTrack, colTrack, (rowTrack * 8) + colTrack)
    return (rowTrack * 8) + colTrack


# Read data from file
with open('input.txt') as f:
    highestSeatId = 0
    lowestSeatId = (120 * 8) + 8
    seatIds = []  # Seat Id pool
    for line in f:
        seatId = getSeatId(line.strip())

        # Add Seat Id to pool
        seatIds.append(seatId)

        # Track Highest Seat Id
        if seatId > highestSeatId:
            highestSeatId = seatId

        # Track Lowest Seat Id
        if seatId < lowestSeatId:
            lowestSeatId = seatId

    # Find Missing Seat
    for x in range(lowestSeatId, highestSeatId + 1):
        if x not in seatIds and (x + 1) in seatIds and (x - 1) in seatIds:
            print("Missing Seat Id", x)

    print("Highest Seat Id: ", highestSeatId)
    print("Lowest Seat Id: ", lowestSeatId)
