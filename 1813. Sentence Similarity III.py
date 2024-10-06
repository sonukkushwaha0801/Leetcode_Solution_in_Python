# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1, w2 = s1.split(), s2.split()
        i, j, n1, n2 = 0, 0, len(w1), len(w2)
        while i < n1 and i < n2 and w1[i] == w2[i]:
            i += 1
        while j < n1 - i and j < n2 - i and w1[n1 - 1 - j] == w2[n2 - 1 - j]:
            j += 1
        return i + j == n1 or i + j == n2
    
# Another way:
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1==sentence2:
            return True
        s1,s2=sentence1.split(" "), sentence2.split(" ")
        if len(s1)<len(s2):
            small,big=s1,s2
        else:
            small, big=s2, s1
        s=0
        while s < len(small) and small[s] == big[s]:
            s += 1
        e = 0
        while e < len(small) - s and small[len(small) - 1 - e] == big[len(big) - 1 - e]:
            e += 1
        return s + e == len(small)