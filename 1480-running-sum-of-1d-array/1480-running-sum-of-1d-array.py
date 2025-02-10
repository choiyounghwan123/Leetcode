# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [0]

        for num in nums:
            result.append(result[-1] + num)
        return result[1:]

solution = Solution()
print(solution.runningSum(nums = [1,2,3,4]))