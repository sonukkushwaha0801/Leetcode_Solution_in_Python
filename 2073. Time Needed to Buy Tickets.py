# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def timeRequiredToBuy(self, t: list[int], k: int) -> int:
        n=len(t)
        x=t[k]
        time=0
        for i, y in enumerate(t):
            buy=x
            if i>k: buy=x-1
            time+=min(buy, y)
        return time
    
# Another way:
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        c=0
        while True:
            if tickets[k]==0:    break
            for i in range(len(tickets)):
                if tickets[k]==0:    break
                if tickets[i]>0:
                    tickets[i]-=1
                    c+=1
        return c