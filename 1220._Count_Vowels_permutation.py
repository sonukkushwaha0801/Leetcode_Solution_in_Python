# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        for _ in range(1, n):
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a
            
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        
        return (a + e + i + o + u) % MOD

# Another way:
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007

        countA = 1
        countE = 1
        countI = 1
        countO = 1
        countU = 1

        for length in range(1, n):
            nextCountA = countE
            nextCountE = (countA + countI) % MOD
            nextCountI = (countA + countE + countO + countU) % MOD
            nextCountO = (countI + countU) % MOD
            nextCountU = countA

            countA = nextCountA
            countE = nextCountE
            countI = nextCountI
            countO = nextCountO
            countU = nextCountU

        totalCount = (countA + countE + countI + countO + countU) % MOD

        return int(totalCount)