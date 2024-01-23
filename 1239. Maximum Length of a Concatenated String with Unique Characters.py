# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import chain, combinations


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def is_unique(subseq):
            return len(subseq) == len(set(subseq))
        def backtrack(start, current_subseq):
            nonlocal max_length
            if is_unique(current_subseq):
                max_length = max(max_length, len(current_subseq))
            for i in range(start, len(arr)):
                backtrack(i + 1, current_subseq + arr[i])
        max_length = 0
        backtrack(0, "")
        return max_length

# Another way:
class Solution:
    def maxLength(self, a: list[str]) -> int:
        return max(q for k in range(len(a)+1) for c in combinations(a,k) if (q:=len({*chain(*c)}))==len(''.join(c)))