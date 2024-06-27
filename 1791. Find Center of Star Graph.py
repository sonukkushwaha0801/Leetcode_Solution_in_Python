# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return e[0][0] if e[0][0]==e[1][0] or e[0][0]==e[1][1] else e[0][1]
        
# Another way:
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()