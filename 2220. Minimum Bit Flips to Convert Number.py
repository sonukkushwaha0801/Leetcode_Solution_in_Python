# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_value = start ^ goal
        return bin(xor_value).count('1')

# Another way:
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start != 0 or goal != 0:
            count += (start & 1) ^ (goal & 1)
            start = start >> 1
            goal = goal >> 1
        return count