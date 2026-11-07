class Solution(object):
    def isPowerOfTwo(self, n):

        """
        :type n: int
        :rtype: bool
        """
        import math
        if n==1:
            return True
        a=0    
        while 2**a<=n:
            if n==2**a:
                return True 
            a+=1
        return False         
        