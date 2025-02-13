# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = dict()
        for char in ransomNote:
            hash_map[char] = hash_map.get(char,0) + 1

        for char in magazine:
            if char not in hash_map:
                continue
            hash_map[char]-=1

        for key,value in hash_map.items():
            if value > 0:
                return False
        return True

solution = Solution()
print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))