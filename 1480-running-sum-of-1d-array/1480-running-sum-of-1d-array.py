class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l2=[]
        total=0
        for i in nums:
            total+=i
            l2.append(total)
        return l2    