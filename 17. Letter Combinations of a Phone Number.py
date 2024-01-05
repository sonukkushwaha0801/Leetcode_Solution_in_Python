# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            '1': ''    , '2': 'abc', '3': 'def',
            '4': 'ghi' , '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        return list(map(''.join, product(*map(phone.get, digits)))) if digits else []

# Another way:
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        return list("".join(c) for c in product(*[[chr(ord('a') + (ord(d) - ord('2')) * 3 + i) for i in range(0 + (d > '7'), 3 + (d > '6') + (d == '9'))] for d in digits]) if c)