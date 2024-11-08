# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def getMaximumXor(self, a: List[int], q: int) -> List[int]:
        return [2**q-1^x for x in accumulate(a,xor)][::-1]
    
# Another way:
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        max_possible = (1 << maximumBit) - 1
        total_XOR = 0

        for num in nums:
            total_XOR ^= num

        for i in range(len(nums)):
            ans.append(total_XOR ^ max_possible)
            total_XOR ^= nums[-1 - i]

        return ans