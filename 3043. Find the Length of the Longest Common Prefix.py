# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def prefix(a, b):
            a, b = str(a), str(b)
            length = min(len(a), len(b))
            for i in range(length):
                if a[i] != b[i]:
                    return i  
            return length  
        result = 0
        d1 = sorted(map(str, set(arr1)))
        d2 = sorted(map(str, set(arr2)))
        i = j = 0
        while i < len(d1) and j < len(d2):
            result = max(result, prefix(d1[i], d2[j]))
            if d1[i] < d2[j]:
                i += 1
            else:
                j += 1
        return result
    
# Another way:
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        X, Y = len(arr1), len(arr2)

        s = set()
        for i in arr2:
            copy = i
            # 12345 -> 1, 12, 123, 1234, 12345
            s.add(copy)
            copy = copy // 10
            while copy > 0:
                s.add(copy)
                copy = copy // 10
        
        t = set()
        for i in arr1:
            copy = i
            # 12345 -> 1, 12, 123, 1234, 12345
            t.add(copy)
            copy = copy // 10
            while copy > 0:
                t.add(copy)
                copy = copy // 10
                
        ans = 0
        for i in t:
            if i in s:
                ans = max(ans, len(str(i)))
                
        return ans