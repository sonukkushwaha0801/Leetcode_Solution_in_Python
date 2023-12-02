# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = []
        for i in words:
            for j in i:
                if chars.count(j) < i.count(j):
                    break
            else:
                result.append(len(i)) 
        return sum(result)

            
# Another way:
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(word) for word in words if all(word.count(char) <= chars.count(char) for char in set(word)))