# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from cmath import inf
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dic = {end: [end-1] for end in range(1, n)} # add the original 1-step arrows
        res = []
        for j in range(len(queries)):
            dp = [0 if i == 0 else n for i in range(n)]
            dic[queries[j][1]].append(queries[j][0])
            # below, each query will be visited at most once so it's not really a "nested" loop
            for i in range(1, n):
                for start in dic[i]:
                    dp[i] = min(dp[i], dp[start]+1)
            res.append(dp[-1])
        return res
    
# Another way:
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        hs = defaultdict(list)
        for i in range(n):
            if i + 1 < n:
                hs[i].append(i + 1)
        sm = inf
        arr = []
        for i, j in queries:
            hs[i].append(j)
            queue = deque([(0, 0)])
            seen = set()
            while queue:
                node, path = queue.popleft()
                # print(hs, node)
                seen.add(node)
                for i in hs[node]:
                    if i in seen:
                        continue
                    if i == n - 1:
                        # print(i, path + 1)
                        sm = min(sm, path + 1)
                        queue = []
                        break
                    queue.append((i, path + 1))
            arr.append(sm)
        return arr
        