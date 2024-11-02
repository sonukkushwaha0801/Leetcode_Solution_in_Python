# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word=sentence.split()
        #print(word,type(word))
        for i in range(len(word)-1):
            if word[i][-1]==word[i+1][0]:
                pass
            else:
                return False
        return True if word[0][0]==word[-1][-1] else False

#Another WAy:

from re import search
class Solution:
    def isCircularSentence(self, s: str) -> bool:
        return s[0]==s[-1] and not search(r'(.) (?!\1)',s)