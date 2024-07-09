# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prepare, n=0, len(customers)
        return sum((prepare:=max(t[0],prepare)+t[1])-t[0] for t in customers)/n
    
# Another way:
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        
        for arrival, time_needed in customers:
            if current_time < arrival:
                current_time = arrival
            finish_time = current_time + time_needed
            waiting_time = finish_time - arrival
            total_waiting_time += waiting_time
            current_time = finish_time
        
        average_waiting_time = total_waiting_time / len(customers)
        return average_waiting_time