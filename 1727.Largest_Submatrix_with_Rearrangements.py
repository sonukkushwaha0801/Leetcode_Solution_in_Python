# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0
        
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0
                
        for i in range(m): 
            matrix[i].sort(reverse=1)
            for j in range(n):
                ans = max(ans, (j+1)*matrix[i][j])
        return ans
    
#Another way:
class Solution:
    def largestSubmatrix(self, mat: list[list[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        ans=0
        for row in range(m):
            for col in range(n):
                if mat[row][col]!=0 and row>0:
                    mat[row][col]+=mat[row-1][col]
                
            
            curr_row=sorted(mat[row],reverse=True)
            for i in range(n):
                ans=max(ans,curr_row[i]*(i+1))
            
        return ans
        