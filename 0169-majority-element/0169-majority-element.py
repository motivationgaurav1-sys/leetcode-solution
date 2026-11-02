class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """freq={}
        for a in nums:
            freq[a]=freq.get(a,0)+1
        return max(freq,key=freq.get)"""
        maj=nums[0]
        cnt=1
        for i in range(1,len(nums)):
            if maj==nums[i]:
                cnt+=1
            elif cnt>0:
                cnt-=1
            else:
                maj=nums[i]
                cnt=1
        return maj        

          
        