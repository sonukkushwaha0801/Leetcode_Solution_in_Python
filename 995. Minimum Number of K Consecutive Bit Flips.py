# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = [False] * (len(nums) + 1)

        result = 0
        current_flips = False
        for i in range(len(nums) - k + 1):
            current_flips ^= flips[i]
            if nums[i] == current_flips:
                result += 1
                current_flips ^= 1
                flips[i + k] = 1

        for i in range(len(nums) - k + 1, len(nums)):
            current_flips ^= flips[i]
            if nums[i] == current_flips:
                return -1

        return result

# Another way:
from collections import deque
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        is_flipped = 0
        flip_positions = deque()
        
        for i in range(n):
            if flip_positions and flip_positions[0] == i:
                flip_positions.popleft()
                is_flipped ^= 1
            
            if nums[i] == is_flipped:
                if i + k > n:
                    return -1
                flip_positions.append(i + k)
                is_flipped ^= 1
                flips += 1
        
        return flips