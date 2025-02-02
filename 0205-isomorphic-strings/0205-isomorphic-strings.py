# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            else:
                if dict1[s[i]] != t[i]:
                    return False
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            else:
                if dict2[t[i]] != s[i]:
                    return False
        return True

solution = Solution()
print(solution.isIsomorphic(s="babc", t="baba"))
