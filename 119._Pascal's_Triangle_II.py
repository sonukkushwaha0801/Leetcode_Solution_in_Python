# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - k + 1) // k
            res.append(next_val)
            prev = next_val
        return res

# Another way:
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(1, rowIndex + 1):
            prevElement = result[i - 1]
            currentElement = prevElement * (rowIndex - i + 1) // i
            result.append(currentElement)
        return result