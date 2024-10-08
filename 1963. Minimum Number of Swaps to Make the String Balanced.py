# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)
        return (max_imbalance + 1) // 2
    
# Another way:
class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        swaps=0
        for c in s:
            if c=='[':
                stack.append(c)
            else:
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    swaps+=1
        return (swaps+1)//2