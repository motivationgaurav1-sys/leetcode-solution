class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        prefix=[0]
        sums=0
        for a in nums:
            sums+=a
            prefix.append(sums)
        self.prefix=prefix

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)