# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            odd = self.expandAroundCenter(s, i, i)
            even = self.expandAroundCenter(s, i, i + 1)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest


# Another way:
class Solution:
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i + 1)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest
