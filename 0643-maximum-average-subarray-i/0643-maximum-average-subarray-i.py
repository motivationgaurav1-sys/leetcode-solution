class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """max_sum=float("-inf")
        for i in range(len(nums)-k+1):
            current_sum=0
            for j in range(i,k+i):
                current_sum+=nums[j]
            max_sum=max(max_sum,current_sum)
        return max_sum/float(k)   """     
# in this code time limit exceed
        window_sum=0
        for i in range(k):
            window_sum+=nums[i]
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,window_sum)
        return max_sum/float(k)

        