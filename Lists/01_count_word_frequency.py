
"""
Problem:
Count the frequency of each word in a string.

Example:
Input: "apple banana apple orange banana apple"
Output: {'apple': 3, 'banana': 2, 'orange': 1}

Approach:
- Split the string into words
- Use a dictionary to count occurrences

"""

# Code
text = "apple banana apple orange banana apple"
output_dict = {}
words = text.split()

for word in words:
    if word in output_dict:
        output_dict[word] += 1
    else:
        output_dict[word] = 1

print(output_dict)

# Time Complexity: O(n)
# Space Complexity: O(n)
