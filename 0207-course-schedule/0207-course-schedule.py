import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)

        # 그래프 초기화
        for i in range(numCourses):
            graph[i] = []

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()  # 방문을 완료한 노드를 저장

        def dfs(i):
            if i in traced:  # 사이클이 존재할 경우 False
                return False
            if i in visited:  # 이미 방문한 노드일 경우 True
                return True

            traced.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            traced.remove(i)
            visited.add(i)  # 방문 완료된 노드로 표시
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False

        return True

# 테스트
print(Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # 출력: False