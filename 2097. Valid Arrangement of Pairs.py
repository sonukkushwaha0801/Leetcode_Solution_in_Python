# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        
        stack = [start_node]
        path = []
        
        while stack:
            node = stack[-1]
            if graph[node]:
                next_node = graph[node].popleft()
                stack.append(next_node)
            else:
                path.append(stack.pop())
        
        path.reverse()
        result = [[path[i], path[i+1]] for i in range(len(path) - 1)]
        return result
    
# Another way:
from collections import defaultdict, deque
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        # Build the graph and track in/out degrees
        for src, dest in pairs:
            adj_list[src].append(dest)
            out_degree[src] += 1
            in_degree[dest] += 1

        # Find the starting node
        start_node = pairs[0][0]
        for node in adj_list:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
 
        # Hierholzer's algorithm to find the Eulerian path
        stack = [start_node]
        result = []

        while stack:
            while adj_list[stack[-1]]:
                next_node = adj_list[stack[-1]].popleft()
                stack.append(next_node)
            result.append(stack.pop())
        
        # Reverse the path to get the correct order
        result.reverse()
        return [[result[i], result[i+1]] for i in range(len(result) - 1)]