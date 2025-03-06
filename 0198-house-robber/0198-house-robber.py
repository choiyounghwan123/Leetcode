# 198. House Robber

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(3,len(nums)+1):
            if i == 3:
                dp[i] = nums[i - 1] + max( dp[i - 2], dp[i - 3])
                continue
            dp[i] = nums[i-1] + max(dp[i-4],dp[i-2],dp[i-3])
        print(dp)
        print(max(dp))
        return max(dp)



solution = Solution()
print(solution.rob(nums = [1,2,3,1]))