class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2=""
        max_len=0
        i=0
        j=len(s)-1
        for a in s:
            if a not in s2:
                s2+=a
            else:
                current_sub=s2
                if len(current_sub)>max_len:
                    max_len=len(current_sub)
                
                s2=s2[s2.index(a)+1:]
                s2=s2+a
            if len(s2)>max_len:
                max_len=len(s2)    
        return max_len       




        

        