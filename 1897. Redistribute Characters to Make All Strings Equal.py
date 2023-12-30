# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter
from itertools import chain


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)
        f = [0] * 26
        for word in words:
            for c in word:
                f[ord(c) - ord('a')] += 1

        for x in f:
            if x % n != 0:
                return False

        return True
# Another way:
class Solution:
    def makeEqual(self, w: list[str]) -> bool:
        return all(f%len(w)==0 for f in Counter(chain(*w)).values())