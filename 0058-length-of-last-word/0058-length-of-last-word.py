# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

solution = Solution()
print(solution.lengthOfLastWord(s = "   fly me   to   the moon  "))