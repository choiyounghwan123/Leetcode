# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = dict()
        for c in s:
            hash_map[c] = hash_map.get(c,0) + 1
        
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        
        return -1

        

solution = Solution()
print(solution.firstUniqChar(s = "leetcode"))