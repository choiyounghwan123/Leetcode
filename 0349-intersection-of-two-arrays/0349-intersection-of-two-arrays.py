# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result:set = set()

        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)
        return list(result)


print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))