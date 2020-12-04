import re

# Validate Passport


def isValidPassport(passport):
    dataKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    if len(passport) < 7:
        return False

    for key, value in passport.items():
        if not validateField(key, value):
            return False

    return ((len(passport) >= 7 and 'cid' not in passport.keys()) or len(passport) == 8)

# Validate individual Fields


def validateField(key, value):
    # Validate Country ID - ignored, missing or not
    if key == 'cid':
        return True
    # Validate Birth Year - four digits; at least 1920 and at most 2002.
    if key == 'byr':
        return int(value) >= 1920 and int(value) <= 2002

    # Validate Issue Year - four digits; at least 2010 and at most 2020.
    if key == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020

    # Validate Expiration Year - four digits; at least 2020 and at most 2030.
    if key == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030

    # Validate Height - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    #  reIf in, the number must be at least 59 and at most 76.
    if key == 'hgt':
        if re.search('in$', value):
            height = int(value.split('in')[0])
            return height >= 59 and height <= 76
        if re.search('cm$', value):
            height = int(value.split('cm')[0])
            return height >= 150 and height <= 193

    # Validate Hair Color - a # followed by exactly six characters 0-9 or a-f.
    if key == 'hcl':
        return True if re.search('^#(?:[0-9a-f]{6})$', value) else False

    # Validate Eye Color - exactly one of: amb blu brn gry grn hzl oth.
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    # Validate Passport ID - a nine-digit number, including leading zeroes.

    if key == 'pid':
        return True if re.search('^[0-9]{9}$', value) else False

    # return False by default
    return False


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
