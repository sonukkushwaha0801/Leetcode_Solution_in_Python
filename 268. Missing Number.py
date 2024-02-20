# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        v = [-1] * (n + 1)
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] == -1:
                return i
        return 0

# Another way:
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
