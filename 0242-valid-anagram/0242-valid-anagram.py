# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

print(Solution().isAnagram(s = "anagram", t = "nagaram"))