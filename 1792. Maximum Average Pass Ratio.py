# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq

        def gain(pass_, total):
            return (pass_ + 1) / (total + 1) - pass_ / total

        max_heap = []
        sum_ = 0.0

        for pass_, total in classes:
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        for _ in range(extraStudents):
            current_gain, pass_, total = heapq.heappop(max_heap)
            sum_ -= pass_ / total
            pass_ += 1
            total += 1
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        return sum_ / len(classes)
    
# Another way:
from heapq import heappush, heappop
from math import gcd
class Frac:
    def __init__(self, head, bot):
        self.head = head
        self.bot = bot
    def __sub__(self, other):
        top = self.head * other.bot - self.bot * other.head
        bot = self.bot*other.bot
        g = gcd(top, bot)
        top //= g
        bot //= g
        return Frac(top, bot)
    def __lt__(self, other):
        return self.head * other.bot - self.bot * other.head < 0
    def __str__(self):
        return f"{self.head}/{self.bot}"

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        minH = []
        for a, b in classes:
            heappush(minH, (Frac(a, b) - Frac(a + 1, b+ 1), Frac(a, b)))
        for _ in range(extraStudents):
            top = heappop(minH)[1]
            top.head += 1
            top.bot += 1
            heappush(minH, (top - Frac(top.head + 1, top.bot + 1), top))
            
        ans = 0.0
        for _, x in minH:
            ans += x.head / x.bot
        
        return ans / len(classes)