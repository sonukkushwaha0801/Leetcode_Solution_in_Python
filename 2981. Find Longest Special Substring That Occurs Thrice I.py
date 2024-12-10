# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        l, r = 1, n

        if not self.helper(s, n, l):
            return -1

        while l + 1 < r:
            mid = (l + r) // 2
            if self.helper(s, n, mid):
                l = mid
            else:
                r = mid

        return l

    def helper(self, s: str, n: int, x: int) -> bool:
        cnt = [0] * 26
        p = 0

        for i in range(n):
            while s[p] != s[i]:
                p += 1
            if i - p + 1 >= x:
                cnt[ord(s[i]) - ord('a')] += 1
            if cnt[ord(s[i]) - ord('a')] > 2:
                return True

        return False
    
# Another way:
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        mp = {}
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                unique_chars = set(substring)
                if len(unique_chars) == 1:
                    mp[substring] = mp.get(substring, 0) + 1

        maxi = -1
        for key, value in mp.items():
            if value >= 3:
                maxi = max(maxi, len(key))

        return maxi