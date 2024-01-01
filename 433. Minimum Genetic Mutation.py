# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank = set(bank) | {start}

        def dfs(st0, cnt):
            if st0 == end:
                return cnt

            bank.remove(st0)
            for i, ch0 in enumerate(st0):
                for ch1 in "ACGT":
                    if (
                        ch0 != ch1
                        and (st1 := st0[:i] + ch1 + st0[i + 1 :]) in bank
                        and (res := dfs(st1, cnt + 1)) != -1
                    ):
                        return res

            return -1

        return dfs(start, 0)

# Another way:
class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank = set(bank)
        dq = deque([(start, 0)])

        while dq:
            st0, cnt = dq.popleft()
            if st0 == end:
                return cnt

            for i, ch0 in enumerate(st0):
                for ch1 in "ACGT":
                    if ch0 != ch1 and (st1 := st0[:i] + ch1 + st0[i + 1 :]) in bank:
                        bank.remove(st1)
                        dq.append((st1, cnt + 1))

        return -1