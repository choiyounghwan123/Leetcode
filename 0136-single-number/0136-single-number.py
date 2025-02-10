class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hash_map = dict()

        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        return min(hash_map, key=hash_map.get)
        