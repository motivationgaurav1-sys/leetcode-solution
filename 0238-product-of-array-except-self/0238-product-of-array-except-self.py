class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        n=len(nums)
        result=[1]*n
        for i in range(n):
            result[i]=product
            product*=nums[i]
        product=1    
        for i in range(n-1,-1,-1):
            result[i]*=product
            product*=nums[i]       
        return result
            