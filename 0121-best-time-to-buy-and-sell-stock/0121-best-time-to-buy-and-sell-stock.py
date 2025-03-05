# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        min_ = 100000
        max_ = -1
        for i in range(len(prices)):
            if min_ > prices[i]:
                min_ = prices[i]
                max_= min_
                continue
            max_ = max(max_,prices[i])
            result = max(result,max_ - min_)
        return result

solution = Solution()
print(solution.maxProfit(prices = [7,1,5,3,6,4]))