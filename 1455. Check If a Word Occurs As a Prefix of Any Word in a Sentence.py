# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1

# Another way:
class Solution:
    def isPrefixOfWord(self, s: str, w: str) -> int:
        return (i:=(' '+s).find(' '+w))>=0 and s[:i].count(' ')+1 or -1