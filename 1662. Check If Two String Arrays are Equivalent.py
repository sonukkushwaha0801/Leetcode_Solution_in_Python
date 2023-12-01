# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#one way:

from itertools import chain, starmap, zip_longest
from operator import eq


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)
    
# Another way:
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return all(starmap(eq, zip_longest(chain.from_iterable(word1), chain.from_iterable(word2))))