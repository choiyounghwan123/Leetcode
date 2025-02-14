# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)
            

solution = Solution()
print(solution.sortedSquares(nums = [-4,-1,0,3,10]))