# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preReq = collections.defaultdict(list)

        for c,pr in prerequisites:
            preReq[c].append(pr)
        
        res = []

        visit, cycle = set(), set()

        def dfs(c):
            # terminating case
            if c in cycle:
                return False
            
            if c in visit:
                return True
            
            cycle.add(c)
            for pr in preReq[c]:
                if dfs(pr) == False:
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return res
    
# Another way:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preq = {i:set() for i in range(numCourses)}
        graph = collections.defaultdict(set)
        for i,j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)
        
        q = collections.deque([])
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            if len(taken) == numCourses:
                return taken
            for cor in graph[course]:
                preq[cor].remove(course)
                if not preq[cor]:
                    q.append(cor)
        return []