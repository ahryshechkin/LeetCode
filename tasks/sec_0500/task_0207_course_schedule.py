from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            visited[node] = 2

            return True

        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre] = graph.get(pre, []) + [course]

        visited = [0] * numCourses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
