# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = dict()
        for char in magazine:
            hash_map[char] = hash_map.get(char,0) + 1

        for c in ransomNote:
            if c not in hash_map or hash_map[c] <= 0:
                return False
            hash_map[c] -= 1
        return True




solution = Solution()
print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))