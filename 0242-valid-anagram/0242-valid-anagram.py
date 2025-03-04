# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = dict()

        for c in s:
            hash_map[c] = hash_map.get(c,0) + 1

        for c in t:
            if c in hash_map and hash_map[c] > 0:
                hash_map[c] -= 1
            else:
                return False
        return True

solution = Solution()
print(solution.isAnagram( s = "anagram", t = "nagaram"))