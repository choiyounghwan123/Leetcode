# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = dict()

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                return True
        return False
solution = Solution()
print(solution.containsDuplicate( nums = [1,2,3,1]))