# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        moves = 0
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                prev += 1
                moves += prev - nums[i]
            else:
                prev = nums[i]
        
        return moves
    
# Another way:
class Solution:
    def minIncrementForUnique(self, nums):
        max_val = 0
        min_val = float('inf')
        arr = [0] * (10**5 + 1)
        for x in nums:
            if x < min_val:
                min_val = x
            if x > max_val:
                max_val = x
            arr[x] += 1
        exp = min_val
        cost = 0
        for i in range(min_val, max_val + 1):
            for y in range(arr[i]):
                if i > exp:
                    exp = i + 1
                else:
                    cost += (exp - i)
                    exp += 1
        return cost