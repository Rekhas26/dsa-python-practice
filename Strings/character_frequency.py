def char_count(s):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """s=list(s)
        left,right=0,len(s)-1"""
        
        d = {}
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
        return d
            
     
        


# Example usage
s = "madam"
print(char_count(s))  #
