# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import groupby, zip_longest
from operator import truth


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        return [[*filter(truth, r)] for r in zip_longest(*[[*i] for _,i in groupby(sorted(nums))])]

# Another way:
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        ans = []

        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])
            ans[freq[c]].append(c)
            freq[c] += 1

        return ans