# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
    
# Type Two:
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            goal = i if i + nums[i] >= goal else goal
        return goal == 0