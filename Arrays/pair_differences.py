def pair_difference(nums, target):
    start = 0
    end = 1  # Important: end starts just after start

    while start < len(nums) and end < len(nums):
        diff = nums[end] - nums[start]
        if start != end and diff == target:
            return True
        elif diff < target:
            end += 1
        else:
            start += 1
    return False

# Example usage
arr = [1, 5, 8, 12, 15]
print(pair_difference(arr, 7))  # Output: True (8-1 = 7)
print(pair_difference(arr, 20)) # Output: False
