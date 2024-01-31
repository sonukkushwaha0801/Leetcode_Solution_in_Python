# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures):
        deq = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if not deq:
                deq.appendleft(i)
                res[i] = 0
            else:
                while deq and temperatures[i] >= temperatures[deq[0]]:
                    deq.popleft()

                if not deq:
                    res[i] = 0
                else:
                    res[i] = deq[0] - i

                deq.appendleft(i)

        return res

# Another way:
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            ans[i] = st[-1] - i if st else 0
            st.append(i)
        
        return ans