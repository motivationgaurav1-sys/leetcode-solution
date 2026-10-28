class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        """l2=[]
        
        for a in accounts:
            s=sum(a)
            l2.append(s)
        return max(l2)    
        """
        max_wealth=0
        for a in accounts:
            s=sum(a)
            if s>max_wealth:
                max_wealth=s
        return max_wealth        
