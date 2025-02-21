# 75. Sort Colors

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]



solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))