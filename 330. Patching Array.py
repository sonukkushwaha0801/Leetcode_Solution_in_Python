# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        count = 0
        index = 0
        while patch < n:
            if index < len(nums) and patch + 1 >= nums[index]:
                patch += nums[index]
                index += 1
            else:
                patch += (patch + 1)
                count += 1
        return count
    
# Type two:
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, added, index = 1, 0, 0
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                added += 1
        return added