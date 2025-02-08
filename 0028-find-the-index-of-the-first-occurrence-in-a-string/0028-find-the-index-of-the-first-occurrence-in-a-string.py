# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        index = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0] :
                for j in range(len(needle)):
                    if j+i >= len(haystack) or haystack[j+i] != needle[j]:
                        break
                else:
                    index = i
                    break
        return index


solution = Solution()
print(solution.strStr(haystack = "mississippi", needle = "issipi"))