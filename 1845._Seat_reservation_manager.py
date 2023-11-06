# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.last = 0
        self.pq = []

    def reserve(self) -> int:
        if not self.pq:
            self.last += 1
            return self.last
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.pq, seatNumber)

# Another way:
class SeatManager:

    # O(logn)
    def __init__(self, n: int):
        self.unres = [i for i in range(1,n+1)]
        

    def reserve(self) -> int:
        return heapq.heappop(self.unres)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres,seatNumber)
        

