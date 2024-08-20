# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]
        
        def helper(i, M):
            if i >= n:
                return 0
            if (i, M) in dp:
                return dp[(i, M)]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                if i + X <= n:
                    max_stones = max(max_stones, suffix_sum[i] - helper(i + X, max(M, X)))
            
            dp[(i, M)] = max_stones
            return max_stones
        
        return helper(0, 1)
    
# Another way:
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        suffix_sums = tuple(reversed(tuple(accumulate(reversed(piles)))))

        @cache
        def score(i: int, m: int) -> int:
            return (i < len(piles)) and max(suffix_sums[i] - score(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        
        return score(0, 1)
