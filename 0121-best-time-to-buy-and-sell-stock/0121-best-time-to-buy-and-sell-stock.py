class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """mini=prices[0]
        
        profit=0
        for i in range(1,len(prices)):
            mini=min(prices[i],mini)
            today_profit=prices[i]-mini
            profit=max(today_profit,profit)
        return profit     """   
        mp=float("inf")
        mx=0
        for price in prices:
            if price<mp:
                mp=price
            elif price-mp>mx:
                mx=price-mp
        return mx   

