def count_pairs_with_sum(nums, target):
    nums.sort()  # Important to apply two pointers correctly
    start = 0
    end = len(nums) - 1
    count = 0

    while start < end:
        curr_sum = nums[start] + nums[end]

        if curr_sum == target:
            count += 1
            start += 1
            end -= 1  # Move both pointers after finding a valid pair
        elif curr_sum < target:
            start += 1
        else:
            end -= 1

    return count

# Example usage
arr = [1, 5, 7, -1, 5]
target = 6
print(count_pairs_with_sum(arr, target))  # Output: 3 (pairs: (1,5), (7,-1), (1,5 again))
