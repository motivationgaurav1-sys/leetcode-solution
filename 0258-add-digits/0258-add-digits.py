class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
      
        while num>=10:
            sum=0
            for a in str(num):
                sum+=int(a)
            num=sum 
        return num      
                
                   
        