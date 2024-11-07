# 46. Permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(path):
            if len(path) == len(nums):
                print(path)
                result.append(path)
                return
            print(path)
            for i in range(len(nums)):
                if nums[i] not in path:
                    dfs(path + [nums[i]])


        result = []
        dfs([])
        return result

print(Solution().permute(nums = [1,2,3]))