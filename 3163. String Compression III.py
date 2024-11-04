# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)
        
        while i < n:
            char = word[i]
            count = 0
            while i < n and word[i] == char and count < 9:
                count += 1
                i += 1
            comp += str(count) + char
        
        return comp
    
# Another way:
class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        prev = word[0]
        count = 1

        for i in range(1, len(word)):
            if prev != word[i]:
                ans += str(count) + prev
                count = 1
                prev = word[i]
            else:
                if count == 9:
                    ans += str(count) + prev
                    count = 1
                else:
                    count += 1

        ans += str(count) + prev
        return ans