# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import deque
from typing import List


def get_degrees_count(favorite_connections: list[int], people_count: int) -> list[int]:
    result = [0] * people_count
    for favorite_person in favorite_connections:
        result[favorite_person] += 1
    return result


def calculate_max_depths(favorite_connections: list[int], degrees_count: list[int], people_count: int):
    max_depths = [1] * people_count
    queue = deque(i for i, degrees in enumerate(degrees_count) if degrees == 0)
    while queue:  
        current_person = queue.popleft()
        current_persons_favorite = favorite_connections[current_person] 
        max_depths[current_persons_favorite] = max_depths[current_person] + 1
        degrees_count[current_persons_favorite] -= 1
        if degrees_count[current_persons_favorite] == 0:
            queue.append(current_persons_favorite)
    return max_depths


class Solution:
    def maximumInvitations(self, favorite_connections: list[int]) -> int:
        people_count = len(favorite_connections)
        degrees_count: list[int] = get_degrees_count(favorite_connections, people_count)
        max_depths = calculate_max_depths(favorite_connections, degrees_count, people_count)

        max_ring_size = sum_chain_size = 0

        for current_person, degree in enumerate(degrees_count):
            if degree == 0:
                continue
            degrees_count[current_person] = 0
            ring_size = 1
            persons_favorite = favorite_connections[current_person]

            while persons_favorite != current_person:
                degrees_count[persons_favorite] = 0
                ring_size += 1
                persons_favorite = favorite_connections[persons_favorite]

            if ring_size == 2: 
                sum_chain_size += max_depths[current_person] + max_depths[favorite_connections[current_person]]
            else:
                max_ring_size = max(max_ring_size, ring_size)

        return max(max_ring_size, sum_chain_size)

# Another way:

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        fav_counter = [0] * n 
        for f in favorite:
            fav_counter[f] += 1
        root_employees = deque(emp for emp, fav_count in enumerate(fav_counter) if fav_count == 0)
        chain_lengths = [1] * n
        while root_employees: 
            root_emp = root_employees.popleft() 
            root_fav = favorite[root_emp]
            chain_lengths[root_fav] = chain_lengths[root_emp] + 1
            fav_counter[root_fav] -= 1 
            if fav_counter[root_fav] == 0: 
                root_employees.append(root_fav)
        max_cycle = 0
        sum_groups = 0
        for start_emp, fav_count in enumerate(fav_counter):
            if fav_count == 0: continue
            fav_counter[start_emp] = 0

            cycle_len = 1
            cur_emp = favorite[start_emp]
            while cur_emp != start_emp:
                fav_counter[cur_emp] = 0  
                cycle_len += 1
                cur_emp = favorite[cur_emp]

            if cycle_len == 2:
                sum_groups += chain_lengths[start_emp] + chain_lengths[favorite[start_emp]]
            else: 
                max_cycle = max(max_cycle, cycle_len)

        return max(max_cycle, sum_groups) 