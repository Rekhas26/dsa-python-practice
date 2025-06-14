"""class SparseVector:
    def __init__(self, nums):
        self.non_zero = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec):
        result = 0
        for i in self.non_zero:
            if i in vec.non_zero:
                result += self.non_zero[i] * vec.non_zero[i]
        return result"""

class SparseVector:
    def __init__(self, nums):
        self.nums=[]
        for i,num in enumerate(nums):
            if num:
                self.nums.append((i,num))      
    def dotProduct(self, vec):
        result = 0
        i=j=0

        while i<len(self.nums) and j<len(vec.nums):
            i_idx, i_num=self.nums[i]
            j_idx, j_num = vec.nums[j]

            if i_idx==j_idx:
                result+=(i_num*j_num)

                i+=1
                j+=1
            elif i_idx>j_idx:
                j+=1
            else:
                i+=1
        return result



