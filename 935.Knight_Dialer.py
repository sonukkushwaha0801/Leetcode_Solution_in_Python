# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        for _ in range(n-1):
            dp_next = [0] * 10
            for digit in range(10):
                for move_digit in moves[digit]:
                    dp_next[digit] += dp[move_digit]
                    
            dp = dp_next
        
        return sum(dp) % (10**9 + 7)

# Another way:
class Solution(object):

    def knightDialer(self, n):

        moves = {0:[4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}

        d = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
        INICIAL = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        newD = INICIAL.copy()


        for i in range(n-1):

            for j in range(len(d)):

                for k in range(len(moves[j])):
                    
                    newD[ moves[j][k] ] += d[j]

                d[j] = 0

            d = newD.copy()
            newD = INICIAL.copy()
        
        res = 0
        for i in range(len(d)):
            res += d[i]
         
        return res % ( 10**9 + 7 )
        