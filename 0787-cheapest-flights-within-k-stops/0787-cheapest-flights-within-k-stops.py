# 787. Cheapest Flights K Stops

import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        Q = [(0,0,src)]
        dist = collections.defaultdict(int)
        while Q:
            k_,time,node = heapq.heappop(Q)

            if node not in dist or dist[node] > time and k_ <= k+1 :
                dist[node] = time
                for v,w in graph[node]:
                    print(v,w)
                    alt = time + w
                    if k_  <= k:
                        heapq.heappush(Q, ( k_+1,alt,v))
        if dist[dst] == 0:
            return -1
        return dist[dst]


print(Solution().findCheapestPrice(  n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))