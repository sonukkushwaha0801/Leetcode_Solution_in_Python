# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def explore(index, curr):
            if index == len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[index])
            explore(index + 1, curr)
            curr.pop()
            explore(index + 1, curr)

        explore(0, [])
        return result
    
# Another way:
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        
        return result