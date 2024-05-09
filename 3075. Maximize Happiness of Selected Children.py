# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0
        for i in range(k):
            ans += max(0, happiness[i] - i)

        return ans
    
# Another way:
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        return sum(max(0, h - i) for i, h in enumerate(sorted(happiness, reverse=True)[:k]))