from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inv = [0 for i in range (0, numCourses)]
        frees = [[] for i in range (0, numCourses)]
        nex = []

        for v in prerequisites:
            inv[v[0]] += 1
            frees[v[1]].append(v[0])

        for i in range (0, numCourses):
            if inv[i] == 0:
                nex.append(i)

        i = 0
        while i < len(nex):
            c = nex[i]
            for vv in frees[c]:
                inv[vv] -= 1
                if inv[vv] == 0:
                    nex.append(vv)
            i +=1
        
        if len(nex) == numCourses:
            return nex
        return []