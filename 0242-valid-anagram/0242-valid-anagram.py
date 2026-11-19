class Solution(object):
    def isAnagram(self, s, t):
        """ if len(s)!=len(t):
            return False
        if sorted(s)!=sorted(t):
            return False
        else:
            return True"""

        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in t:
            if i not in freq:
                return False
            freq[i]-=1
        return all(value==0 for value in freq.values())    