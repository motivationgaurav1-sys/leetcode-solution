class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        l2=[]
        for a in sentences:
            l1=a.split()
            s=len(l1)
            l2.append(s)
        return max(l2)    
