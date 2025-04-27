def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum from 0 to n
    actual_sum = sum(nums)           # Sum of given array
    return expected_sum - actual_sum # Missing number

print(missing_number([3,0,1]))
