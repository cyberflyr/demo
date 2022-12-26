from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for course in prerequisites:
            edges[course[1]].append(course[0])
            indeg[course[0]] += 1

        q = collections.deque(
            [index for index in range(numCourses) if indeg[index] == 0]
        )
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses
