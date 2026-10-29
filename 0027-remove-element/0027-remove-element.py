class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for a in nums:
            if a!=val:
                nums[k]=a
                k+=1
        return k        