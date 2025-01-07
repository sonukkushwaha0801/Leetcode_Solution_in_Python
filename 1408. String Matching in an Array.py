#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=" ".join(words)
        subStr=[word for word in words if arr.count(word)>1]
        return subStr
    
# Another way:

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []

        for i in range(n):
            for j in range(n):
                if i != j and words[j].find(words[i]) != -1:
                    ans.append(words[i])
                    break

        return ans
