# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# Another Way:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
                return haystack.find(needle,0)
        else:
            return -1

# One more way:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, H = len(needle), len(haystack)

        for i in range(H - N + 1):
            for j in range(N):
                if needle[j] != haystack[i + j]:
                    break
                if j == N - 1:
                    return i

        return -1       