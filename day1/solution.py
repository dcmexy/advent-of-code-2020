# Rough solution

# Part 1 - Using for loops


def part1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i] * nums[j]
    return 0

# Part 2 - Using for loops


def part2(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i] * nums[j] * nums[k]
    return 0


# Recursive method to allow for flexible numbers to sum.
def recursiveSolution(nums, target, parts):
    # parts = how many numbers to sum
    if len(nums) == 0 or parts == 0 or target == 0:
        return 0

    # Get first item in the list
    head = nums[0]
    tail = nums[1:]
    # print("Target: ", target)

    # Check if head matches target
    if head == target and parts == 1:
        return head

    val = recursiveSolution(tail, target - head, parts - 1)
    if val > 0:
        return val * head
    return recursiveSolution(tail, target, parts)


# Read file
with open('input.txt') as f:
    nums = []
    for line in f:
        nums.append(int(line.strip('\n')))

# Execute
print("Solution 1 with for loop:", part1(nums, 2020))
print("Solution 2 with for loop:", part2(nums, 2020))
print("Solution 1 with recursive:", recursiveSolution(nums, 2020, 2))
print("Solution 2 with recursive:", recursiveSolution(nums, 2020, 3))
