# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0

        for i in range(1,len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index],nums[i] = nums[i],nums[index]
        return index + 1

solution = Solution()
print(solution.removeDuplicates(nums = [1,1,2]))