#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        count_char = Counter(s)
        s_vowels = []
        for char in count_char.keys():
            if char in vowels:
                s_vowels.append(char)                
                s = s.replace(char, '_')                              
        s_vowels.sort()
        for char in s_vowels:
            s = s.replace('_', char, count_char[char])
        return s
    
# Another way:

class Solution:
    def isVowel(self, c):
        return c.lower() in ['a', 'e', 'i', 'o', 'u']

    def sortVowels(self, s):
        t = ""       
        temp = ""     
        for char in s:
            if self.isVowel(char):
                temp += char

        temp = ''.join(sorted(temp))

        j = 0
        for char in s:
            if self.isVowel(char):
                t += temp[j]
                j += 1
            else:
                t += char

        return t
