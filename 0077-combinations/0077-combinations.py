# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(i,path):
            if len(path) == k:
                result.append(path)
                return
            for j in range(i,n+1):
                dfs(j+1,path + [j])

        result = []
        dfs(1,[])
        return result


print(Solution().combine(n = 4, k = 2))