# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(combinations(range(1, n+1), k))
    
# Another way:
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        pool = tuple(range(1, n+1))
        n = len(pool)
        indices = list(range(k))
        res = [tuple(pool[i] for i in indices)]
        while True:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break
            else:
                return res
            indices[i] += 1
            for j in range(i+1, k):
                indices[j] = indices[j-1] + 1
            res.append(tuple(pool[i] for i in indices))