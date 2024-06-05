# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from functools import reduce
from operator import and_
from typing import Counter, List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])
        
        for word in words[1:]:
            word_counter = Counter(word)
            for char in common_counter:
                common_counter[char] = min(common_counter[char], word_counter[char])
                
        result = []
        for char, freq in common_counter.items():
            result.extend([char] * freq)
        
        return result
    
# Another solution:
class Solution:
    def commonChars(self, w: List[str]) -> List[str]:
        return reduce(and_,map(Counter,w)).elements()