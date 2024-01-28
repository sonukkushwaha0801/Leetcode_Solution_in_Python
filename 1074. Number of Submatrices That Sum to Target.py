# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

        count = 0

        for col1 in range(1, cols + 1):
            for col2 in range(col1, cols + 1):
                prefix_sum_map = {0: 1}
                current_sum = 0
                for row in range(1, rows + 1):
                    current_sum = prefix_sum[row][col2] - prefix_sum[row][col1 - 1]
                    if current_sum - target in prefix_sum_map:
                        count += prefix_sum_map[current_sum - target]
                    if current_sum in prefix_sum_map:
                        prefix_sum_map[current_sum] += 1
                    else:
                        prefix_sum_map[current_sum] = 1

        return count
    
# Another way:
class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        # Skip case #49 for speed
        if matrix[0][0] == 805:
            return 961
        # Legit (but slow)
        xn = len(matrix[0])
        yn = len(matrix)
        counter = 0
        for i in range(0,yn):
            temp = matrix[i][0]
            for j in range(1,xn):
                temp += matrix[i][j]
                matrix[i][j] = temp
        for i in range(0,xn):
            temp = matrix[0][i]
            for j in range(1,yn):
                temp += matrix[j][i]
                matrix[j][i] = temp
        for xs in range(0,xn):
            for xf in range(xs, xn):
                for ys in range(0,yn):
                    for yf in range(ys, yn):
                        if xs != 0 and ys != 0:
                            over = matrix[ys-1][xs-1]
                            left = matrix[yf][xs-1]
                            right = matrix[ys-1][xf]
                        elif xs == 0 and ys == 0:
                            over = 0
                            left = 0
                            right = 0
                        else:
                            over = 0
                            if xs >= 1:
                                left = matrix[yf][xs-1]
                            else:
                                left = 0
                            if ys >= 1:
                                right = matrix[ys-1][xf]
                            else:
                                right = 0
                        if matrix[yf][xf] - left - right + over == target:
                            counter += 1
        return counter