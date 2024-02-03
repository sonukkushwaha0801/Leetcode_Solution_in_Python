# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        occurrences = Counter(nums)
        for n in nums:
            if occurrences[n] == 1:
                return n

# Another way:
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return ((3*sum((set(nums))))-sum(nums))//2