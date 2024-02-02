# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        return [int(x) for x in [str("123456789"[i:i+d]) for d in range(2,10) for i in range(10-d)] if low<=int(x)<=high]

# Another way:
class Solution:
    def sequentialDigits(self, low: int, high: int):
        all_possible = [12, 23, 34, 45, 56, 67, 78, 89,
                        123, 234, 345, 456, 567, 678, 789,
                        1234, 2345, 3456, 4567, 5678, 6789,
                        12345, 23456, 34567, 45678, 56789,
                        123456, 234567, 345678, 456789,
                        1234567, 2345678, 3456789,
                        12345678, 23456789,
                        123456789]

        result = []

        for num in all_possible:
            if num < low:
                continue
            if num > high:
                break
            result.append(num)

        return result