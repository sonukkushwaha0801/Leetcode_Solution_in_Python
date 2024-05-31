# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        distinguishing_bit = xor_all & -xor_all
        unique1 = 0
        unique2 = 0
        for num in nums:
            if num & distinguishing_bit:
                unique1 ^= num
            else:
                unique2 ^= num
        
        return [unique1, unique2]
    
# Simplier solution:
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor^=n

        diffBit = 1

        while not(xor & diffBit):
            diffBit = diffBit<<1

        num1,num2 = 0,0

        for num in nums:
            if num & diffBit:
                num1^=num
            else:
                num2^=num

        return [num1,num2]
        