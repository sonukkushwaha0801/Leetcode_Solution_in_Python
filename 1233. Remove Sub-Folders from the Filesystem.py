# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        return result
    
# Another way:
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        f_set = set()

        for f in folder:
            chars = f[1:].split('/')
            cur = ''
            for c in chars:
                cur += '/' + c
                if cur in f_set: break
            else:
                f_set.add(cur)

        return list(f_set)