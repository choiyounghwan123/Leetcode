# Best Time to Buy and Sell Stock
import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = sys.maxsize
        max_price = 0

        for price in prices:
            min_price = min(min_price,price)
            max_price = max(max_price,price-min_price)
        return max_price
