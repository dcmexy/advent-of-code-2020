# Part 1 solution for day 6.

# Read data from file
with open('input.txt') as f:
    lines = f.read().splitlines()
    numberOfLines = len(lines)
    anyoneYes = []
    everyoneYes = []
    questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    yeses = ''
    yesCount = 0

    for i, line in enumerate(lines):
        val = line.strip('\n')

        # Track yesses
        if val != '':
            yesCount += 1
            yeses += val

        # Break into groups when empty line or EOF
        if val == '' or i == numberOfLines - 1:

            # Get count yes by anyone
            anyoneYes.append(len(set(yeses)))

            # Check for yes by everyone
            allYes = 0
            for q in questions:
                if q in yeses and yeses.count(q) == yesCount:
                    allYes += 1

            # Get count of yes by everyone
            everyoneYes.append(allYes)

            # Reset trackers
            yeses = ''
            yesCount = 0

    # Print answers
    print("Sum of Anyone Yes:", sum(anyoneYes))
    print("Sum of Everyone Yes:", sum(everyoneYes))
