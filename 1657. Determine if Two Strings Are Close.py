# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)

        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())
      
        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())

        return sorted_values_word1 == sorted_values_word2 and keys_match

# Another way:
class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        return (f:=lambda w:(set(w),sorted(Counter(w).values())))(w1)==f(w2)