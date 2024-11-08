# 39. Combination Sum

import itertools


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(path,min_,k):
            if sum(path) == target and result not in list(map(list, itertools.permutations(path))):
                result.append(path)
                return
            elif sum(path) > target:
                return

            for i in range(k,len(candidates)):
                if min_ >= candidates[i]:
                    dfs(path + [candidates[i]],candidates[i],i)
        candidates.sort(reverse=True)
        result = []
        dfs([],10000000,0)
        return result


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
