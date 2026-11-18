class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini=prices[0]
        
        profit=0
        for i in range(len(prices)):
            mini=min(prices[i],mini)
            today_profit=prices[i]-mini
            profit=max(today_profit,profit)
        return profit        
