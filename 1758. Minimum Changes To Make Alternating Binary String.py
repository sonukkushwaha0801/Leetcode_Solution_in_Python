# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        op=[0]*2
    
        for i in range(0, n, 2):
            op[ord(s[i])&1]+=1
            if i+1<n:
                op[1-(ord(s[i+1])&1)]+=1
        return min(op[0], op[1])        

# Another way:
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count1, count2 = 0, 0

        for i in range(n):
            if i % 2 == 0:
                count1 += s[i] != '0'
                count2 += s[i] != '1'
            else:
                count1 += s[i] != '1'
                count2 += s[i] != '0'

        return min(count1, count2)
