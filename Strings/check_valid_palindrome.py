def palindrome(s):
    s = list(s)
    s = [char.lower() for char in s if char.isalnum()]
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Example usage
s = "A man, a plan, a canal: Panama"
print(palindrome(s))  # True
"""⏱ Time Complexity:
O(n) — because you traverse the string once to filter and once to check palindrome.

📦 Space Complexity:
O(n) — for the cleaned list (could be optimized if needed to O(1) using in-place checking, but this version is perfect for interviews.)

"""
