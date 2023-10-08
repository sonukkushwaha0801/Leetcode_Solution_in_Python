# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(product, dp[i - 1][j - 1] + product, dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
    
# Another way:
from functools import cache
class Solution:
    def maxDotProduct(self, nums1, nums2):
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')
            return max(nums1[i] * nums2[j] + dp(i + 1, j + 1), nums1[i] * nums2[j], dp(i + 1, j), dp(i, j + 1))
        return dp(0, 0)
       
    