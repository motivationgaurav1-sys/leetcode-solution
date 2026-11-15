class Solution(object):
    def isPalindrome(self, x):
        """x=str(x)
        return x==x[::-1]"""
        s=str(x)
        i=0
        j=len(s)-1
        
        for i in range(len(s)):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True        
           
            