# Solution for Day 9 - Part 1

# function to process the data (cipher)
# takes in data and preamble (p)


def processCipher(data, p):
    i = 0
    x = []
    for j in range(i + p, len(data)):
        for k in range(i, i + p):
            for l in range(k + 1, i + p):
                dejavu = data[j]
                # validate number and track
                if data[j] == data[k] + data[l] and data[k] != data[l]:
                    x.append(data[j])

        # check for first non valid number
        if data[j] not in x:
            return data[j]
        i += 1
    return False

# Part 2 of Day 10 solution


def process2(data, res):
    for i in range(len(data)):
        total = data[i]
        js = [data[i]]
        for j in range(i + 1, len(data)):
            total += data[j]
            js.append(data[j])
            if total >= res:
                break

        if total == res:
            # return the max and min of range
            return min(js) + max(js)


# Read data from file
with open('input.txt') as f:
    data = []
    for line in f:
        data.append(int(line.strip()))
    # Execute processCipher is a preamble of 25
    res = processCipher(data, 25)
    print(res)

    # execute part 2
    print(process2(data, res))
