# 743. Network Delay Time

import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        Q = [(0,k)] # starting vertex
        dist = collections.defaultdict(int) # distance (time, vertex)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time

                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) == n:
            return max(dist.values())
        return -1

print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))