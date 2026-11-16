class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        seen=set()
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            max_len=max(max_len,right-left+1)  
        return max_len    

        """s2=""
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
                """



        