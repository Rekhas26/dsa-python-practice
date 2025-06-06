class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums 

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count=0
        result=0
        for i, num in enumerate(self.nums):
            if num == target:
                count+=1
                if random.randint(1, count) == count:
                    result = i
        return result
