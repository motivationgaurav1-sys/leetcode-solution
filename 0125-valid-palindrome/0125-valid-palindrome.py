class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s1=""
        for a in s:
            if a.isalnum():
                s1+=str(a)
        return s1==s1[::-1]        