# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans=[]
        vowelStrings = 'aeiou'
        v = [1 if (word[0] in vowelStrings) and (word[-1] in vowelStrings) else 0 for word in words]
        pref = [0] * len(v)
        pref[0] = v[0]
        for i in range(1, len(v)):
            pref[i] = pref[i - 1] + v[i]
        print(pref)

        for i,j in queries:
            ans.append(pref[j] if i == 0 else pref[j] - pref[i - 1])
        return ans
    
# Another way:
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = len(words)
        temp = [0]*l
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(l):
            if words[i][0] in vowels and words[i][-1] in vowels:
                temp[i] = temp[i-1]+1
            else:
                temp[i] = temp[i-1]


        n = len(queries)
        res = [0]*n
        for i in range(n):
            q = queries[i]
            l, r = q[0], q[1]
            if l == 0:
                res[i] = temp[r]
            else:
                res[i] = temp[r]-temp[l-1]
        return res