# 349. Intersection of Two Arrays

import bisect

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2 = sorted(nums2)

        result:set = set()

        for n1 in nums1:
            i2 = bisect.bisect_left(nums2,n1)
            if i2 < len(nums2) and n1 == nums2[i2]:
                result.add(n1)
        return list(result)



print(Solution().intersection(nums1 = [1,2], nums2 = [1,1]))