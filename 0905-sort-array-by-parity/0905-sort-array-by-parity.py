# 905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        nums.sort(key=lambda x:x %2)
        return nums

solution = Solution()
print(solution.sortArrayByParity(nums = [3,1,2,4]))