# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        
        def palindromeCount(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            even = palindromeCount(i, i + 1)
            odd = palindromeCount(i, i)
            ans += even + odd
            
        return ans

# Another way:
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < n and s[right] == s[left]:
                count += 1
                left -= 1
                right += 1

        return count