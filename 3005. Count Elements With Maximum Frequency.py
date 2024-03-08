# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter
from functools import reduce
from operator import mul


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter = Counter(nums)
        max_freq = max(counter.values())
        return sum(freq for freq in counter.values() if freq == max_freq)
    
# Another way:
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        return reduce(mul, max(Counter(Counter(nums).values()).items()))