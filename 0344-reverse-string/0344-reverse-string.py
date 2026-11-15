class Solution(object):
    def reverseString(self, s):
        
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        """left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1"""  
        """s.reverse()"""
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s    
            
        
          

