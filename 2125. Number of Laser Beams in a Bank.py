# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from cv2 import reduce


class Solution:
    def numberOfBeams(self, bank):
        ans, temp = 0, 0
        for s in bank:
            n = s.count('1')
            if n == 0:
                continue
            ans += temp * n
            temp = n
        return ans


# Another way:
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        return reduce(lambda p,r:(p[0]+p[1]*c,c) if (c:=r.count('1')) else p, bank, (0,0))[0]