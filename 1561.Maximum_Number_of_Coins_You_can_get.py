# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:len(piles)*2//3:2])
        
# Another way:
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        cnt = [0] * (max(piles) + 1)
        s, ans = len(piles), 0
        # count pile of coins
        for p in piles:
            cnt[p] += 1
        i, j = 0, len(cnt) - 1
        while s:
            # find the next available pile for the most and the least, repectively
            while not cnt[j]:
                j -= 1
            while not cnt[i]:
                i += 1
            if cnt[j] >= 2:
                # there are 2 piles of max coins, grab it as Alice does since the second most is also there
                ans += j
                cnt[j] -= 2
            elif cnt[j] == 1:
                # there's only 1 pile of max coins which belongs to Alice, proceed to find the second most
                cnt[j] -= 1
                while not cnt[j]:
                    j -= 1
                ans += j
                cnt[j] -= 1
            # i, as the minimum coins, is always for Bob
            cnt[i] -= 1
            s -= 3

        return ans