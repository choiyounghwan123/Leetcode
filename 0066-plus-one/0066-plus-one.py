# 66. Plus One

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(x) for x in str(int("".join(map(str,digits)))+1)]

solution = Solution()
print(solution.plusOne(digits = [1,2,3]))
