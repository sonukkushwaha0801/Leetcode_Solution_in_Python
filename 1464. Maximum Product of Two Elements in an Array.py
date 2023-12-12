# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
from heapq import nlargest
from math import prod


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums=sorted(nums)
        return (nums[-1]-1) * (nums[-2]-1)

# Another way:
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        return prod(x-1 for x in nlargest(2,nums))        