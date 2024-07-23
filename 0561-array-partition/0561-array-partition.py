class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()
        pair = []

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum
