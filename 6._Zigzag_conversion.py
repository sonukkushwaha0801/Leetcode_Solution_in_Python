# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        level = 0
        answer = ""
        forward = True
        for i in range(len(s)):
            ans[level].append(s[i])
            if forward:
                level += 1
            if not forward:
                level -= 1
            if level > numRows - 1:
                level -= 2
                forward = False
            if level < 0:
                level += 2
                forward = True
        for i in ans:
            for j in i:
                answer += j
        return answer

# ANother Way:
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s

        a = ['']*n
        k = index = 0

        for letter in s:
            a[k%n] += letter

            if k == n-1:
                index = 1
            if k == 0:
                index = 0
            k = k+1 if index == 0 else k-1

        result = a[0]
        for i in a[1:]:
            result += i
        return result