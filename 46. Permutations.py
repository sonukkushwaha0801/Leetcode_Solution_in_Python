# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(nums, path): 
            if not nums: 
                result.append(path) 
                return 
            for i in range(len(nums)): 
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
        result = [] 
        backtrack(nums, []) 
        return result 

# Another way:
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permutations(nums)