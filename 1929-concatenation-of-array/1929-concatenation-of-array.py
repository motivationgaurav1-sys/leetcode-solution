class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ans=nums+nums
        return ans"""
        n=len(nums)
        ans=[0]*(2*n)
        for i in range(n):
            ans[i]=nums[i]
            ans[n+i]=nums[i]
        return ans    
