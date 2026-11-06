class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a]==nums[b]:
                        count+=1
        return count
                        


        