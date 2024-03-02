# Write your solution for algorithm 5 below
def sum(nums, target):
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)

    return 'No pairs sum to the target'

# Example usage
nums = [5, 10, 4, 7, 6, 2]
target = 9
result = sum(nums, target)
print(result)
