# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.start_events = SortedList()
        self.end_events = SortedList()

    def book(self, start: int, end: int) -> bool:
        left = bisect_right(self.end_events, start)
        right = bisect_left(self.start_events, end)
        if left == right:
            # add book
            self.start_events.add(start)
            self.end_events.add(end)
            return True
        else: return False

# Another way:
class MyCalendar:

    def __init__(self):
        self.l = [(-1, -1), (10**9+1, 10**9+1)]

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.l, (start, end))
        if self.l[index - 1][1] > start or self.l[index][0] < end:
            return False
        self.l.insert(index, (start, end))
        return True
