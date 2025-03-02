# 53. Maximum Subarray

"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [nums[0]]

        for i in range(1,len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
        return max(dp)


"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

solution = Solution()
print(solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))