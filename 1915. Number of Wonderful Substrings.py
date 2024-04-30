# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dic = {chr(ord('a') + i) : (1 << i) for i in range(10)}
        diff = list(dic.values())
        masks = {h:0 for h in range(1 << 10)}
        mask = 0
        masks[0] += 1
        for c in word:
            mask ^= dic[c]
            masks[mask] += 1
        result= 0
        for mask in masks:
            result+= (masks[mask] - 1) * (masks[mask])
            for m in diff:
                result+= masks[mask] * masks[mask ^ m]
        return result// 2
# type second:  

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        mask = 0
        prefix = defaultdict(int)
        prefix[0] += 1
        result= 0
        for w in word:
            mask ^= 1 << (ord(w) - ord('a'))
            result+= prefix[mask]
            for i in range(10):
                tmp = mask ^ (1 << i)
                result+= prefix[tmp]
            prefix[mask] += 1
        return result