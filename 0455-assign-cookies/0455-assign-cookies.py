# 455. Assign Cookies

import heapq

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        child_index = size_index = 0

        while child_index < len(g) and size_index < len(s):
            if g[child_index] <= s[size_index]:
                child_index += 1
            size_index += 1
        return child_index


print(Solution().findContentChildren( g = [1,2,3], s = [3]))