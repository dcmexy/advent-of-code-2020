# Part 1 solution for day 7.

# initialize global bag repository
bags = {}

# process and transform data


def processBag(bag):
    # parentBag = bag[0]
    # Get only the parent bag (container) name to eliminate plurality
    # E.g. shinyy gold for both shiny gold bag and shiny gold bags
    parentBag = ' '.join(bag[0].split(' ')[0:-1])

    content = bag[1].split(', ')

    childBags = {}

    # Transform bag contents
    for c in content:
        childBags.update(dict([c.split(' ', 1)[::-1]]))

    # return a dictionart of container bags with contents
    return dict([[parentBag, childBags]])

# Part 1 Solution - find bags containing at least one 'shiny gold' bag


def findBags(bagsToSearch, bagCount):

    for bag, content in bags.items():
        for c in content:
            if any(bts in c for bts in bagsToSearch) and bag not in bagsToSearch:
                # track containerBags
                bagsToSearch.append(bag)

    if len(bagsToSearch) > bagCount:
        findBags(bagsToSearch, len(bagsToSearch))

    # return number of bags tracked less the initial 'shiny gold'
    return len(bagsToSearch) - 1

# Part 2 Solution - find how many individual bags inside a single 'shiny gold' bag


def findBags2(bagsToSearch):
    val = 0
    for bag, numberOfBags in bags[bagsToSearch].items():
        if 'no' in numberOfBags:
            # print(numberOfBags)
            return 0
        bagName = ' '.join(bag.split(' ')[0:-1])
        val += findBags2(bagName) * int(numberOfBags) + int(numberOfBags)
    return val


# Read data from file
with open('input.txt') as f:
    for line in f:
        bags.update(processBag(line.strip('.\n').split(' contain ')))

    print("Part 1 Solution -", findBags(['shiny gold'], 0))
    print("Part 2 Solution -", findBags2('shiny gold'))
