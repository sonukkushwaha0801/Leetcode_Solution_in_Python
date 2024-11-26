# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isUndefeated = [True] * n
        
        for winner, loser in edges:
            isUndefeated[loser] = False
            
        champion = -1
        championCount = 0
        
        for team in range(n):
            if isUndefeated[team]:
                champion = team
                championCount += 1
                
        if championCount == 1:
            return champion
            
        return -1
    
# Another way:
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = set(range(n))
        for _, weak in edges:
            teams.discard(weak)
        return -1 if len(teams) > 1 else list(teams)[0]