# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)-1):
            if hash_map[s[i]] < hash_map[s[i+1]]:
                result -= hash_map[s[i]]
            else:
                result += hash_map[s[i]]
        return result + hash_map[s[-1]]

solution = Solution()
print(solution.romanToInt(s = "III"))