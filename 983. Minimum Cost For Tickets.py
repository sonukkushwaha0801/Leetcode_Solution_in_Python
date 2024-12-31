# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [-1] * n 
        
        def solve(in_):
            if in_ >= n:  
                return 0
            
            if dp[in_] != -1: 
                return dp[in_]
            
            ans = float('inf')
            ans = min(ans, costs[0] + solve(in_ + 1))
            
            num = in_
            while num < n and days[num] <= days[in_] + 6:
                num += 1
            ans = min(ans, costs[1] + solve(num))
            
            ij = in_
            while ij < n and days[ij] <= days[in_] + 29:
                ij += 1
            ans = min(ans, costs[2] + solve(ij))
            
            dp[in_] = ans 
            return ans
        
        return solve(0) 