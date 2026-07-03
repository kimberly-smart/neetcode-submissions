class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxprofit = 0

        for sell in prices:
            if sell < buy:
                buy = sell
            
            maxprofit = max(maxprofit, sell-buy)

        return maxprofit
            