# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import Counter, defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderFrq = defaultdict(int)
        remainderFrq[0] = 1
        
        res = prefixSum = 0
        for n in nums:
            prefixSum += n
            remainder = prefixSum % k
            res += remainderFrq[remainder]
            remainderFrq[remainder] += 1
        return res
    
# Another way to solve:
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        return sum(map(
            lambda n: n * (n - 1) // 2,
            Counter(accumulate(nums, lambda a, x: (a + x % k) % k, initial=0)).values(),
        ))
