# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def countSubarrays(self, nums: list[int], mink: int, maxK: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1
        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                bad_idx = i
            if num == mink:
                left_idx = i
            if num == maxK:
                right_idx = i
            res += max(0, min(left_idx, right_idx) - bad_idx)
        return res
    
# Another way:
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        left = 0
        pmin = -1
        pmax = -1

        for right in range(len(nums)):
            num = nums[right]
            if num < minK or num > maxK:
                left = right + 1
                pmin = -1
                pmax = -1
            else:
                if num == minK:
                    pmin = right
                if num == maxK:
                    pmax = right
                res += max(0, min(pmin, pmax) - left + 1)

        return res