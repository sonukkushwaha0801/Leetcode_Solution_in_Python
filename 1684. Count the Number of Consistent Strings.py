# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        arr = [0] * 26
        for c in allowed:
            arr[ord(c) - ord('a')] = 1
        
        count = 0
        for word in words:
            flag = 1
            for char in word:
                if arr[ord(char) - ord('a')] == 0:
                    flag = 0
                    break
            count += flag
        return count

# Another way:
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(1 for word in words if set(word).issubset(set(allowed)))
        