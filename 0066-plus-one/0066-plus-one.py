class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x=""
        for a in digits:
            x+=str(a)
        b=int(x)+1
        b=list(str(b))
        return list(map(int,b))
        
          
