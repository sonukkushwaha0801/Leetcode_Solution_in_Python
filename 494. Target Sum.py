# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if target > total_sum or (total_sum - target) % 2 != 0:
            return 0
        s = (total_sum - target) // 2
        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for j in range(s, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[s]
    

# Another way:
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def recurtion(idx, cur_sum):
            if idx == len(nums):
                return 1 if cur_sum == target else 0
            if (idx, cur_sum) in dp:
                return dp[(idx, cur_sum)]

            add = recurtion(idx + 1, cur_sum + nums[idx])
            subtract = recurtion(idx + 1, cur_sum - nums[idx])
            dp[(idx, cur_sum)] = add + subtract
            return add + subtract
        return recurtion(0, 0)