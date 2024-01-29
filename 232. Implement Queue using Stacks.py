# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

#Anthoer way:
class MyQueue:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        return self.s.append(x)

    def pop(self) -> int:
        return self.s.popleft()

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        if len(self.s) == 0:
            return True 
        else:
            return False 
