# 973. K Closet Points to Origin

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x,y in points:
            heapq.heappush(heap, ((x ** 2 + y ** 2) ** 1/2, x,y))

        result = []

        for i in range(k):
            a,x,y = heapq.heappop(heap)
            result.append([x,y])
        return result

print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))