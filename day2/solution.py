# Validate Password
def isValidPassword(portfolio, part):
    policy = portfolio[0].split(' ')
    password = portfolio[1].strip()
    characterToCheck = policy[1]
    characterCountRange = policy[0].split('-')

    # Part 1
    if part == 1:
        characterCount = password.count(characterToCheck)

        return (characterCount >= int(characterCountRange[0]) and characterCount <= int(characterCountRange[1]))

    if part == 2:
        characterCount = 0

        if password[int(characterCountRange[0]) - 1] == characterToCheck:
            characterCount += 1
        if password[int(characterCountRange[1]) - 1] == characterToCheck:
            characterCount += 1

        return characterCount == 1


# Read data from file
with open('input.txt') as f:
    count = [0, 0]
    for line in f:
        count[0] += isValidPassword(line.strip().split(':'), 1)
        count[1] += isValidPassword(line.strip().split(':'), 2)

    print(count)
