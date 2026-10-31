class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        for a in s:
            freq[a]= freq.get(a,0)+1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i 
        return -1                   



        """for a in range(len(s)):
            b=s.count(s[a])
            if b==1:
                return a
        return -1"""



