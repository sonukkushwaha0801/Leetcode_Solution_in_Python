# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import Counter


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_count = [0] * (n + 1)
        for a, b in trust:
            trust_count[a] -= 1  
            trust_count[b] += 1 
        
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        
        return -1 
    
# Another way:
class Solution:
    def findJudge(self, n: int, t: list[list[int]]) -> int:
        return (n==1)*1 or [x:=set(a for a,_ in t)] and next((a for a,f in Counter(b for _,b in t).items() if f==n-1 and a not in x),-1)