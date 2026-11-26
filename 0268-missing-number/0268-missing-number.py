class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       

        n=len(nums)
        actual_sum=n*(n+1)//2
        missing_num=actual_sum-sum(nums)
        return missing_num
        