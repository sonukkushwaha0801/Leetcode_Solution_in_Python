#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers, persons):
        blooming_intervals = defaultdict(int)
        for start, end in flowers:
            blooming_intervals[start] += 1
            blooming_intervals[end + 1] -= 1
        blooming_status, bloom_count = {}, 0
        remaining_persons = sorted(persons, reverse=True) 
        for time in sorted(blooming_intervals.keys()):
            bloom_change = blooming_intervals[time] 
            while remaining_persons and time > remaining_persons[-1]:
                blooming_status[remaining_persons.pop()] = bloom_count
            if not remaining_persons:
                break

            bloom_count += bloom_change  # 
        return [blooming_status[p] if p in blooming_status else 0 for p in persons]
    
# Another way:
class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]],people: list[int]) -> list[int]:
        (beg, end), ans  = map(sorted, zip(*flowers)), []
        for person in people:
            ans.append(bisect_right(beg, person) - bisect_left (end, person))
        return ans