# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n<3 or m<3:
            return 0
        ans = 0
        ch = 0
        for x in range(n-2):
            for y in range(m-2):
                dic = {0:1,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:1,11:1,12:1,13:1,14:1,15:1}
                flag = 0
                c = 0
                d = 0
                for i in range(3):
                    a = 0
                    b = 0
                    for j in range(3):
                        val = grid[x+i][y+j]
                        
                        if dic[val]==1:
                            flag = 1
                            break
                        dic[val] = 1
                        a += val
                        b += grid[x+j][y+i]
                        if (i==j):
                            c += grid[x+i][y+j]
                    if (i==0):
                            ch = a
                    if flag or ch!=a or ch!=b:
                        flag = 1
                        break
                    d += grid[x+i][y+(2-i)]
                if flag==0:
                    if ch==c and ch==d:
                        ans += 1
        return ans
    
# Another way:
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def valid(row, column):
            seen = set()
            c = [0] * 3
            r = [0] * 3
            for i in range(3):
                for j in range(3):
                    number = grid[row + i][column + j]
                    if number > 9 or number < 1 or number in seen:
                        return 0
                    seen.add(number)
                    c[j] += number
                    r[i] += number
            rowSum = r[0] == r[1] == r[2]
            colSum = c[0] == c[1] == c[2]
            diagonalSum = grid[row][column] + grid[row + 2][column + 2] == grid[row][column + 2] + grid[row + 2][column]
            return 1 if diagonalSum and rowSum and colSum else 0

        rows, columns = len(grid), len(grid[0])
        count = 0

        for row in range(rows - 2):
            for column in range(columns - 2):
                count += valid(row, column)
        return count

                


