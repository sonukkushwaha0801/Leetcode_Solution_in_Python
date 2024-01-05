# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Another way:
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        subseq = []
        for n in nums:
            index = bisect.bisect_left(subseq, n) 
            if index >= len(subseq):
                subseq.append(n)
            else:
                subseq[index] = n
        return len(subseq)
            