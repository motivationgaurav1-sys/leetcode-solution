class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l2=[]
        
        for a in accounts:
            s=sum(a)
            l2.append(s)
        return max(l2)    
        