# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#Solution:
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        def dfs(curr):
            output.append(curr)
            if curr*10 <= n:
                dfs(curr*10)
            if curr+1 <= n and curr % 10 != 9:
                dfs(curr+1)   
        dfs(1)
        return output
    
# Another way:
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        x = 1
        f = True
        while x > 0:
            if f:
                ans.append(x)
            if f and x * 10 <= n:
                f = True
                x = x * 10
            elif x % 10 != 9 and x + 1 <= n:
                f = True
                x = x + 1
            else:
                f = False
                x = x // 10
        return ans
            
        