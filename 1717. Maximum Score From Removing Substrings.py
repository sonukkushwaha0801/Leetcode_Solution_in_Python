# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        stack: list[str] = []
        for char in s:
            if char == top[1] and stack and stack[-1] == top[0]:
                res += top_score
                stack.pop()  
            else:
                stack.append(char)

        new_stack: list[str] = []
        for char in stack:
            if char == bot[1] and new_stack and new_stack[-1] == bot[0]:
                res += bot_score
                new_stack.pop()
            else:
                new_stack.append(char)

        return res
    
# Another way:
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def process(stack, s, pattern, points):
            for char in s:
                if stack and stack[-1] == pattern[0] and char == pattern[1]:
                    stack.pop()
                    points[0] += points[1]
                else:
                    stack.append(char)
            return stack
        
        points = [0, 0]
        if x > y:
            points[1] = x
            stack = []
            stack = process(stack, s, "ab", points)
            points[1] = y
            stack = process([], ''.join(stack), "ba", points)
        else:
            points[1] = y
            stack = []
            stack = process(stack, s, "ba", points)
            points[1] = x
            stack = process([], ''.join(stack), "ab", points)
        
        return points[0]