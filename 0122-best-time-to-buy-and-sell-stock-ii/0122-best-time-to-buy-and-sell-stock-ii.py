# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        return profit

print(Solution().maxProfit(prices = [7,1,5,3,6,4]))