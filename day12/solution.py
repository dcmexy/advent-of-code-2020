data = []


def getNextDirection(currentDirection, change):
    if change == 180:
        if currentDirection == 'E':
            return 'W'
        if currentDirection == 'W':
            return 'E'
        if currentDirection == 'N':
            return 'S'
        elif currentDirection == 'S':
            return 'N'
    if change == 90 or change == 270:
        pass


def solve():
    directions = {"E": 0, "W": 0,  "N": 0, "S": 0}
    currentDirection = 'E'

    for d in data:
        way = d[0]
        step = int(d[1:])

        if way == 'F':
            directions[currentDirection] += step
        elif way == 'R' or way == 'L':
            if step == 270:
                way = 'R' if way == "L" else 'L'
            if step == 180:
                if currentDirection == 'E':
                    currentDirection = 'W'
                elif currentDirection == 'W':
                    currentDirection = 'E'
                elif currentDirection == 'N':
                    currentDirection = 'S'
                elif currentDirection == 'S':
                    currentDirection = 'N'
            if step == 90 or step == 270:
                if way == "R":
                    if currentDirection == 'E':
                        currentDirection = 'S'
                    elif currentDirection == 'S':
                        currentDirection = 'W'
                    elif currentDirection == 'W':
                        currentDirection = 'N'
                    elif currentDirection == 'N':
                        currentDirection = 'E'
                elif way == "L":
                    if currentDirection == 'E':
                        currentDirection = 'N'
                    elif currentDirection == 'N':
                        currentDirection = 'W'
                    elif currentDirection == 'W':
                        currentDirection = 'S'
                    elif currentDirection == 'S':
                        currentDirection = 'E'
        else:
            directions[way] += step

    return abs(directions['E'] - directions['W']) + abs(directions['N'] - directions['S'])


with open('input.txt') as f:
    for line in f:
        data.append(line.strip())

print(solve())
