# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        reachable_cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_cities[i] += 1
        
        min_reachable = float('inf')
        result_city = -1
        for i in range(n):
            if reachable_cities[i] <= min_reachable:
                if reachable_cities[i] < min_reachable or i > result_city:
                    min_reachable = reachable_cities[i]
                    result_city = i
        
        return result_city
    
# Another way:
def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cost=[[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
        for u,v,d in edges:
            cost[u][v]=d
            cost[v][u]=d
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j]=min(cost[i][j],cost[i][via]+cost[via][j])
        d={}
        for i in range(n):
            c=0
            for j in range(n):
                if cost[i][j]<=distanceThreshold and i!=j:
                    c+=1
            d[i]=c
        m1=min(d.values())
        m2=0
        for k,v in d.items():
            if m1==v:
                m2=max(m2,k)
        return m2