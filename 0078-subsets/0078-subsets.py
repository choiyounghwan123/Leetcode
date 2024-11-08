# 78. Subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(index,path):
            if len(path) > len(nums):
                return

            result.append(path)

            for i in range(index,len(nums)):
                dfs(i+1, path + [nums[i]])

        result = []
        dfs(0,[])
        return result

print(Solution().subsets(nums = [1,2,3]))

# output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]