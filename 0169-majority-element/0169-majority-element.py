# 169. Majority Element

import collections
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        for i in range(len(nums)):
            if counts[nums[i]] == 0:
                counts[nums[i]] = nums.count(nums[i])
            if counts[nums[i]] > len(nums) // 2:
                return nums[i]
print(Solution().majorityElement(nums = [1]))