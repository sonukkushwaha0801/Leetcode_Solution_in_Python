# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

import heapq


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        _sum = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1

# Another way:
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        sum_val = sum(nums)
        nums = [-x for x in nums]  # convert to min-heap
        heapq.heapify(nums)
        
        while len(nums) > 2:
            num = heapq.heappop(nums)
            if sum_val > 2 * (-num):
                return sum_val
            sum_val -= (-num)
        
        return -1