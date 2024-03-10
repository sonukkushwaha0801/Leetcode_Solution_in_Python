# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return set(nums1) & set(nums2)
        
# Another way:
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        res = []
        for num in set_1:
            if num in set_2:
                res.append(num)
        return res