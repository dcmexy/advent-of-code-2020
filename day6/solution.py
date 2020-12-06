# Part 1 solution for day 6.

# Read data from file
with open('input.txt') as f:
    lines = f.read().splitlines()
    numberOfLines = len(lines)
    groups = []
    yeses = ''

    for i, line in enumerate(lines):
        val = line.strip('\n')
        yeses += val

        # Break into groups when empty line or EOF
        if val == '' or i == numberOfLines - 1:
            groups.append(len(set(yeses)))
            yeses = ''

    print("Sum of counts:", sum(groups))
