# 347. Top K Frequent Elements

import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = collections.Counter(nums)
        heap = []
        for f in counter:
            heapq.heappush(heap, (-counter[f],f))

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))