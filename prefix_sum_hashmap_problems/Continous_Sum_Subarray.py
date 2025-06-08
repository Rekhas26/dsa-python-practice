class Solution:
    def checkSubarraySum(self, nums, k) :
        # Check for consecutive zeros (special case for k != 0)
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        
        mods = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k

            if prefix_sum in mods:
                if i - mods[prefix_sum] >= 2:
                    return True
            else:
                mods[prefix_sum] = i
        
        return False
