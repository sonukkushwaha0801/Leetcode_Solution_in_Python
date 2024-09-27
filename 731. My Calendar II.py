# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

class MyCalendarTwo:

    def __init__(self):
        # List of single and double bookings
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for dbl_start, dbl_end in self.double_bookings:
            if max(start, dbl_start) < min(end, dbl_end): 
                return False
        
        for sng_start, sng_end in self.single_bookings:
            overlap_start = max(start, sng_start)
            overlap_end = min(end, sng_end)
            if overlap_start < overlap_end: 
                self.double_bookings.append((overlap_start, overlap_end))
        self.single_bookings.append((start, end))
        return True

# Another way:
class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
            
    def book(self, start: int, end: int) -> bool:
        pieces = [(max(start, s), min(end, e)) for s,e in self.bookings 
                    if start < e and end > s]
        if len(pieces) > 0 and max([len([1 for s,e in self.bookings 
                    if st < e and en > s]) for st, en in pieces]) > 1:  return False
        self.bookings.append((start, end))
        return True