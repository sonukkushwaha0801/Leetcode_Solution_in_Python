# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(); return nums[k*-1]
    
# Another way:
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]