# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import collections
from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)

# Another way:
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict.pop(i)
        return int(*dict)
    
# Adddition one :
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        mydict = collections.Counter(nums)
        for i in mydict:
            if mydict[i]==1:
                return i