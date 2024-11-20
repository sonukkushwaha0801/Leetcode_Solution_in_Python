# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import defaultdict
from typing import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        cnt_all = Counter(s)
        if len(cnt_all) < 3 or any(c < k for c in cnt_all.values()):
            return -1
        cnt_excess = defaultdict(int)
        ans, left = 0, 0
        for right, ch in enumerate(s):
            cnt_excess[ch] += 1
            while cnt_all[ch] - cnt_excess[ch] < k:
                cnt_excess[s[left]] -= 1
                left += 1
            ans = max(right - left + 1, ans)
        return len(s) - ans
# Another way:
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        c = Counter(s)
        if c['a'] < k or c['b'] < k or c['c'] < k:
            return -1
        n = len(s)
        left = 0
        right = n - 1
        # remove last element so that we can calculate min sliding window which ends on last element
        c[s[-1]] -= 1

        ans = n
        while left <= n:
            c[s[right%n]] += 1
            while c['a'] >= k and c['b'] >= k and c['c'] >= k and left <= n:
                ans = min(ans, right - left + 1)
                c[s[left%n]] -= 1
                left += 1
            right += 1
        return ans