class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxPrice = 99999, 0, 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]

            elif prices[i] > sell:
                sell = prices[i]
            
            maxPrice = max(maxPrice, sell-buy)
        return maxPrice
            