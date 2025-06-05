class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.prefix_sums=[]
        curr_sum=0
        for weight in w:
            curr_sum+=weight
            self.prefix_sums.append(curr_sum)
        self.total_sum=curr_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        target= random.randint(1, self.total_sum)
        #compute binary search to find the index
        left,right = 0, len(self.prefix_sums)-1
        while left<right:
            mid = (left+right)//2
            if self.prefix_sums[mid] <target:
                left=mid+1
            else:
                right=mid
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
