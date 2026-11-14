class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority=nums[0]
        count=1
        for i in range(1,len(nums)):
            if majority==nums[i]:
                count+=1
            elif count>0:
                count-=1
            else:
                majority=nums[i]
                count=1
        return majority           

          
        