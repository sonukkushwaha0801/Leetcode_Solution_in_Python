# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

# Another way:
class Solution:
    def makeGood(self, s: str) -> str:
        sb = list(s)
        flag = 0
        while flag == 0 and len(sb) > 0:
            flag = 1
            i = 0
            while i < len(sb) - 1:
                if self.isGreat(sb, i):
                    del sb[i:i+2]
                    flag = 0
                i += 1
        return ''.join(sb)

    def isGreat(self, sb, i):
        return ord(sb[i]) == ord(sb[i + 1]) + 32 or ord(sb[i]) == ord(sb[i + 1]) - 32