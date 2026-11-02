class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq={}
        for a in magazine:
            freq[a]=freq.get(a,0)+1
        for i in ransomNote:
            if i not in freq or freq[i]==0:
                return False
            freq[i]-=1
        return True        
