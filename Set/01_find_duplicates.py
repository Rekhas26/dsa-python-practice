"""
Problem:
Find all duplicate numbers in a list.

Example:
Input: [1, 2, 3, 2, 4, 5, 1, 6, 3]
Output: [1, 2, 3]

Approach:
- Create a set 'seen' to track numbers we have already seen.
- Create another set 'duplicates' to track numbers that appear more than once.
- Loop through the list:
    - If a number is already in 'seen', add it to 'duplicates'.
    - Otherwise, add the number to 'seen'.
- Finally, convert the 'duplicates' set to a list and print it.

Time Complexity:
O(n), where n is the number of elements in the list.

Space Complexity:
O(n), for storing 'seen' and 'duplicates' sets.
"""

# Code starts here

nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))

# Code ends here
