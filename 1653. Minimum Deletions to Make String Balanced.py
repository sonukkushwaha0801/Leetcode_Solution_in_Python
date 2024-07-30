# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def minimumDeletions(self, s: str) -> int:
        cntA, ans=0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i]=='a': cntA+=1
            else: ans=min(ans+1, cntA)
        return ans
        
# Another way:
class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a = s.count('a') 
        left_b = 0 
        min_deletions = total_a  
        
        for char in s:
            if char == 'b':
                left_b += 1 
            else: 
                total_a -= 1 
            
            min_deletions = min(min_deletions, left_b + total_a)
        
        return min_deletions