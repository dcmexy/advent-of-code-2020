# Validate Passport - Part 1
def isValidPassport(passport):
    dataKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    return (len(passport) >= 7 and 'cid' not in passport.keys()) or len(passport) == 8


# Read data from file
with open('input.txt') as f:
    validCount = 0
    passportData = {}
    lines = f.read().splitlines()
    numberOfLines = len(lines)

    for i, line in enumerate(lines):
        val = line.strip('\n').split(' ')
        if val == ['']:
            validCount += int(isValidPassport(passportData))
            passportData.clear()
            continue
        for v in range(len(val)):
            passportData.update(dict([val[v].split(':')]))
        if i == numberOfLines - 1:
            validCount += int(isValidPassport(passportData))

    print('Total valid passports:', validCount)
