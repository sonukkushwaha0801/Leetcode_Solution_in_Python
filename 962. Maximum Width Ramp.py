# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def maxWidthRamp(self, A):
        stack = []
        res = 0   
        n = len(A)
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        for i in range(n - 1, res, -1):
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack[-1])
                stack.pop()  

        return res
    
# One liner:
class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        return max(map(sub,a:=[i for _,i in sorted((v,i) for i,v in enumerate(a))],accumulate(a,min)))