class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """list_sum=[] 
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                    subarray=(nums[i:j+1])
                    list_sum.append(sum(subarray))
        return max(list_sum)  """          
        # above and below code time limit exceed
        """max_sum=nums[0]
        for i in range(len(nums)):
            current_sum=0   
            for j in range(i,len(nums)):
                current_sum+=nums[j]
                if current_sum>max_sum:
                    max_sum=current_sum
        return max_sum"""
        max_sum=nums[0]
        current_sum=nums[0]
        for i in range(1,len(nums)):
            current_sum=max(nums[i],current_sum+nums[i])
            max_sum=max(max_sum,current_sum)
        return max_sum    

            
            






        