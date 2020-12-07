# Part 1 solution for day 7.
bags = {}


def processBag(bag):
    #parentBag = bag[0]
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


    # Read data from file
with open('input.txt') as f:
    for line in f:
        bags.update(processBag(line.strip('.\n').split(' contain ')))

    print(findBags(['shiny gold'], 0))
