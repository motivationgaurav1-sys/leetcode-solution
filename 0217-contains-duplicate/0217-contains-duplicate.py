class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """freq={}
        
        for a in nums:
            freq[a]=freq.get(a,0)+1
        if any(x>=2 for x in freq.values()):
            return True
        else:
            return False  """ 
        return len(nums)!=len(set(nums))     


        