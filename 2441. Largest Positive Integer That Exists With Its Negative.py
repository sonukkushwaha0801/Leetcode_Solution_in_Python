# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ans = -1
        seen = set()

        for num in nums:
            if -num in seen:
                ans = max(ans, abs(num))
            else:
                seen.add(num)

        return ans

# Another solution:
class Solution:
    def findMaxK(self, a: list[int]) -> int:
        return max(filter(lambda v:-v in d,d:={*a}),default=-1)