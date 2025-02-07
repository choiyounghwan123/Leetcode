# 1. Two Sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = dict()

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [i,hash_map[target - nums[i]]]
            else:
                hash_map[nums[i]] = i



solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))