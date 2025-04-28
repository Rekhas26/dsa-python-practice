def reverse_string(s):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s=list(s)
        left,right=0,len(s)-1
        
        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return ''.join(s)
        


# Example usage
s = 'hello'
print(reverse_string(s))  #
"""✅ Time Complexity = O(n)
✅ Space Complexity = O(n) (because you made a list copy)

"""
