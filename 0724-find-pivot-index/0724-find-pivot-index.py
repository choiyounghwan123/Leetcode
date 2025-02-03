# 724. Find pivot index

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        prefixSum = 0

        for i in range(len(nums)):
            if prefixSum == sum(nums[i+1:]):
                return i
            else:
                prefixSum += nums[i]
        return -1


solution = Solution()
print(solution.pivotIndex(nums = [1,7,3,6,5,6]))

