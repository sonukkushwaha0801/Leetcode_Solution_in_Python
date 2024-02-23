# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import defaultdict, deque
import heapq


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        adj = defaultdict(list)
        visited = [float('inf')] * n
        visited[src] = 0
        
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
            
        queue = deque([(src, 0)])
        K += 1
        
        while K > 0 and queue:
            size = len(queue)
            while size > 0:
                curr_node, curr_price = queue.popleft()
                for neighbor, price in adj[curr_node]:
                    new_price = curr_price + price
                    if new_price < visited[neighbor]:
                        visited[neighbor] = new_price
                        queue.append((neighbor, new_price))
                size -= 1
            K -= 1
        
        return visited[dst] if visited[dst] != float('inf') else -1
    
# Another way:
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for frm,to,price in flights:
            graph[frm].append((to,price))

        heap = [(0,0,src)] #price,stops,city
        visited = {}

        while heap:
            price,stops,city = heapq.heappop(heap)

            if stops>k+1:
                continue
            
            if city==dst:
                return price

            if city in visited and visited[city]==stops:
                continue

            visited[city] = stops

            for nei,p in graph[city]:
                if nei not in visited or visited[nei]>stops:
                    heapq.heappush(heap,(price+p,stops+1,nei))

        return -1