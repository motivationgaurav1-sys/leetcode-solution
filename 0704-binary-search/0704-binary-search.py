class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """if target in nums:
            return nums.index(target)
        else:
            return -1 """  
        i=0
        j=len(nums)-1 
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                i=mid+1
            else:
                j=mid-1
        return -1                        

             
          
        