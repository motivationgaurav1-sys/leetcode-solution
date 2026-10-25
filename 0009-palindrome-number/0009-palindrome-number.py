class Solution(object):
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
        """if str(x)==str(x)[::-1]:
            return True
        else:
            return False   """