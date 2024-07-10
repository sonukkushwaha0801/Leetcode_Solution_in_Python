# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import reduce
from typing import List


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0

        for folder in logs:
            if folder == '../':
                depth = max(depth - 1, 0)
            elif folder == './':
                continue
            else:
                depth += 1

        return depth
    
# Another way:
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        return reduce(lambda p, o: max(p + {"./": 0, "../": -1}.get(o, 1), 0),logs, 0)