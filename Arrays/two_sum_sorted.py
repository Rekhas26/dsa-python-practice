def two_sum_sorted(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        current_sum = arr[start] + arr[end]
        
        if current_sum == target:
            return True
        elif current_sum < target:
            start += 1
        else:
            end -= 1
    
    return False

# Example usage:
print(two_sum_sorted([1, 2, 3, 9], 8))  # Output: False
print(two_sum_sorted([1, 2, 4, 4], 8))  # Output: True
