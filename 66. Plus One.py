# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 

# Another way:
class Solution:
    def plusOne(self, digits):
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) +1)

        return [int(temp[i]) for i in range(len(temp))]
