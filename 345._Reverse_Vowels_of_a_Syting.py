# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def reverseVowels(self, s: str) -> str:
        str_index = []
        vowel = []
        res = []
        pos = -1
        for index, value in enumerate(s):
            if value in 'aeiouAEIOU':
                str_index.append(-1)
                vowel.append(value)
            else:
                str_index.append(index)
        for index in str_index:
            if index < 0:
                res.append(vowel[pos])
                pos -= 1
            else:
                res.append(s[index])
        return ''.join(res)

# Type Second:
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a = [f for f in s[::-1] if f in v]
        n = ''
        j = 0
        for i in s:
            if i in v:
                n += a[j]
                j += 1
            else:
                n += i
        return n