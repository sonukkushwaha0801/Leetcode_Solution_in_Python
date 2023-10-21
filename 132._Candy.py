# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def candy(self, R):
        n, ans = len(R), [1]*len(R)
        
        for i in range(n-1):
            if R[i] < R[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])
                
        for i in range(n-2, -1, -1):
            if R[i+1] < R[i]:
                ans[i] = max(1 + ans[i+1], ans[i])
        
        return sum(ans)

#Another way:
class Solution:
    def candy(self, R):
        n, ans = len(R), [1]*len(R)
        
        for i in range(n-1):
            if R[i] < R[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])
                
        for i in range(n-2, -1, -1):
            if R[i+1] < R[i]:
                ans[i] = max(1 + ans[i+1], ans[i])
        
        return sum(ans)