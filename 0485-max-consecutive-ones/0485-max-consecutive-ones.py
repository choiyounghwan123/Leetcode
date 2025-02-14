# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        answer = 0
        pre = 0

        for num in nums:
            if num == 1:
                pre += 1
            else:
                answer = max(answer,pre)
                pre = 0
        return max(answer,pre)



solution = Solution()
print(solution.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))