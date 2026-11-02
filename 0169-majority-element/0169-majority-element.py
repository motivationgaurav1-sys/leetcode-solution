class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for a in nums:
            freq[a]=freq.get(a,0)+1
        return max(freq,key=freq.get)
          
        