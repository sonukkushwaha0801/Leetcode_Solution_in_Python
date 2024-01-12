# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            vowels = set('aeiouAEIOU')
            return sum(1 for char in string if char in vowels)

        length = len(s)
        mid_point = length // 2

        first_half = s[:mid_point]
        second_half = s[mid_point:]

        return count_vowels(first_half) == count_vowels(second_half)

# Another way:
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt, vowels = 0, 'a,e,i,o,u,A,E,I,O,U'
        
        for i in range(len(s)//2):
            cnt += s[i] in vowels
            cnt -= s[~i] in vowels
        
        return not cnt