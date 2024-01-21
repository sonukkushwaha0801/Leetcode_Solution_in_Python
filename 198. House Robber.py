# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:


from functools import reduce


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3: return max(nums)
        prev, curr = nums[0], max(nums[0], nums[1])
        for n in range(2, len(nums)):
            curr, prev = max(nums[n]+prev, curr), curr
        return curr

# Another way:
class Solution:
    def rob(self, nums: list[int]) -> int:
        return reduce(lambda a, x: (a[1], max(a[1], a[0] + x)), nums, (0, 0))[1]