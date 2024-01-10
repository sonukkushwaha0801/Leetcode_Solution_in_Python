# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def generateParenthesis(self, n: int):
        
        
        def helper(ans, s, left, right):
            if left==0 and right==0:
                ans.append(s)
                
            if left>0:
                helper(ans, s+'(', left-1, right)
                
            if right>0 and left<right:
                helper(ans, s+')', left, right-1)
        
        ans = []
        helper(ans, '', n, n)
        
        return ans
    
# Another way:
class Solution:
    def f(self, open, close, ans, res):
        # base case
        if open == 0 and close == 0:
            ans.append(res)
            return

        if open > 0:
            self.f(open - 1, close, ans, res + '(')

        if close > open:
            self.f(open, close - 1, ans, res + ')')

    def generateParenthesis(self, n):
        ans = []
        self.f(n, n, ans, "")
        return ans