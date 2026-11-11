class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2=""
        max_len=0
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
        """left=0
        seen=set()
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            current_len=right-left+1
            max_len=max(max_len,current_len)    
        return max_len"""


        

        