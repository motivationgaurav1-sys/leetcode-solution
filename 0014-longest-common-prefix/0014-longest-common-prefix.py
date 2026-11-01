class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s2=""
        for i in range(len(strs[0])):
            for a in strs:
                if i>=len(a) or a[i]!=strs[0][i]:
                    return s2       
            s2+=strs[0][i]    
        return s2            


        