class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l2=[]
        for a in nums:
            a=str(a)
            count=0
            for i in a:
                count+=1
            l2.append(count)
        c=0    
        for b in l2:
            if b%2==0:
                c+=1 
        return c              




        