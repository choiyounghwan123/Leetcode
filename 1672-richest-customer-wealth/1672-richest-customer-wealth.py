# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        result = []

        for account in accounts:
            prefixSum = [0]

            for i in range(len(account)):
                prefixSum.append(prefixSum[i] + account[i])
            result.append(prefixSum[-1])
        return max(result)


solution = Solution()
print(solution.maximumWealth(accounts = [[1,2,3],[3,2,1]]))