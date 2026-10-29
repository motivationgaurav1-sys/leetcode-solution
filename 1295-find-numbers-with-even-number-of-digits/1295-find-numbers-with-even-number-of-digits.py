class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """l2=[]
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
        return c"""  


        """c=0
        for a in nums:
            digits=len(str(a))
            if digits%2==0:
                c+=1
        return c"""


        count=0
        for  num in nums:
            if num<100 and num>=10:
                count+=1
            elif num<10000 and num>=1000:
                count+=1
            elif num ==100000:
                count+=1
        return count                
            




        