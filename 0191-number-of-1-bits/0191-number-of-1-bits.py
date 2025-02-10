# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        return format(n,'b').count("1")

solution = Solution()
print(solution.hammingWeight(n = 2147483645))