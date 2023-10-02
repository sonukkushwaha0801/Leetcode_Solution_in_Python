# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])

# Second Type:
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[::-1], s.split()))