class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """l2=[]
        for a in nums:
            l2.append(a**2)
        return sorted(l2) """  
        return sorted(x**2 for x in nums) 
        