# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r=word.find(ch)
        if r==-1: return word
        s=list(word[:r+1])
        t=list(word[r+1:])
        s.reverse()
        return "".join(s+t)

# Another way:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c=0
        for i in range(len(word)):
            if word[i]==ch:   
                c=i 
                break
        st=word[0:c+1][::-1]+word[c+1:]
        return st
        