class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product=1
        sum=0
        for a in str(n):
            product*=int(a)
            sum+=int(a)
        return product-sum   
        