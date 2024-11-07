# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

from logging import log
from typing import List


class Solution:
    def largestCombination(self, a: List[int]) -> int:
        return max(sum(v>>i&1 for v in a) for i in range(int(log(max(a),2))+1))
    

# Another way:
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0] * 30

        for i in candidates:
            for j in range(30):
                if i & (1 << j):
                    res[j] += 1

        max_count = max(res)
        return max_count