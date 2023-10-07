# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        MOD = 10**9 + 7

        def helper(indx, curr_max, cost, m, dp):

            tpl = (indx, curr_max, cost)

            if tpl in dp:
                return dp[tpl]

            if indx == 1 and cost == 1:
                return 1
            elif indx == 1:
                return 0
            elif cost == 0:
                return 0
            
            numberWays = 0

            for j in range(1, m+1):
                if j <= curr_max:
                    numberWays += helper(indx-1, curr_max, cost, m, dp)
                else:
                    numberWays += helper(indx-1, j, cost-1, m, dp)
            dp[tpl] = numberWays % MOD

            return dp[tpl]

        ans = 0

        dp = {}

        for j in range(1, m+1):
            ans = (ans + helper(n, j, k, m, dp)) % MOD
            
        return ans

# Another Way:
class Solution:
    def dp(self,i,n,m,k,last,dct):
        if i==n:
            if k==0:
                return 1
            return 0
        if (i,k,last) in dct:
            return dct[(i,k,last)]
        val=0
        for j in range(1,m+1):
            if j<=last:
                val+=self.dp(i+1,n,m,k,last,dct)
            else:
                val+=self.dp(i+1,n,m,k-1,j,dct)
        dct[(i,k,last)]=val
        return val%1000000007

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        return self.dp(0,n,m,k,-1,{})%1000000007