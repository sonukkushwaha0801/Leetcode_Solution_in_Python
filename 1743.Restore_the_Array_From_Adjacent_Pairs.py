# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        n = len(adjacentPairs) + 1
        res = [None] * n
        from collections import defaultdict
        neis = defaultdict(list)
        for a, b in adjacentPairs:
            neis[a].append(b)
            neis[b].append(a)

        for val in neis:
            if len(neis[val]) == 1:
                res[0] = val
                break
        
        for i in range(n - 1):
            left = None if i == 0 else res[i - 1]
            for nei in neis[res[i]]:
                if nei != left:
                    res[i + 1] = nei
                    break
        return res
    
# Another way:
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        n = len(adjacentPairs) + 1
        dict = defaultdict(list)

        for u, v in adjacentPairs:
            dict[u].append(v)
            dict[v].append(u)
        
        for key, value in dict.items():
            if len(value) == 1:
                start_val = key
                break
        
        ans = []
        ans.append(start_val)
        val = dict[start_val][0]
        parent = start_val

        while True:
            ans.append(val)
            if len(dict[val]) == 1:
                break
            u, v = dict[val]
            if u != parent:
                parent, val = val, u
            else:
                parent, val = val, v
        
        return ans

        