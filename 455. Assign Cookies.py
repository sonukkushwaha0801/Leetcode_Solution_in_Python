# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        count = 0 
        i_g, j_s = 0, 0 
        n_g, n_s = len(g), len(s)

        while i_g < n_g and j_s < n_s:
            if g[i_g] <= s[j_s]:
                count += 1
                i_g += 1
                j_s += 1 
            else:
                j_s += 1
        return count

# Another way:
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        return s.sort() or sum(s.pop()>0 for q in sorted(g)[::-1] if s and s[-1]>=q)