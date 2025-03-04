# 344. Reverse String

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))