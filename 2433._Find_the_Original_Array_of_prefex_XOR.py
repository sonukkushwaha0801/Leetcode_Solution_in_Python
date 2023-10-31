# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        ans = [0] * n
        ans[0]=pref[0]
        for i in range(1,n):
            ans[i]=pref[i]^pref[i-1]
        return ans

# ANother way:
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        return [pref[0]]+[(pref[i-1]^pref[i]) for i in range(1,len(pref))]