# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        arr = []
        for x in range(n):
            arr.append((heights[x], names[x]))
        
        arr.sort(reverse = True)

        for x in range(n):
            names[x] = arr[x][1]
        
        return names

# Type two:
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(heights)), key= lambda i: -heights[i])]