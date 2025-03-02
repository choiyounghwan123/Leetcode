# 189. Rotate Array


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(k):
            nums.insert(0,nums.pop())
        print(nums)

solution = Solution()
print(solution.rotate(nums = [1,2,3,4,5,6,7], k = 3))