# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([x*x for x in nums])
    
# Another way:
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i**2 for i in nums])