# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [] 
        last_occurrence = {} 
        visited = set()
        
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and s[i] < stack[-1] and last_occurrence[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(s[i])
            visited.add(s[i])
        return "".join(stack)
    
# Second Way:
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set() 
        last_occ = {c: i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):
            if c not in seen:
                
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        
        return ''.join(stack)