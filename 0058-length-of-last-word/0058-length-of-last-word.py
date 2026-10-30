class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1=s.split()
        x=l1[-1]
        return len(x)
