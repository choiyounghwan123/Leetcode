# 217. Contains Duplicate

import collections

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = collections.defaultdict(int)

        for num in nums:
            if hash_map[num] > 0:
                return True
            hash_map[num] += 1
        return False

print(Solution().containsDuplicate(nums = [1,2,3,1]))