# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x-y) for x, y in zip(sorted(seats), sorted(students)))
        
# Type two:
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total_moves = 0
        
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
        
        return total_moves