# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c=len(rowSum), len(colSum)
        arr=[[0]*c for _ in range(r)]
        i, j=0, 0
        while i<r and j<c:
            x=min(rowSum[i], colSum[j])
            arr[i][j]=x
            rowSum[i]-=x
            colSum[j]-=x
            i+=(rowSum[i]==0)
            j+=(colSum[j]==0)
        return arr
        
# Another way:
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        result = [[0 for j in range(n)] for i in range(m)]
        i = j = 0
        while ( i < m and j < n ):
            result[i][j] = min(rowSum[i],colSum[j])
            rowSum[i] -= result[i][j]
            colSum[j] -= result[i][j]
            if rowSum[i]== 0:
                i+=1
            if colSum[j]==0:
                j+=1
        return result 