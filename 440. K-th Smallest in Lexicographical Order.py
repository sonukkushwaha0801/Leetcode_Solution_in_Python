# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:
            steps = self.getSteps(n, cur, cur+1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
                
        return cur

    def getSteps(self, n: int, n1: int, n2: int) -> int:
        steps = 0
        while n1 <= n:
            steps += min(n+1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps

# Another way
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def steps(curr, n):
            nxt, step = curr + 1, 0
            while curr <= n:
                step += min(n + 1, nxt) - curr
                curr, nxt = curr * 10, nxt * 10
            return step

        curr = 1
        k -= 1
        while k > 0:
            step = steps(curr, n)
            if step <= k:
                k -= step
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr
 