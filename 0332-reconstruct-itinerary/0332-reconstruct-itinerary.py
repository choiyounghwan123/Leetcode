# 332. Reconstruct Itinerary

import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)
        for a,b in sorted(tickets):
            graph[a].append(b)
        print(graph)
        def dfs(departure):
            while graph[departure]:
                dfs(graph[departure].pop(0))
            result.append(departure)
        result = []

        dfs("JFK")

        return result[::-1]

print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))