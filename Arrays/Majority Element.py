def majority_element(arr):
    n = len(arr)
    count_dict = {}
    
    # Traverse the array and update the count in the dictionary
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the element whose count is greater than or equal to n/2
    for num, count in count_dict.items():
        if count >= n // 2:
            return num
    return None  # In case there's no majority element, though the problem guarantees one.

# Test case
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Majority Element is:", majority_element(arr))  # Output: 4
