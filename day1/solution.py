# Rough solution

# Part 2


def part1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i] * nums[j]
    return 0

# Part 2


def part2(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i] * nums[j] * nums[k]
    return 0


# Read file
with open('input.txt') as f:
    nums = []
    for line in f:
        nums.append(int(line.strip('\n')))

# Execute
print(part2(nums, 2020))
