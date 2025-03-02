# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash_map = dict()
        result = []
        for num in nums1:
            hash_map[num] = hash_map.get(num,0) + 1

        for num in nums2:
            if num in hash_map and hash_map[num] != 0:
                result.append(num)
                hash_map[num] -=1
        return result

solution = Solution()
print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))