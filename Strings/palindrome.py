def palindrome(s):
    s = list(s)                     # Convert string to list if needed
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:      # If mismatch, it's not a palindrome
            return False
        left += 1                    # Move inward
        right -= 1
    return True                      # If no mismatch found, it's a palindrome


print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
