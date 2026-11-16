class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2=""
        max_len=0
        for a in range(len(s)):
            if s[a] not in s2:
                s2+=s[a]
            else:
                current_len=len(s2)
                max_len=max(current_len,max_len)
                while s[a] in s2:
                    s2=s2[1:]
                s2+=s[a] 
            current_len=len(s2)
            max_len=max(current_len,max_len)       
        return max_len
                


        