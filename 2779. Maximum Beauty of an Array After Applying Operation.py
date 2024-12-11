# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        left = 0
        threshold = k * 2
        for num in sorted_nums:
            if threshold < num - sorted_nums[left]:
                left += 1
        return len(sorted_nums) - left
    
# Another way:
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        i, k2 = 0, k * 2
        for j in range(len(nums)):
            if nums[j] - nums[i] > k2:
                i+=1
        return j - i + 1     