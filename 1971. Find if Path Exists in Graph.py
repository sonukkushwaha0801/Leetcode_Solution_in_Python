# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        visited = [False for i in range(n)]
        vc = 0
        for i in range(len(edges)):
            if edges[i][0] == source or visited[edges[i][0]] == True:
                visited[edges[i][1]] = True
            elif edges[i][1] == source or visited[edges[i][1]] == True:
                visited[edges[i][0]] = True
            if visited[destination] == True:
                return True
        while visited.count(True)>vc:
            vc = visited.count(True)
            for i in range(len(edges)):
                if edges[i][0] == source or visited[edges[i][0]] == True:
                    visited[edges[i][1]] = True
                elif edges[i][1] == source or visited[edges[i][1]] == True:
                    visited[edges[i][0]] = True
                if visited[destination] == True:
                    return True
        return False

# Another way:
class Solution(object):
    def validPath(self, n, edges, start, end):
        visited = [False]*n
        d = {}

        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
                
            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]] = [i[0]]

        q = [start]
        while q:
            curr = q.pop(0) 
            if curr == end:
                return True
            elif curr in d and not visited[curr]:
                q.extend(d[curr])
            visited[curr] = True 
        return False