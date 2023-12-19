# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rows, cols = len(img), len(img[0])
        def average_value(r, c):
            total, count = 0, 0
            top = max(0, r - 1)
            bottom = min(rows, r + 2)
            left = max(0, c - 1)
            right = min(cols, c + 2)
            for row in range(top, bottom):
                for col in range(left, right):
                    total += img[row][col]
                    count += 1
            return total // count
        return [[average_value(r, c) for c in range(cols)] for r in range(rows)]
    
# another Way:
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m = len(img)
        n = len(img[0])

        temp = [0] * n

        for i in range(m):
            for j in range(n):
                sum = 0
                count = 0

                if i + 1 < m:
                    if j - 1 >= 0:
                        sum += img[i + 1][j - 1]
                        count += 1
                    sum += img[i + 1][j]
                    count += 1
                    if j + 1 < n:
                        sum += img[i + 1][j + 1]
                        count += 1

                if j + 1 < n:
                    sum += img[i][j + 1]
                    count += 1
                
                sum += img[i][j]
                count += 1

                if j - 1 >= 0:
                    sum += temp[j - 1]
                    count += 1

                if i - 1 >= 0:
                    if j - 1 >=  0:
                        sum += prev_val
                        count += 1
                    sum += temp[j]
                    count += 1
                    if j + 1 < n:
                        sum += temp[j + 1]
                        count += 1
                if i - 1 >= 0:
                    prev_val = temp[j]
                temp[j] = img[i][j]
                img[i][j] = sum // count
        return img
