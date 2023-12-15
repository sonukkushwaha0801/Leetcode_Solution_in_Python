# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
from cv2 import reduce


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:

        sec = set(path[1] for path in paths)
        fir = set(path[0] for path in paths)
        ans = sec - fir
        return ans.pop()
        

# Another way:
class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        return reduce(lambda x, y: y - x, map(set, zip(*paths))).pop()